import unittest

from lines_selector import collect_include_lines


class LinesSelector(unittest.TestCase):
    def test_when_input_empty_collects_no_lines(self):
        self.assertFalse(collect_include_lines([]))


unittest.main()
