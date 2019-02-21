#! /etc/bin/env python3

import argparse
from argparse import ArgumentParser

calc = {
        'plus' : lambda a, b: a + b,
        'minus' : lambda a, b: a - b,
        'div': lambda a, b: a / b,
        'mult': lambda a, b: a * b
        }


def main():
    parser = ArgumentParser()
    parser.add_argument('-o', '--operation', dest='operation', default = 'plus')
    parser.add_argument('op1', type=float)
    parser.add_argument('op2', type=float)
    args = parser.parse_args()
    print('op1: {}, op2: {}'.format(args.op1, args.op2))

    op = args.operation

    if op in calc:
        print('Ergebnis: {}'.format(calc[op](args.op1, args.op2)))
    else:
        parser.error('Unspecified operator {}. Supported operators:{}'.format(op, calc.keys()))





if __name__ == '__main__':
    main()
