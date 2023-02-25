import unittest
import os
import sys
import xmlrunner

THIS_DIR = os.path.dirname(__file__)
TEST_LOCATION = THIS_DIR + '/tests'
PARENT_DIR = os.path.dirname(THIS_DIR)

suite = unittest.defaultTestLoader.discover(TEST_LOCATION)

if __name__ == '__main__':
    with open(PARENT_DIR+'/logs/results.xml', 'wb') as outfile:
        runner = xmlrunner.XMLTestRunner(output=outfile)
        # xmlrunner doesn't set the right exit code: must do this manually.
        ret = not runner.run(suite).wasSuccessful()
        sys.exit(ret)
