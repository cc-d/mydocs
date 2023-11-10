#!/usr/bin/env python3
import re
import sys
import shutil
from decimal import Decimal, ROUND_HALF_UP


# Utility functions
def D(num) -> Decimal:
    return Decimal(str(num))


def CD(num) -> Decimal:
    return D(str(num)).quantize(D('0.01'), rounding=ROUND_HALF_UP)


def boxprint(strings: list, title: str = None) -> None:
    terminal_width, _ = shutil.get_terminal_size()
    max_length = max(
        *(len(s) for s in strings), len(title) - (len(title) // 3)
    )
    num_columns = max(1, terminal_width // (max_length + 4))
    column_width = (terminal_width - num_columns - 1) // num_columns
    num_rows = -(-len(strings) // num_columns)
    horizontal_border = (
        '+' + '-' * (column_width * num_columns + num_columns - 1) + '+'
    )
    empty_row = (
        '|' + ' ' * (column_width * num_columns + num_columns - 1) + '|'
    )

    if title:
        title_line = (
            '| '
            + title.center(column_width * num_columns + num_columns - 2)
            + '|'
        )
        print(horizontal_border)
        print(title_line)
    print(horizontal_border)

    for i in range(num_rows):
        row_strings = strings[i::num_rows]
        row_strings.extend([''] * (num_columns - len(row_strings)))
        columns = [s.ljust(column_width - 2) for s in row_strings]
        print('| ' + ' | '.join(columns) + ' |')

    print(empty_row)
    print(horizontal_border)
