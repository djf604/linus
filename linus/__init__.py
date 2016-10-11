import argparse

from linus import compare_lists


def readlines(filepath, strip=None, split=None):
    with open(filepath, 'r') as filehandle:
        return [line.strip(strip).split(split)
                for line in filehandle.readlines()]


def add_column(filepath, col, elem, elem_func_args=None, elem_func_kwargs=None, delimiter='\t'):
    is_callable = hasattr(elem, '__call__')
    tmp_write_file = 'todo'
    with open(filepath, 'r') as filehandle:
        for line in filehandle:
            record = line.strip().split(delimiter)



def swap_columns(filepath, columns=None, delimiter='\t'):
    pass


def execute_from_command_line():
    parser = argparse.ArgumentParser(prog='linus')
    subparsers = parser.add_subparsers()

    subprograms = [
        (compare_lists, 'compare-lists')
    ]

    for module, name in subprograms:
        subp = subparsers.add_parser(name)
        subp.set_defaults(func=module.main)
        module.populate_parser(subp)

    args = parser.parse_args()
    args.func(vars(args))