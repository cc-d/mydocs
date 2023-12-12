from decimal import Decimal as D


def CD(n):
    return D(str(n)).quantize(D('0.01'))


def py(start: D, years: int, rate: D) -> list[tuple[D, int]]:
    """Calculate the balance of a savings account over a number of years.

    :param start: The starting balance.
    :param years: The number of years to calculate.
    :param rate: The interest rate.
    :return: A list of tuples containing the year and balance.
    """
    balance = CD(start)
    rate = CD(rate)
    result = []
    for year in range(1, years + 1):
        diff = CD(balance * rate)
        balance = balance + diff
        perday = CD(diff / D(365))
        result.append((balance, year, balance - start, diff, perday))

    return result


print(
    '\t'.join(
        str(x).ljust(10)
        for x in ('Balance', 'Year', 'Gain', 'Diff', 'Per Day')
    )
)
for t in py(30000, 10, 0.05):
    st = '\t'.join(str(x).ljust(10) for x in t)
    print(st)
