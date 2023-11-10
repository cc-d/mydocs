#!/usr/bin/env python3
import re
import sys
from decimal import Decimal as D
from typing import List, Tuple

from utils import boxprint, CD, D, Decimal


class _DEFAULT:
    price = D('100')
    incperc = D('0.25')
    n = 100


def generate_prices(
    price: str, incperc: D = D('0.25'), n: int = 100
) -> Tuple[List[str], D]:
    """Generates a list of prices and their percent change from the original
    price.
    Args:
        price: The original price.
        incperc: The percent change of each price.
        n: The number of prices to generate.
    Returns:
        A tuple containing a list of prices and the title of the box.
    """
    price, incperc = CD(price), D(str(incperc))
    start_price = D(str(price))

    increment = CD(price * (incperc / 100))
    half_n = n // 2
    prices = []

    inc1percent = CD(price * D('0.01'))
    price0 = f"${price} 0.00%"
    prices.append(price0)

    maxlen = len(price0)

    for i in range(-half_n, half_n + 1):
        if n % 2 == 0 and i == 0:
            continue
        curinc = i * increment
        new_price = price + curinc

        formatted_price = f"${new_price} {curinc}%"

        prices.append(formatted_price)

        if len(formatted_price) > maxlen:
            maxlen = len(formatted_price)

    title = f'${start_price} | ${increment} {incperc * 100}%'

    reg = r'\$(\d+?\.\d+)\s+(-?\d+?\.?\d+)%'

    for si in range(len(prices)):
        s = prices[si]
        sdiff = (maxlen - len(s)) + 1
        pri, per = re.match(reg, s).groups()
        sp = (maxlen - (len(s) - 2)) * ' '

        prices[si] = f'{pri}{sp}{per}%'

    return [
        f'${x}'
        for x in list(
            reversed(sorted(prices, key=lambda x: Decimal(x.split(' ')[0])))
        )
    ], title


def help():
    print('Usage: increments.py [price] [increment] [n]')
    sys.exit(0)


def main():
    price, incperc, n = _DEFAULT.price, _DEFAULT.incperc, _DEFAULT.n
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        if i == 1:
            if sys.argv[1].lower()[0] in ['h', '-']:
                help()
            price = sys.argv[1]
        if i == 2:
            incperc = sys.argv[2]
        if i == 3:
            n = int(sys.argv[3])

    if isinstance(incperc, str) and incperc.find('%') != -1:
        incperc = incperc[:-1]
        incperc = D(str(incperc)) / D('100')

    prices, title = generate_prices(price, incperc, n)
    boxprint(prices, title=title)


if __name__ == '__main__':
    main()
