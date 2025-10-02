import unittest
import calendar

class TestCalendar(unittest.TestCase):

    def test_integer_to_binary(self):
        self.assertEqual(calendar.integer_to_binary(10), '0b1010')
        self.assertEqual(calendar.integer_to_binary(0), '0b0')
        self.assertEqual(calendar.integer_to_binary(1), '0b1')
        self.assertEqual(calendar.integer_to_binary(100), '0b1100100')

if __name__ == '__main__':
    unittest.main()
