import unittest

from headers_collector import collect_user_includes
from headers_collector import extract_headers_paths
from headers_collector import read_lines_from


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
        self.assertEqual(collect_user_includes(
            [user_include]), [user_include])

    def test_inputHasMultipleLines_collectsOnlyUserIncludes(self):
        system_include = "#include <stdio.h>"
        user_include = "#include \"path/to/header.h\""
        non_include = "int main() { return 0; }"
        self.assertEqual(collect_user_includes([system_include, user_include, non_include]),
                         [user_include])


class GetHeadersPaths(unittest.TestCase):
    def test_emptyInput_returnsEmptyList(self):
        self.assertFalse(extract_headers_paths([]))

    def test_inputHasUserInclude_returnsHeaderPath(self):
        self.assertEqual(extract_headers_paths(["#include \"path/to/header.h\""]),
                         ["path/to/header.h"])

    def test_inputHasTwoIdenticalIncludes_throwsException(self):
        return


class ReadLinesFrom(unittest.TestCase):
    def test_oneLineFile_returnsLineWithoutEolSymbol(self):
        self.assertEqual(read_lines_from("tests/data/one_line_file.c"),
                         ["int main() { return 0; }"])


unittest.main()
