import unittest
import os
import xmlrunner

THIS_DIR = os.path.dirname(__file__)
TEST_LOCATION = THIS_DIR + '/tests'

suite = unittest.defaultTestLoader.discover(TEST_LOCATION)

if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(suite)