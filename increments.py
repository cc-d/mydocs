#!/usr/bin/env python3
import sys
from decimal import Decimal as D
from typing import List, Tuple

from myutils import *


def generate_prices(
    stock_price: str, 
    increment_percent: D = D('0.25'),
    n: int = 100
) -> Tuple[List[str], D]:
    """
    Generates a list of prices based on a starting stock price, an increment percentage, and the number of prices to generate.
    
    Args:
    - stock_price: The starting stock price, as a string.
    - increment_percent: The percentage increment to apply to each price. Default is 0.25
    - n: The number of prices to generate. Default is 10.
    
    Returns:
    - A tuple containing a list of formatted prices as strings and the price increment as a Decimal.
    """
    stock_price, increment_percent = D(str(stock_price)), D(str(increment_percent))
    start_price = D(str(stock_price))

    increment = CD(stock_price * increment_percent / 100)
    half_n = n // 2
    prices = []

    for i in range(-half_n, half_n + 1):
        if n % 2 == 0 and i == 0:
            continue
        curinc = i * increment
        new_price = stock_price + curinc

        formatted_price = f"${new_price} {curinc}%"
        prices.append(formatted_price)

    return list(
        reversed(
            sorted(
                prices, 
                key=lambda x: D(str(x.split(' ')[0])[1:])))
    ), increment


def main():
    funcargs = []
    for i in range(len(sys.argv)):
        if i == 1:
            funcargs.append(D(sys.argv[i]))
        elif i == 2:
            funcargs.append(D(sys.argv[i]))
        elif i == 3:
            funcargs.append(int(sys.argv[i]))
    
    prices, inc = generate_prices(*(x for x in funcargs))
    boxprint(prices, title=f'${inc}')


if __name__ == '__main__':
    main()
