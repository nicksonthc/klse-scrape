"""
Unit testing of the automatic batch processing application
"""
import unittest
from main import companyList


class AppTests(unittest.TestCase):
    def test_companyList(self):
        """Simple Tests"""
        self.assertIsNone(companyList(None))

def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(AppTests('test_companyList'))
    # _suite.addTest(AppTests('test_errors'))
    return _suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
