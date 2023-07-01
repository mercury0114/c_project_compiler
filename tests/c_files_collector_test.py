import unittest

from c_files_collector import get_c_files_to_compile


class GetCFilesToCompile(unittest.TestCase):
    def test_cProgramHasNoDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile(
            "tests/data/project0/program_without_dependencies.c"))

    def test_cProgramHasNoUserDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile(
            "tests/data/project0/program_without_user_dependencies.c"))

    def test_cProgramHasOneUserDependency_returnsCDepenencyPath(self):
        self.assertEqual(get_c_files_to_compile(
            "tests/data/project1/main.c"), ["library.c"])

    def test_cProgramHasTwoUserDependencies_returnsTwoPaths(self):
        self.assertEqual(get_c_files_to_compile(
            "tests/data/project2/main.c"), ["library1.c", "library2.c"])


unittest.main()
