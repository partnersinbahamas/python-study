# argparse is a module with allows to use argument from python command line
# such as python --argument
import argparse

parse = argparse.ArgumentParser(description="Power app.")
# python command-line.py baseArg
parse.add_argument(
    'base',
    type=float,
    help='A number to raise to specific power.'
) # (a1: short-arg-name, a2: full-arg-name, type: type of value, metavar: change the name with --help, default: default value, help: note)

# --exponent=2 || -e 2
parse.add_argument(
    '-e',
    '--exponent',
    type=float,
    help='A power to raise the provided number to.'
) # dash "-" make argument optional

args = parse.parse_args()
base_arg = args.base
e_arg = args.exponent

print('parse: ', parse)

print('--base:',base_arg)
print('--exponent:', e_arg)
print('result of power: ', base_arg ** e_arg)