import unittest

from lines_selector import collect_include_lines


class CollectIncludeLines(unittest.TestCase):
    def test_emptyInput_returnsEmptyOutput(self):
        self.assertFalse(collect_include_lines([]))

    def test_inputWithoutIncludeLines_returnsEmptyOutput(self):
        c_code_line = "int main() { return 0; }"
        self.assertFalse(collect_include_lines([c_code_line]))

    def test_inputHasSystemHeader_returnsSystemHeader(self):
        system_header = "#include <stdio.h>"
        self.assertEquals(collect_include_lines(
            [system_header]), [system_header])


unittest.main()
