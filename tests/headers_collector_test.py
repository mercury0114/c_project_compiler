import unittest

from headers_collector import collect_user_includes
from headers_collector import extract_header_path
from headers_collector import read_lines_from
from headers_collector import get_user_headers_paths


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
        user_include = '#include "path/to/my/header.h"'
        self.assertEqual(collect_user_includes(
            [user_include]), [user_include])

    def test_inputHasMultipleLines_collectsOnlyUserIncludes(self):
        system_include = "#include <stdio.h>"
        user_include = '#include "path/to/header.h"'
        non_include = "int main() { return 0; }"
        self.assertEqual(collect_user_includes([system_include, user_include, non_include]),
                         [user_include])

    def test_inputHasUserIncludeWithComments_returnsUserIncludeLine(self):
        user_include = '#include "library/header.h" // some comment'
        self.assertEqual(collect_user_includes([user_include]), [user_include])


class ExtractHeaderPath(unittest.TestCase):
    def test_extractsExpectedSimplePath(self):
        self.assertEqual(extract_header_path('#include "library/header1.h"'),
                         'library/header1.h')
        self.assertEqual(extract_header_path('#include "library/header2.h"'),
                         'library/header2.h')

    def test_extractsFullPath(self):
        self.assertEqual(extract_header_path('#include "path/to/header.h"'),
                         "path/to/header.h")

    def test_extractsPathFromUserIncludeContainingComment(self):
        self.assertEqual(extract_header_path(
            '#include "library/header.h" // comment'), 'library/header.h')

    def test_headerPathInRootDirectory_throwsException(self):
        self.assertRaisesRegex(ValueError, 'header.h not allowed in project root dir.*',
                               extract_header_path, '#include "header.h"')
        self.assertEqual(extract_header_path(
            '#include "subdirectory/header.h"'), 'subdirectory/header.h')


class GetUserHeadersPaths(unittest.TestCase):
    def test_programWithoutUserHeaders_returnsEmptyList(self):
        self.assertFalse(get_user_headers_paths("tests/data/project0/program_without_dependencies.c"),
                         [])
        self.assertFalse(get_user_headers_paths(
            "tests/data/project0/program_without_user_dependencies.c"), [])

    def test_programWithOneUserHeader_returnsHeader(self):
        self.assertEqual(get_user_headers_paths(
            "tests/data/project1/main.c"), ["library/function.h"])


class ReadLinesFrom(unittest.TestCase):
    def test_oneLineFile_returnsLineWithoutEolSymbol(self):
        self.assertEqual(read_lines_from("tests/data/one_line_file.c"),
                         ["int main() { return 0; }"])

    def test_twoLinesFile_returnsTwoLines(self):
        self.assertEqual(read_lines_from("tests/data/two_lines_file.c"),
                         ["#include <stdio.h>", "#include <stdlib.h>"])


if __name__ == '__main__':
    unittest.main()
