#!/usr/bin/env python3
import shutil
from decimal import ROUND_HALF_UP, Decimal
from typing import List, Optional


def D(num) -> Decimal:
    return Decimal(str(num))


def CD(num) -> Decimal:
    return D(str(num)).quantize(D(0.01), rounding=ROUND_HALF_UP)



def boxprint(strings: List[str], title: Optional[str] = None) -> None:
    # Get terminal
    title = str(title)
    terminal_width, _ = shutil.get_terminal_size()

    # Determine column width and number of rows
    max_length = max(len(s) for s in strings + [title])
    # 4 for column padding and separators
    num_columns = max(1, terminal_width // (max_length + 4))
    column_width = (terminal_width - num_columns - 1) // num_columns
    num_rows = -(-len(strings) // num_columns)  # ceil division

    # Prepare box border
    horizontal_border = '+' + '-' * \
        (column_width * num_columns + num_columns - 1) + '+'
    empty_row = '|' + ' ' * \
        (column_width * num_columns + num_columns - 1) + '|'

    # Prepare box title
    if title:
        title_line = '| ' + \
            title.center(column_width * num_columns + num_columns - 2) + '|'
        print(horizontal_border)
        print(title_line)
    print(horizontal_border)

    # Print rows of data
    for i in range(num_rows):
        row_strings = strings[i::num_rows]
        if len(row_strings) < num_columns:
            row_strings.extend([''] * (num_columns - len(row_strings)))
        columns = [s.ljust(column_width - 2) for s in row_strings]
        print('| ' + ' | '.join(c.ljust(column_width - 2)
              for c in columns) + ' |')

    # Print bottom border
    print(empty_row)
    print(horizontal_border)
