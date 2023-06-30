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

    def test_inputHasUserHeader_returnsUserHeader(self):
        user_header = "#include \"path/to/my/header.h\""
        self.assertEquals(collect_include_lines([user_header]), [user_header])

    def test_inputHasMultipleLines_collectsOnlyHeaders(self):
        system_header = "#include <stdio.h>"
        user_header = "#include \"path/to/my_header.h\""
        non_header = "int main() { return 0; }"
        self.assertEquals(collect_include_lines([system_header, user_header, non_header]),
                          [system_header, user_header])


unittest.main()
