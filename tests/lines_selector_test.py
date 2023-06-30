import unittest

from lines_selector import collect_user_includes


class CollectUserIncludes(unittest.TestCase):
    def test_emptyInput_returnsEmptyList(self):
        self.assertFalse(collect_user_includes([]))

    def test_inputWithoutIncludeLines_returnsEmptyList(self):
        c_code_line = "int main() { return 0; }"
        self.assertFalse(collect_user_includes([c_code_line]))

    def test_inputHasOnlySystemInclude_returnsEmptyList(self):
        system_include = "#include <stdio.h>"
        self.assertFalse(collect_user_includes([system_include]))

    def test_inputHasUserInclude_returnsUserInclude(self):
        user_include = "#include \"path/to/my/header.h\""
        self.assertEquals(collect_user_includes(
            [user_include]), [user_include])

    def test_inputHasMultipleLines_collectsOnlyUserIncludes(self):
        system_include = "#include <stdio.h>"
        user_include = "#include \"path/to/my_header.h\""
        non_include = "int main() { return 0; }"
        self.assertEquals(collect_user_includes([system_include, user_include, non_include]),
                          [user_include])


unittest.main()
