from collections.abc import Callable
from itertools import chain
from math import ceil, exp, inf, log
from unittest import TestCase, main

from math2.analysis import interpolate
from math2.calc import integrate, root
from math2.consts import EPS
from math2.econ import (Bond, CashFlow, CompInt, ContInt, DblDeclBalDeprec, DeclBalDeprec, EfInt, Mortgage, NomInt,
                        Project, Rel, SPInt, SYDDeprec, SimpleInt, StrLineDeprec, UPDeprec, aw, beta, capm,
                        de_facto_marr, fair, fp, irr, irr_table, link, pa, payback, perp, pf, pg, pw, rel,
                        rel_combinations, repeated, ror, rpw, select, yield_)
from math2.tests import ExtendedTestCase


class InterestTestCase(TestCase):
    def test_difference(self) -> None:
        r, p, t, s, c = 0.07, 24, 2020 - 1626, 685.92, 9066082143624.828

        self.assertAlmostEqual(p * SimpleInt(r).to_factor(t), s)
        self.assertAlmostEqual(p * EfInt(r).to_factor(t), c)

    def test_comparison(self) -> None:
        self.assertLess(NomInt(0.06, 12).to_ef().rate, SPInt(0.063, 1).to_ef().rate)

    def test_consistency(self) -> None:
        nr, sc, t, f = 0.1, 4, 2.5, 1.2800845441963565
        counts = range(1, 366)

        interests = (
            EfInt((1 + nr / sc) ** sc - 1),
            ContInt(log((1 + nr / sc) ** sc)),
            NomInt(nr, sc),
            SPInt(nr / sc, sc),
        )

        for interest in interests:
            self.assertAlmostEqual(interest.to_factor(t), f)
            self.assertAlmostEqual(interest.to_ef().to_factor(t), f)
            self.assertAlmostEqual(interest.to_cont().to_factor(t), f)

            for count in counts:
                self.assertAlmostEqual(interest.to_nom(count).to_factor(t), f)
                self.assertAlmostEqual(interest.to_sp(count).to_factor(t), f)

        self.assertAlmostEqual(NomInt(nr, sc).to_nom().to_factor(t), f)
        self.assertAlmostEqual(NomInt(nr, sc).to_sp().to_factor(t), f)
        self.assertAlmostEqual(SPInt(nr / sc, sc).to_nom().to_factor(t), f)
        self.assertAlmostEqual(SPInt(nr / sc, sc).to_sp().to_factor(t), f)


class InstrumentTestCase(ExtendedTestCase):
    def test_relationships(self) -> None:
        self.assertEqual(rel((5000, 7000, 6000, 3000), 1000000), Rel.INDEP)
        self.assertEqual(rel((5000, 7000, 6000, 3000), 7000), Rel.MEX)
        self.assertEqual(rel((5000, 7000, 6000, 3000), 10000), Rel.REL)

    def test_combinations(self) -> None:
        self.assertEqual(len(tuple(rel_combinations((5000, 7000, 6000, 3000), 10000))), 8)

    def test_projects(self) -> None:
        self.assertAlmostEqual(pw(Project(-20000, 4000 - 1000, 4000, 10).cash_flows, EfInt(0.05)), 5620.857801717468)
        self.assertAlmostEqual(aw(Project(-20000, 4000 - 1000, 4000, 10).cash_flows, EfInt(0.05)), 727.9268005526942)


class CashFlowTestCase(TestCase):
    def test_payback_period(self) -> None:
        self.assertAlmostEqual(payback((), 0), 0)
        self.assertAlmostEqual(payback((), 10), inf)
        self.assertAlmostEqual(payback((CashFlow(0, 100), CashFlow(1, 200), CashFlow(2, 300)), 450), 1.5)


class PS1TestCase(TestCase):
    def test_1(self) -> None:
        self.assertLess(8000 + 1200, 6800 + 2500)
        self.assertAlmostEqual(root(lambda mv: 8000 + 1200 - (mv + 2500), 6800, EPS), 6700)

    def test_2(self) -> None:
        self.assertAlmostEqual(root(lambda t: 7500 - t * 1700, 0, EPS), 4.411764705882353)
        self.assertAlmostEqual(root(lambda t: 9000 - t * 2200, 0, EPS), 4.09090909)

    def test_3(self) -> None:
        self.assertAlmostEqual((1 + 0.05 / 1000000) ** 1000000, exp(0.05))

    def test_4(self) -> None:
        e, p, t = EfInt(0.034), 100000, 4

        self.assertAlmostEqual(e.to_nom(2).rate, 0.03371581102178567)
        self.assertAlmostEqual(e.to_nom(12).rate, 0.033481397886386155)
        self.assertAlmostEqual(e.to_nom(365).rate, 0.03343630748129267)
        self.assertAlmostEqual(e.to_cont().rate, 0.03343477608623742)

        self.assertAlmostEqual(p * e.to_nom(2).to_factor(t), p * e.to_nom(12).to_factor(t))
        self.assertAlmostEqual(p * e.to_nom(12).to_factor(t), p * e.to_nom(365).to_factor(t))
        self.assertAlmostEqual(p * e.to_nom(365).to_factor(t), p * e.to_cont().to_factor(t))
        self.assertAlmostEqual(p * e.to_cont().to_factor(t), 114309.4552336)

    def test_5(self) -> None:
        fv, c, cd = 100, 0.023, 0.02

        self.assertAlmostEqual(ContInt(c).to_ef().rate, 0.02326653954721758)
        self.assertAlmostEqual(fv / ContInt(c).to_factor(0.5), 98.8565872247913)
        self.assertAlmostEqual(fv / ContInt(c).to_factor(0.75), 98.28979294344309)
        self.assertAlmostEqual(fv / ContInt(cd).to_factor(0.5), 99.0049833749168)
        self.assertAlmostEqual(fv / ContInt(cd).to_factor(0.75), 98.51119396030627)

    def test_6(self) -> None:
        self.assertAlmostEqual(EfInt(0.08).to_sp(12).rate, 0.00643403011000343)
        self.assertAlmostEqual(NomInt(0.035, 252).to_ef().rate, 0.03561719190449408)
        self.assertAlmostEqual(NomInt(0.04, 4).to_cont().rate, 0.039801323412672354)
        self.assertAlmostEqual(CompInt.from_factor(SPInt(0.015, 12).to_factor(), 4).to_cont().rate,
                               0.04466583748125169)
        self.assertAlmostEqual(CompInt.from_factor(CompInt.from_factor(
            NomInt(0.012, 3).to_factor(), 1 / 4).to_factor(3)).to_nom(6).rate, 0.1454477030768886)


class PS2TestCase(ExtendedTestCase):
    def test_1(self) -> None:
        factor = NomInt(0.15, 4).to_factor(4 / 12) * ContInt(0.11).to_factor(5 / 12)

        self.assertAlmostEqual(CompInt.from_factor(factor, 9 / 12).rate, 0.134915472328168)

    def test_2(self) -> None:
        p, i, n = 100, 0.05, 10

        self.assertAlmostEqual(p * pa(i, n), p * ((1 + i) ** n - 1) / (i * (1 + i) ** n))

    def test_3(self) -> None:
        cases = (
            (1, 99.52, 0.05943811, 0.05773868),
            (4, 99.01, 0.03029791, 0.02984799),
            (8, 97.64, 0.03647384, 0.03582441),
            (12, 95.85, 0.04329682, 0.04238572),
        )

        for m, p, a, b in cases:
            self.assertAlmostEqual(root(lambda y: p * EfInt(y).to_factor(m / 12) - 100, 0, EPS), a)
            self.assertAlmostEqual(root(lambda y: p * ContInt(y).to_factor(m / 12) - 100, 0, EPS), b)

        self.assertAlmostEqual(interpolate(7, (4, 8), (0.03029791, 0.03647384)), 0.0349298575)
        self.assertAlmostEqual(interpolate(7, (4, 8), (0.02984799, 0.03582441)), 0.034330305)

        self.assertAlmostEqual(root(lambda y: 1.03029791 ** (4. / 12) * (1 + y) ** (8. / 12) - 1.04329682, 0, EPS),
                               0.04985765)

    def test_4(self) -> None:
        data = {
            2: 99.11,
            6: 98.72,
            9: 96.85,
            12: 95.97,
        }

        r: dict[float, float] = {
            t: root(lambda y: p * ContInt(y).to_factor(t / 12) - 100, 0, EPS)
            for t, p in data.items()
        }

        r[4] = interpolate(4, (2, 6), (r[2], r[6]))
        r[5.5] = interpolate(5.5, (2, 6), (r[2], r[6]))
        r[7] = interpolate(7, (6, 9), (r[6], r[9]))
        r[10] = interpolate(10, (9, 12), (r[9], r[12]))

        self.assertAlmostEqual(100 * ContInt(r[2]).to_factor(-1. / 12), 99.55400544428134)
        self.assertAlmostEqual(100 * ContInt(r[4]).to_factor(-4. / 12), 98.68531340424114)
        self.assertAlmostEqual(100 * ContInt(r[5.5]).to_factor(-5.5 / 12), 98.66834503291024)
        self.assertAlmostEqual(100 * ContInt(r[7]).to_factor(-7 / 12), 98.18488742486127)
        self.assertAlmostEqual(100 * ContInt(r[10]).to_factor(-10 / 12), 96.54750684004732)
        self.assertAlmostEqual(2000 * pf(r[2], 1. / 12) + 500 * pf(r[4], 4. / 12) - 1200 * pf(r[7], 7. / 12) - 1000
                               * pf(r[10], 10. / 12) + 500 * pf(r[12], 1), 820.3872407904064)

    def test_5(self) -> None:
        i = 0.02
        options = (
            15500 * pa(i, 10),
            140000,
            155000 * pf(i, 5),
            170000 * pf(i, 10),
        )

        self.assertIterableAlmostEqual(options, (139230.06759675476, 140000, 140388.27552363696, 139459.21097877636))
        self.assertEqual(max(range(4), key=options.__getitem__), 2)

    def test_6(self) -> None:
        i = 0.02
        options = (
            155000 * pf(i, 5),
            10000 * pa(i, 10) + 1500 * pg(i, 10),
        )

        self.assertAlmostEqual(options[1], 148258.50062422457)
        self.assertEqual(max(range(2), key=options.__getitem__), 1)

    def test_7(self) -> None:
        i = 0.02
        option = 10000 * pa(i, 10, g=0.05)

        self.assertAlmostEqual(option, 112086.97925088322)


class PS3TestCase(TestCase):
    def test_1(self) -> None:
        mortgage = Mortgage.from_dtv(2995000, 0.2, NomInt(0.02, 2))

        self.assertAlmostEqual(mortgage.payment, 10145.891129693951)
        self.assertAlmostEqual(mortgage.payment * 12 * 3, 365252.08066898223)

        mortgage = mortgage.pay()
        mortgage.int = NomInt(0.04, 2)

        self.assertAlmostEqual(mortgage.payment, 12128.043601452593)

    def test_2(self) -> None:
        i = NomInt(0.07, 2)

        self.assertAlmostEqual(pw(Bond(100, 0, 2, 3 / 12).cash_flows, i), 98.2946374365981)
        self.assertAlmostEqual(pw(Bond(100, 0, 2, 5 / 12).cash_flows, i), 97.17391685967232)
        self.assertAlmostEqual(pw(Bond(100, 0, 2, 3).cash_flows, i), 81.35006443077528)
        self.assertAlmostEqual(pw(Bond.from_rate(100, NomInt(0.04, 2), 2, 3).cash_flows, i), 92.00717047033226)
        self.assertAlmostEqual(pw(Bond.from_rate(100, NomInt(0.06, 2), 2, 3.25).cash_flows, i), 95.94840994600501)

    def test_3(self) -> None:
        self.assertAlmostEqual(yield_(Bond.from_rate(100, NomInt(0.07, 2), 2, 3).cash_flows, 100, EfInt(0), EPS)
                               .to_nom(2).rate, 0.07)
        self.assertAlmostEqual(pw(Bond.from_rate(
            100, NomInt(0.04, 2), 2, 3).cash_flows, NomInt(0.05, 2)) + 100 * 0.04 / 2, 99.24593731921009)
        self.assertAlmostEqual(yield_(Bond.from_rate(100, NomInt(0.03, 2), 2, 2.25).cash_flows, 100, EfInt(0), EPS)
                               .to_nom(2).rate, 0.026754568040623247)
        self.assertAlmostEqual(pw(Bond.from_rate(100, NomInt(0.07, 2), 2, 2.25).cash_flows, NomInt(0.05, 2)),
                               102.65033622528411)
        self.assertAlmostEqual(root(
            lambda c: pw(Bond.from_rate(100, NomInt(c, 2), 2, 2.25).cash_flows, NomInt(0.03, 2)) - 114, 0.1, EPS,
        ), 0.10627047075771787)

    def test_4(self) -> None:
        i, n = 0.1, 10
        a, g = 100, 10
        r, gp = log(1 + i), log(1 + g)
        a0 = a * pa(i, g, n) * (gp - r) / (exp(n * (gp - r)) - 1)

        self.assertAlmostEqual(a * pa(i, n, g) / integrate(lambda t: a0 * exp((gp - r) * t), 0, n, 10000), 1, 2)

    def test_5(self) -> None:
        y = root(lambda y_: pw(Bond.from_rate(
            100, NomInt(0.07, 2), 2, 7.5).cash_flows, NomInt(y_, 2)) * fp(y_ / 2, 0.5) - 108, 0.1, EPS)
        b: Callable[[float], float] = lambda cr: pw(Bond.from_rate(1000, NomInt(cr, 2), 2, 9).cash_flows, NomInt(y, 2))

        cur_cr = ceil(root(lambda cr: 9500000 / 2 - (4400 * b(cr)), 0.1, EPS) / 0.0025) * 0.0025
        self.assertAlmostEqual(cur_cr, 0.0725)
        self.assertAlmostEqual(4400 * b(cur_cr), 4802235.185695931)

        cur_cr = ceil(root(lambda cr: 9500000 / 2 / (1 - 0.008) - (4400 * b(cr)), 0.1, EPS) / 0.0025) * 0.0025
        self.assertAlmostEqual(cur_cr, 0.0725)
        self.assertAlmostEqual(4400 * b(cur_cr) * (1 - 0.008), 4763817.304210364)

    def test_6(self) -> None:
        i = NomInt(0.060755, 2)

        self.assertAlmostEqual(Mortgage.from_down(500000, 50000, i).payment, 2899.3558026129626)
        self.assertAlmostEqual(Mortgage.from_down(500000, 50000, i).pay(3, 700).payment, 3490.3113416458878)
        self.assertLess(Mortgage.from_down(500000, 50000, i).pay(3).principal,
                        Mortgage.from_down(500000, 50000, i).pay(3, 700).principal)


class PS4TestCase(ExtendedTestCase):
    def test_1(self) -> None:
        fx = root(lambda x: ContInt(0.015).to_factor() - 0.77 * ContInt(0.02).to_factor() / x, 1, EPS)

        self.assertAlmostEqual(fx, 0.7738596388734157)

    def test_2(self) -> None:
        p, t, r = 42, 3, capm(0.86, EfInt(0.015), EfInt(0.08))

        self.assertAlmostEqual(r.rate, 0.0709)
        self.assertAlmostEqual(p * r.to_factor(t), 51.581746894818)

    def test_3(self) -> None:
        self.assertAlmostEqual(2 * perp(capm(1.2, EfInt(0.012), EfInt(0.07)).rate), 24.509803921568626)

    def test_4(self) -> None:
        r = capm(0.8, EfInt(0.017), EfInt(0.07))
        self.assertAlmostEqual(41 * r.to_factor(2.5) * EfInt(-0.03).to_factor(2), 44.56329005026732)

    def test_5(self) -> None:
        rf, p_bull = EfInt(0.022), 0.6
        a_bull, a_bear = 102, 77
        m_price, m_bull, m_bear = 105, 127, 90
        ap = fair(102, 77, m_price, m_bull, m_bear, rf)
        ar, mr = ror(ap, a_bull, a_bear, p_bull), ror(m_price, m_bull, m_bear, p_bull)
        b = beta(ar, mr, rf)

        self.assertAlmostEqual(ap, 86.78663986883166)
        self.assertAlmostEqual(ar.rate, 0.060070998704959244)
        self.assertAlmostEqual(mr.rate, 0.0685714285714285)
        self.assertAlmostEqual(b, 0.8174754323150769)

    def test_6(self) -> None:
        bb = ((90, 102, 66), (85, 115, 77), (150, 200, 132))
        m_price, m_bull, m_bear = 18, 22, 16
        p = 0.6
        rf = EfInt(0.03)
        fps = tuple(fair(bb[i][1], bb[i][2], m_price, m_bull, m_bear, rf) for i in range(3))

        self.assertIterableEqual((i for i, fp_ in enumerate(fps) if fp_ > bb[i][0]), (1, 2))
        self.assertAlmostEqual(fps[1] + fps[2] - bb[1][0] - bb[2][0], 11.47896440129449)
        self.assertAlmostEqual(fps[1] + fps[2], 246.4789644012945)

        a_ror = ror(fps[1] + fps[2], bb[1][1] + bb[2][1], bb[1][2] + bb[2][2], p)
        m_ror = ror(m_price, m_bull, m_bear, p)

        self.assertAlmostEqual(beta(a_ror, m_ror, rf), 1.2901709513930817)

    def test_7(self) -> None:
        self.assertAlmostEqual(root(
            lambda y: ContInt(0.043).to_factor(3) * ContInt(y).to_factor(5) - ContInt(0.0582).to_factor(8), 0, EPS,
        ), 0.06732)

    def test_8(self) -> None:
        bond = Bond.from_rate(100, EfInt(0.05), 1, 5)
        default = 0.02
        rf = EfInt(0.03)
        good, bad = 5 + bond.face, bond.face * 0.4

        for i in range(5):
            good = 5 + ((1 - default) * good + default * bad) / rf.to_factor()

        good -= 5

        self.assertAlmostEqual(good, 103.08377972409899)
        self.assertAlmostEqual(yield_(bond.cash_flows, good, EfInt(0), EPS).rate, 0.04301423365637252)


class PS5TestCase(ExtendedTestCase):
    def test_1(self) -> None:
        i, n = 0.05, 6
        y = pw(Project(-700, 370, 0, n).cash_flows, EfInt(i))

        self.assertAlmostEqual(y, 1178.006064888955)
        self.assertAlmostEqual(y * fp(i, n), 1578.6407921875)
        self.assertAlmostEqual(y * fp(i, 4), 1431.8737344104306)
        self.assertAlmostEqual(root(lambda x: y - x * pf(i, 1) - 5 * x * pf(i, 3), 0, EPS), 223.464034554222)

        i, n = 0.09, 6
        y = pw(Project(-700, 370, 0, n).cash_flows, EfInt(i))

        self.assertAlmostEqual(y, 959.7898783854448)
        self.assertAlmostEqual(y * fp(i, n), 1609.6637114243001)
        self.assertAlmostEqual(y * fp(i, 4), 1354.821741793031)
        self.assertAlmostEqual(root(lambda x: y - x * pf(i, 1) - 5 * x * pf(i, 3), 0, EPS), 200.862256010023)

    def test_2(self) -> None:
        cr = tuple(Project(300000, 14000, 0, 20).cash_flows)
        ed = tuple(Project(220000, 21000, 0, 20).cash_flows) + (CashFlow(8, 35000), CashFlow(16, 35000))
        i = EfInt(0.05)

        self.assertAlmostEqual(pw(cr, i), 474470.94479555974)
        self.assertAlmostEqual(pw(ed, i), 521429.6981340426)
        self.assertAlmostEqual(aw(cr, i), 38072.77615720737)
        self.assertAlmostEqual(aw(ed, i), 41840.86801633675)

        self.assertLess(pw(cr, i), pw(ed, i))
        self.assertLess(aw(cr, i), aw(ed, i))

    def test_3(self) -> None:
        i = EfInt(0.05)

        aw_cr = aw(Project(300000, 14000, 0, 20).cash_flows, i)
        aw_ed = aw(Project(220000, 21000, 0, 20).cash_flows, i) + aw((CashFlow(8, 35000),), i)

        self.assertAlmostEqual(aw_cr, 38072.77615720737)
        self.assertAlmostEqual(aw_ed, 42318.6326589209)

    def test_4(self) -> None:
        a, b = Project(425, 48, 0, 3), Project(450, 45, 0, 4)
        i = EfInt(0.1)

        self.assertAlmostEqual(rpw(a.cash_flows, i, 5), 926.2665553147758)
        self.assertAlmostEqual(rpw(link((a.cash_flows, b.cash_flows)), i, 5), 941.1376210020427)
        self.assertAlmostEqual(rpw(b.cash_flows, i, 5), 927.9414595376618)
        self.assertAlmostEqual(rpw(link((b.cash_flows, a.cash_flows)), i, 5), 912.7288871227124)

    def test_5(self) -> None:
        i = EfInt(0.07)
        sa = aw(chain((CashFlow(0, 5e6),), repeated(Project(0, 2e5, 1e6, 6).cash_flows, 25)), i, 25)
        sb = aw(chain((CashFlow(0, 6e6),), repeated(Project(0, 1.5e5, 1.1e6, 11).cash_flows, 25)), i, 25)
        ba = aw(chain((CashFlow(0, 5e6),), repeated(Project(0, 5e5 - 3e5, 1e6, 14).cash_flows, 25)), i, 25)
        bb = aw(chain((CashFlow(0, 3e6),), repeated(Project(0, 3e5, 6e5, 5).cash_flows, 25)), i, 25)

        self.assertAlmostEqual(sa, 766638.1419621999)
        self.assertAlmostEqual(sb, 731013.277560719)
        self.assertAlmostEqual(ba, 662331.3841421161)
        self.assertAlmostEqual(bb, 661765.9683268208)

        self.assertAlmostEqual(min(sa + ba, sa + bb, sb + ba, sb + bb), sb + bb)

    def test_6(self) -> None:
        i = EfInt(0.06)
        mortgage = Mortgage(580000, i, 1)

        self.assertAlmostEqual(1 - mortgage.pay(2).principal * i.rate / mortgage.payment, 0.26179726123417735)
        self.assertAlmostEqual(1 - mortgage.pay(9).principal * i.rate / mortgage.payment, 0.39364628371277466)

    def test_7(self) -> None:
        s, t, i, n, g = 57000, 1000000, 0.065, 35, 0.035
        sq = s / 4 * (fp(i, 0) + fp(i, 3 / 12) + fp(i, 6 / 12) + fp(i, 9 / 12))

        self.assertAlmostEqual(root(lambda x: x * s * pa(i, n, g) - t * pf(i, n), 0, EPS), 0.09187408282061407)
        self.assertAlmostEqual(root(lambda x: x * sq * pa(i, n, g) - t * pf(i, n), 0, EPS), 0.08971594525258755)

    def test_8(self) -> None:
        project, i = Project(1000, 500, 300, 10), EfInt(0.6)

        x, y = project.cash_flows, link((project.cash_flows, project.cash_flows))

        self.assertAlmostEqual(aw(x, i), aw(y, i))


class PS6TestCase(ExtendedTestCase):
    def test_1(self) -> None:
        projects = (
            Project(-41000, 6100, 0, 7),
            Project(-32000, 6700, 0, 7),
            Project(-28000, 5700, 0, 5),
            Project(-28000, 12600, 0, 5),
            Project(-36000, 9000, 0, 7),
            Project(-27000, 10600, 0, 6),
            Project(-53000, 6700, 0, 5),
            Project(-50000, 15000, 0, 6),
            Project(-32000, 6900, 0, 7),
            Project(-42000, 14600, 0, 5),
        )

        irrs = tuple(irr(project.cash_flows, EfInt(0), EPS) for project in projects)

        self.assertIterableAlmostEqual((irr_.to_ef().rate for irr_ in irrs), (
            0.010261108929599895,
            0.10584583010815002,
            0.005929015028005828,
            0.3494328573992243,
            0.16326709023510008,
            0.31754169406374866,
            -0.13571830650187303,
            0.1990541470961173,
            0.114956469240095,
            0.2178733729868983,
        ))

        self.assertAlmostEqual(de_facto_marr(projects, 100000, EfInt(0), EPS).to_ef().rate, 0.2178733729868983)

    def test_2(self) -> None:
        self.assertEqual(select(map(EfInt, (0.17, 0.14, 0.19, 0.2, 0.18, 0.13)), map(lambda row: map(EfInt, row), (
            (),
            (0.075,),
            (0.209, 0.286),
            (0.127, 0.257, 0.229),
            (0.177, 0.192, 0.158, 0.117),
            (0.128, 0.132, 0.106, 0.081, 0.062),
        )), EfInt(0.12)), 3)
        self.assertEqual(select(map(EfInt, (0.14, 0.20, 0.24, 0.21, 0.17, 0.17,)), map(lambda row: map(EfInt, row), (
            (),
            (0.29,),
            (0.32, 0.36),
            (0.24, 0.22, 0.11),
            (0.18, 0.15, 0.08, 0.06),
            (0.18, 0.16, 0.12, 0.13, 0.19),
        )), EfInt(0.12)), 2)

    def test_3(self) -> None:
        irrs = tuple(map(EfInt, (0.1096, 0.132, 0.1205, 0.1293, 0.1286, 0.1113)))
        table = tuple(map(lambda row: tuple(map(EfInt, row)), (
            (),
            (0.286,),
            (0.17, -0.058),
            (0.189, 0.112, 0.228),
            (0.177, 0.112, 0.187, 0.113),
            (0.113, 0.079, 0.094, 0.069, 0.063),
        )))

        self.assertEqual(select(irrs, table, EfInt(0.04)), 5)
        self.assertEqual(select(irrs, table, EfInt(0.06)), 5)
        self.assertEqual(select(irrs, table, EfInt(0.08)), 4)
        self.assertEqual(select(irrs, table, EfInt(0.10)), 4)
        self.assertEqual(select(irrs, table, EfInt(0.12)), 1)
        self.assertEqual(select(irrs, table, EfInt(0.14)), None)

    def test_4(self) -> None:
        marr = EfInt(0.12)
        projects = tuple(filter(lambda project: irr(project.cash_flows, EfInt(0), EPS) > marr, (
            Project(-80000, 13000, 10000, 10),
            Project(-120000, 23000, 34000, 10),
            Project(-145000, 24000, 25000, 10),
            Project(-145000, 28000, 29000, 10),
        )))
        irrs = (irr(project.cash_flows, EfInt(0), EPS) for project in projects)
        table = irr_table(projects, EfInt(0), EPS)

        self.assertEqual(select(irrs, table, marr), 1)

    def test_5(self) -> None:
        p = root(lambda x: (
                -5e8 + x * (2e8 * pa(0.08, 8) * pf(0.08, 4) + 1e7 / 0.08 * pf(0.08, 12))
                - x * (-5e8 * pf(0.08, 2) + 2e8 * pa(0.08, 6) * pf(0.08, 6) + 1e7 / 0.08 * pf(0.08, 12))
        ), 0, EPS)

        self.assertAlmostEqual(p, 0.7237775659969569)


class PS7TestCase(ExtendedTestCase):
    def test_1(self) -> None:
        basis, salvage, life = 92000, 19000, 4

        self.assertIterableAlmostEqual(StrLineDeprec(basis, salvage, life).books, (92000, 73750, 55500, 37250, 19000))
        self.assertIterableAlmostEqual(DeclBalDeprec(basis, salvage, life).books,
                                       (92000, 62019.64424847585, 41809.08992073374, 28184.618296048306, 19000))
        self.assertIterableAlmostEqual(DeclBalDeprec.from_rate(basis, life, EfInt(0.25)).books,
                                       (92000, 69000, 51750, 38812.5, 29109.375))
        self.assertIterableAlmostEqual(DblDeclBalDeprec(basis, salvage, life).books,
                                       (92000, 46000, 23000, 11500, 5750))
        self.assertIterableAlmostEqual(SYDDeprec(basis, salvage, life).books, (92000, 62800, 40900, 26300, 19000))
        self.assertIterableAlmostEqual(UPDeprec(basis, salvage, (37000, 37000, 32000, 30000)).books,
                                       (92000, 72139.70588235295, 52279.41176470589, 35102.94117647059, 19000))

    def test_2(self) -> None:
        basis, salvage, life, t = 210000, 10000, 20, 6

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).book(t), 150000)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).book(t), 84246.81795174461)
        self.assertAlmostEqual(DeclBalDeprec.from_rate(basis, life, EfInt(0.2)).book(t), 55050.24)
        self.assertAlmostEqual(DblDeclBalDeprec(basis, salvage, life).book(t), 111602.61)

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).amount(t), 10000)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).amount(t), 13852.157371177402)
        self.assertAlmostEqual(DeclBalDeprec.from_rate(basis, life, EfInt(0.2)).amount(t), 13762.56)
        self.assertAlmostEqual(DblDeclBalDeprec(basis, salvage, life).amount(t), 12400.29)

    def test_3(self) -> None:
        basis, life, t, book = 145000, 8, 6, 57000

        self.assertAlmostEqual(root(lambda x: StrLineDeprec(basis, x, life).book(6) - book, 0, EPS), 27666.66666666667)
        self.assertAlmostEqual(root(lambda x: DeclBalDeprec(basis, x, life).book(6) - book, 0, EPS), 41755.1908917986)

    def test_4(self) -> None:
        basis, salvage, life = 110000, 25000, 4

        self.assertIterableAlmostEqual(StrLineDeprec(basis, salvage, life).books, (110000, 88750, 67500, 46250, 25000))
        self.assertIterableAlmostEqual(DeclBalDeprec(basis, salvage, life).books,
                                       (110000, 75950.3039160202, 52440.44240850757, 36207.88671287913, 25000))
        self.assertIterableAlmostEqual(DeclBalDeprec.from_rate(basis, life, EfInt(0.35)).books,
                                       (110000, 71500, 46475, 30208.75, 19635.6875))
        self.assertIterableAlmostEqual(DblDeclBalDeprec(basis, salvage, life).books,
                                       (110000, 55000, 27500, 13750, 6875))
        self.assertIterableAlmostEqual(SYDDeprec(basis, salvage, life).books, (110000, 76000, 50500, 33500, 25000))
        self.assertIterableAlmostEqual(UPDeprec(basis, salvage, (80000, 65000, 50000, 35000)).books,
                                       (110000, 80434.78260869565, 56413.043478260865, 37934.78260869565, 25000))

    def test_5(self) -> None:
        basis, salvage, life, t1, t2 = 23000, 4000, 7, 4, 5

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).book(t1), 12142.857142857143)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).book(t1), 8465.096723059049)
        self.assertAlmostEqual(SYDDeprec(basis, salvage, life).book(t1), 8071.4285714285725)
        self.assertAlmostEqual(UPDeprec(basis, salvage, (50, 60, 40, 20, 10, 15, 5)).book(t1), 6850)

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).amount(t2), 2714.285714285714)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).amount(t2), 1871.7191438152927)
        self.assertAlmostEqual(SYDDeprec(basis, salvage, life).amount(t2), 2035.7142857142856)
        self.assertAlmostEqual(UPDeprec(basis, salvage, (50, 60, 40, 20, 10, 15, 5)).amount(t2), 950)

    def test_6(self) -> None:
        basis, salvage, life, t = 2500000, 200000, 10, 4

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).book(t), 1580000)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).book(t), 910282.1015130404)
        self.assertAlmostEqual(DblDeclBalDeprec(basis, salvage, life).book(t), 1024000)
        self.assertAlmostEqual(SYDDeprec(basis, salvage, life).book(t), 1078181.8181818182)

        self.assertAlmostEqual(StrLineDeprec(basis, salvage, life).amount(t), 230000)
        self.assertAlmostEqual(DeclBalDeprec(basis, salvage, life).amount(t), 261554.3542830096)
        self.assertAlmostEqual(DblDeclBalDeprec(basis, salvage, life).amount(t), 256000)
        self.assertAlmostEqual(SYDDeprec(basis, salvage, life).amount(t), 292727.2727272727)

    def test_7(self) -> None:
        deprec = DeclBalDeprec.from_rate(5000, 5, EfInt(0.15))

        self.assertAlmostEqual(deprec.cap_gain(3000), 0)
        self.assertAlmostEqual(deprec.recap_deprec(3000), 781.4734375)
        self.assertAlmostEqual(deprec.loss_on_disp(3000), 0)

        self.assertAlmostEqual(deprec.cap_gain(2000), 0)
        self.assertAlmostEqual(deprec.recap_deprec(2000), 0)
        self.assertAlmostEqual(deprec.loss_on_disp(2000), 218.5265625)

        self.assertAlmostEqual(deprec.cap_gain(6000), 1000)
        self.assertAlmostEqual(deprec.recap_deprec(6000), 2781.4734375)
        self.assertAlmostEqual(deprec.loss_on_disp(6000), 0)


if __name__ == '__main__':
    main()
