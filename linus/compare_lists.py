import sys
import argparse


def populate_parser(parser):
    parser.add_argument('--one', nargs='*', required=True, help='First list')
    parser.add_argument('--two', nargs='*', required=True, help='Second list')


def main(args=None):
    if not args:
        parser = argparse.ArgumentParser(prog=__name__)
        populate_parser(parser)
        args = vars(parser.parse_args())

    first_set = set(args['one'])
    second_set = set(args['two'])

    if first_set == second_set:
        sys.stdout.write('No difference\n')
    elif len(first_set.intersection(second_set)) == 0:
        sys.stdout.write('Nothing in common\n')
    else:
        sys.stdout.write('Exclusive to first list:\n{}\n'.format(first_set - second_set))
        sys.stdout.write('Exclusive to second list:\n{}\n'.format(second_set - first_set))
        sys.stdout.write('Common between both:\n{}\n'.format(first_set.intersection(second_set)))
