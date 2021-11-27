#!/usr/bin/python
"""Script that forms part of pwb_tests."""
#
# (C) Pywikibot team, 2018-2021
#
# Distributed under the terms of the MIT license.
#
import pywikibot


def main() -> None:
    """Print umlauts."""
    pywikibot.output('Häuser')
    print('Häuser')


if __name__ == '__main__':
    main()
