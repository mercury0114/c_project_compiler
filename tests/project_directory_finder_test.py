import unittest

from project_directory_finder import find_project_dir


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
