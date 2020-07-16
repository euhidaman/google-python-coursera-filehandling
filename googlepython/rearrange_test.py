from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase="Aman, Euhid"
        expected="Euhid Aman"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_adv(self):
        testcase="L. Cooper, Sheldon"
        expected="Sheldon L. Cooper"
        self.assertEqual(rearrange_name(testcase),expected)

    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected)


unittest.main()
