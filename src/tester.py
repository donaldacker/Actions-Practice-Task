import unittest
import os
import xmlrunner

THIS_DIR = os.path.dirname(__file__)
TEST_LOCATION = THIS_DIR + '/tests'
PARENT_DIR = os.path.dirname(THIS_DIR)

suite = unittest.defaultTestLoader.discover(TEST_LOCATION)

if __name__ == '__main__':
    with open(PARENT_DIR+'/results.xml', 'wb') as outfile:
        runner = xmlrunner.XMLTestRunner(output=outfile)
        runner.run(suite)
