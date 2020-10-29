import argparse
import os
from pathlib import Path


def run(args):
    """Run the main program with arguments

    Args:
        args (Namespace): A namespace populated with attributes from argparse
    """
    result = None
    setA = set()
    setB = set()
    for item in handle_file(args.fileA, args.delimiter, args.column,
                            args.no_headers):
        setA.add(item)
    for item in handle_file(args.fileB, args.delimiter, args.column,
                            args.no_headers):
        setB.add(item)
    if args.operation == 'subtract':
        # Set should contain only strings so this should be fine
        print('\n'.join(setA - setB))
    elif args.operation == 'add':
        print('\n'.join(setA | setB))
    elif args.operation == 'multiply':
        print('\n'.join(setA & setB))


def parse_args():
    """Parse the arguments from the commandline input
    """
    #  Main parser
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Useful data manipulation tools')
    subparsers = parser.add_subparsers(help='Sub-command help')

    # Compare parser
    compare_parser = subparsers.add_parser(
        'compare', help='Compare two files in various ways')
    compare_parser.add_argument('fileA',
                                type=argparse.FileType('r'),
                                help='File A')
    compare_parser.add_argument('fileB',
                                type=argparse.FileType('r'),
                                help='File B')
    compare_parser.add_argument('-op',
                                '--operation',
                                help='The operation to perform: "A op B".',
                                choices=('add', 'subtract', 'multiply'),
                                default='subtract')
    compare_parser.add_argument(
        '-nh',
        '--no_headers',
        action='store_false',
        help=
        'Assume compared files have headers and remove them unless this flag is set.'
    )
    compare_parser.add_argument(
        '-de',
        '--delimiter',
        help='The delimiter to use if files have multiple columns',
        default=',')
    compare_parser.add_argument(
        '-c',
        '--column',
        type=int,
        help=
        'The column number to compare, first column is 0, second is 1, and so on.',
        default=0)

    return parser.parse_args()


def handle_file(fileobj, delimiter, column, header):
    if header:
        next(fileobj)
    for line in fileobj:
        if column:
            yield line.strip().split(delimiter)[column]
        else:
            yield line.strip()


def main():
    """Call the main program with arguments from command line by default
    """
    args = parse_args()
    run(args)


if __name__ == '__main__':
    main()