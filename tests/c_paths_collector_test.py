import unittest

from c_paths_collector import get_c_paths_to_compile


class GetCPathsToCompile(unittest.TestCase):
    def test_cProgramHasNoDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_paths_to_compile("tests/data/project0",
                                                "program_without_dependencies.c"))

    def test_cProgramHasNoUserDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_paths_to_compile(
            "tests/data/project0", "program_without_user_dependencies.c"))

    def test_cProgramHasOneUserDependency_returnsCDependencyPath(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project1", "main.c"), ["library.c"])

    def test_cProgramHasTwoUserDependencies_returnsTwoPaths(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project2", "main.c"), ["library1.c", "library2.c"])

    def test_cProgramDependsOnTwoHeadersAndOneCFile_returnsCFilePath(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project3", "main.c"), ["function.c"])

    def test_cProgramHasIndirectDependencies_returnsAllCPaths(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project4", "main.c"), ["function.c", "structure.c"])


unittest.main()
