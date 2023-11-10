#!/usr/bin/env python3
import sys
from typing import List, Tuple

from utils import boxprint, CD, D, Decimal


def strtuple(dp, dpr, pc):
    if pc < 0:
        sp = '-'
        spc = sp + str(D(str(pc * 100)[1:]).quantize(D('0.01')))
    else:
        sp = ' '
        spc = sp + str(D(str(pc * 100)).quantize(D('0.01')))

    return f'${dp} {dpr} {spc}%'


def stock_pe(
    price: Decimal, eps: Decimal, n: int
) -> List[Tuple[Decimal, Decimal, Decimal]]:
    annual_eps = eps * D('4')
    pe_ratio = D(price / annual_eps)
    pe_ratio = Decimal(str(pe_ratio)).quantize(Decimal('0.0001'))
    result: List[Tuple[Decimal, Decimal, Decimal]] = []
    percent_step = D('0.0025')

    longest = 0
    title = 'PE'

    for i in range(0, n + 1):
        # Calculate percent change
        percent_change = D(i * percent_step)

        # Calculate the adjusted stock price for increase and decrease
        increased_price = CD(price * (1 + percent_change))
        decreased_price = CD(price * (1 - percent_change))

        # Calculate the PE ratios for increased and decreased stock prices
        increased_pe_ratio = CD(increased_price / annual_eps)
        decreased_pe_ratio = CD(decreased_price / annual_eps)

        # Add the tuples to the result list
        result.append((increased_price, increased_pe_ratio, percent_change))

        if percent_change != D(0):
            result.append(
                (decreased_price, decreased_pe_ratio, D('-1') * percent_change)
            )
        else:
            title = f'${price} {pe_ratio}'

    return list(reversed(sorted(result))), title


if __name__ == '__main__':
    n = 50
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        if i == 1:
            price = CD(sys.argv[1])
        if i == 2:
            eps = CD(sys.argv[2])
        if i == 3:
            n = int(sys.argv[3])

    pes, title = stock_pe(price, eps, n)

    pes = [strtuple(*(x)) for x in pes]

    boxprint(pes, title=title)
