# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(3), 6)
        pass

    def test_roots(self):
        self.assertEqual(utils.roots(1, 0, 1), ())
        self.assertEqual(utils.roots(1, 0, 0), (0,))
        self.assertEqual(utils.roots(2, 5, 2), (-0.5, -2))
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())