def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    else:
        return x


def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)
