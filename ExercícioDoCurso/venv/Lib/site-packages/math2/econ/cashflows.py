from collections.abc import Iterable, Iterator
from functools import total_ordering
from itertools import accumulate
from math import inf
from typing import Any, Optional

from math2.analysis import interpolate
from math2.calc import root
from math2.econ.factors import ap
from math2.econ.ints import CompInt, EfInt, Int
from math2.misc import arange
from math2.typing import SupportsLessThan
from math2.utils import default, windowed


@total_ordering
class CashFlow(SupportsLessThan):
    """CashFlow is the class for cash flows."""

    def __init__(self, time: float, amount: float):
        self.time = time
        self.amount = amount

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, CashFlow):
            return self.time == other.time
        else:
            return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, CashFlow):
            return self.time < other.time
        else:
            return NotImplemented


def disc(cash_flow: CashFlow, i: Int) -> CashFlow:
    """Discounts the cash flow from a copied value.

    :param cash_flow: The cash flow.
    :param i: The interest at which is discounted.
    :return: The discounted copy of the cash flow.
    """
    return CashFlow(0, cash_flow.amount / i.to_factor(cash_flow.time))


def payback(cash_flows: Iterable[CashFlow], cost: float) -> float:
    """Calculates the payback period of the cash flows.

    :param cash_flows: The cash flows.
    :param cost: The cost to pay back.
    :return: The payback period.
    """
    prefix_sums = tuple(accumulate(cash_flow.amount for cash_flow in sorted(cash_flows)))

    if cost <= 0 or prefix_sums and cost <= prefix_sums[0]:
        return 0
    else:
        for i, (x, y) in enumerate(windowed(prefix_sums, 2)):
            if y >= cost:
                return interpolate(cost, (x, y), (i, i + 1))
        else:
            return inf


def disc_payback(cash_flows: Iterable[CashFlow], cost: float, i: Int) -> float:
    """Calculates the discounted payback period of the cash flows at the given interest value.

    :param cash_flows: The cash flows.
    :param cost: The cost to pay back.
    :param i: The interest at which the cash flows are discounted.
    :return: The payback period.
    """
    return payback((disc(cash_flow, i) for cash_flow in cash_flows), cost)


def pw(cash_flows: Iterable[CashFlow], i: Int) -> float:
    """Calculates the present worth of the supplied cash flows at the interest.

    :param cash_flows: The cash flows.
    :param i: The interest rate.
    :return: The present worth.
    """
    return sum(disc(cash_flow, i).amount for cash_flow in cash_flows)


def rpw(cash_flows: Iterable[CashFlow], i: Int, total_life: float) -> float:
    """Calculates the repeated present worth of the supplied cash flows at the interest and at the total life.

    :param cash_flows: The cash flows.
    :param i: The interest rate.
    :param total_life: The total life.
    :return: The repeated present worth.
    """
    return pw(repeated(cash_flows, total_life), i)


def aw(cash_flows: Iterable[CashFlow], i: CompInt, total_life: Optional[float] = None) -> float:
    """Calculates the annual worth of the supplied cash flows at the interest.

    :param cash_flows: The cash flows.
    :param i: The interest.
    :param total_life: The optional total life.
    :return: The annual worth.
    """
    if isinstance(cash_flows, Iterator):
        return aw(tuple(cash_flows), i, total_life)
    else:
        return pw(cash_flows, i) * ap(i.to_ef().rate, default(total_life, life(cash_flows)))


def irr(cash_flows: Iterable[CashFlow], init_guess: CompInt, eps: float) -> EfInt:
    """Calculates the internal rate of return using the initial guess.

    :param cash_flows: The cash flows.
    :param init_guess: The initial guess.
    :param eps: The desired accuracy.
    :return: The internal rate of return.
    """
    if isinstance(cash_flows, Iterator):
        return irr(tuple(cash_flows), init_guess, eps)
    else:
        return EfInt(root(lambda i: pw(cash_flows, EfInt(i)), init_guess.to_ef().rate, eps))


def yield_(cash_flows: Iterable[CashFlow], price: float, init_guess: CompInt, eps: float) -> EfInt:
    """Calculates the yield of the cash flows using the initial guess.

    :param cash_flows: The cash flows.
    :param price: The price.
    :param init_guess: The initial guess.
    :param eps: The desired accuracy.
    :return: The internal rate of return.
    """
    if isinstance(cash_flows, Iterator):
        return yield_(tuple(cash_flows), price, init_guess, eps)
    else:
        return EfInt(root(lambda y: pw(cash_flows, EfInt(y)) - price, init_guess.to_ef().rate, eps))


def life(cash_flows: Iterable[CashFlow]) -> float:
    """Calculates the life of the cash flows.

    :param cash_flows: The cash flows.
    :return: The life.
    """
    return max(cash_flow.time for cash_flow in cash_flows)


def repeated(cash_flows: Iterable[CashFlow], total_life: float) -> Iterator[CashFlow]:
    """Repeats the cash flows by the total life.

    :param cash_flows: The cash flows.
    :param total_life: The total life.
    :return: The repeated cash flows.
    """
    if isinstance(cash_flows, Iterator):
        return repeated(tuple(cash_flows), total_life)
    else:
        return (cash_flow for cash_flow in link((cash_flows for _ in arange(0, total_life, life(cash_flows))))
                if cash_flow.time <= total_life)


def link(it: Iterable[Iterable[CashFlow]]) -> Iterator[CashFlow]:
    """Links the cash flows together, updating corresponding time periods.

    :param it: The cash flow sets to chain.
    :return: The chained cash flows.
    """
    total = list[CashFlow]()
    total_life = 0.0

    for cash_flows in map(tuple[CashFlow], it):
        total.extend(CashFlow(cash_flow.time + total_life, cash_flow.amount) for cash_flow in cash_flows)
        total_life += life(cash_flows)

    return iter(total)
