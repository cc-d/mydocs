#!/usr/bin/env python3
import re
import sys
from decimal import Decimal as D
from typing import List, Tuple

from myutils import *


def generate_prices(
    price: str, 
    incperc: D = D('0.25'),
    n: int = 100
) -> Tuple[List[str], D]:
    """
    Generates a list of prices based on a starting stock price, an increment percentage, and the number of prices to generate.
    
    Args:
    - price: The starting stock price, as a string.
    - incperc: The percentage increment to apply to each price. Default is 0.25
    - n: The number of prices to generate. Default is 10.
    
    Returns:
    - A tuple containing a list of formatted prices as strings and the price increment as a Decimal.
    """
    price, incperc = CD(price), D(str(incperc))
    start_price = D(str(price))

    increment = CD(price * incperc / 100)
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

    title = f'${start_price} | ${increment} {incperc}% | ${inc1percent} 1.00%' 

    reg = r'\$(\d+?\.\d+)\s+(-?\d+?\.?\d+)%'

    for si in range(len(prices)):
        s = prices[si]
        sdiff = (maxlen - len(s)) + 1
        pri, per = re.match(reg, s).groups()
        sp = (maxlen - (len(s) - 2)) * ' '

        prices[si] = f'{pri}{sp}{per}%'

    return [f'${x}' for x in list(
        reversed(
            sorted(
                prices, 
                key=lambda x: Decimal(x.split(' ')[0]))
        )
    )], title


def main():
    funcargs = []
    for i in range(len(sys.argv)):
        if i == 1:
            funcargs.append(D(sys.argv[i]))
        elif i == 2:
            funcargs.append(D(sys.argv[i]))
        elif i == 3:
            funcargs.append(int(sys.argv[i]))
    
    prices, title = generate_prices(*(x for x in funcargs))
    boxprint(prices, title=title)


if __name__ == '__main__':
    main()
