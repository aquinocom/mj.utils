from  mj.utils.testing import MJ_UTILS_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=MJ_UTILS_FUNCTIONAL_TESTING)
    ])
    return suite