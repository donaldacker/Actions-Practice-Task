# Unittests for solver_add.py
#
# (c) 2022 ANSYS, Inc. Unauthorized use, distribution, or duplication is prohibited.

import unittest
import sys
import os

# Add the solver.py location to sys path
THIS_DIR = os.path.dirname(__file__)
SCRIPT_LOCATION = os.path.dirname(THIS_DIR)
sys.path.append(SCRIPT_LOCATION)
import solver_add

class TestSolver(unittest.TestCase):
    """ Test class for the dummy solver """

    def test_solve(self):
        self.assertEqual(solver_add.solve(1, 2), 3)

    def test_solve_negative(self):
        self.assertEqual(solver_add.solve(-1, -2), -3)

    def test_solve_zero(self):
        self.assertEqual(solver_add.solve(0, 0), 0)


if __name__ == "__main__":
    unittest.main()