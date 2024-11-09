import tests_12_3
import unittest
from unittest import TestSuite

test = TestSuite()

test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test)

