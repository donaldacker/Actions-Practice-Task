# Dummy solver script.
# Can be used via command line by providing two input numbers. Returns the result.
#
# (c) 2022 ANSYS, Inc. Unauthorized use, distribution, or duplication is prohibited.

import argparse

def _parse_args():
    """ Passes the command line arguments and returns them as an object. """
    parser = argparse.ArgumentParser()
    parser.add_argument('param_1', type=int, help='The first input parameter. Must be an integer.')
    parser.add_argument('param_2', type=int, help='The second input parameter. Must be an integer.')

    return parser.parse_args()

def solve(param1, param2):
    """ Dummy solve that just substracts the second number from the first and returns the result. """
    return param1 - param2

if __name__ == "__main__":
    arguments = _parse_args()
    print(str(solve(arguments.param_1, arguments.param_2)))
