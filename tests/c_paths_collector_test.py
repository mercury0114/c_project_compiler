import unittest

from c_paths_collector import find_project_dir
from c_paths_collector import get_c_paths_to_compile


class GetCPathsToCompile(unittest.TestCase):
    def test_cProgramHasNoDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_paths_to_compile("tests/data/project0",
                                                "program_without_dependencies.c"))

    def test_cProgramHasNoUserDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_paths_to_compile(
            "tests/data/project0", "program_without_user_dependencies.c"))

    def test_cProgramHasOneUserDependency_returnsDependencyPath(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project1", "main.c"), ["library/function.c"])

    def test_cProgramHasTwoUserDependencies_returnsTwoPaths(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project2", "main.c"), ["library/function1.c", "library/function2.c"])

    def test_cProgramDependsOnTwoHeadersAndOneCFile_returnsCFilePath(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project3", "main.c"), ["library/function.c"])

    def test_cProgramHasIndirectDependencies_getsAllDependenciesPaths(self):
        self.assertEqual(get_c_paths_to_compile(
            "tests/data/project4", "main.c"), ["library/function.c", "library/structure.c"])

    def test_cProgramNotInRootDirectory_getsAllDependenciesPaths(self):
        self.assertEqual(get_c_paths_to_compile("tests/data/project5", "dir/main.c"),
                         ['dir/function.c', 'dir/subdir/function.c', 'dir2/function.c'])


class FindProjectDir(unittest.TestCase):
    def test_noProjectDir_throwsException(self):
        self.assertRaisesRegex(FileNotFoundError, 'Can not locate project root directory *',
                               find_project_dir, '/')

    def test_cProgramInRootDirectory_returnsRootDirectory(self):
        self.assertEqual(find_project_dir("tests/data/project1/main.c"),
                         "tests/data/project1/")
        self.assertEqual(find_project_dir('tests/data/project2/main.c'),
                         'tests/data/project2/')

    def test_cProgramInSubdirectory_returnsRootDirectory(self):
        self.assertEqual(find_project_dir('tests/data/project5/dir/main.c'),
                         'tests/data/project5/')

    def test_cProjectRootMatchesScriptInvocationDir_returnsProjectRoot(self):
        self.assertEqual(find_project_dir('./main.c'), './')
        self.assertEqual(find_project_dir('main.c'), './')


if __name__ == '__main__':
    unittest.main()
