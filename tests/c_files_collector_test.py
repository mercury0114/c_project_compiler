import unittest

from c_files_collector import get_c_files_to_compile


class GetCFilesToCompile(unittest.TestCase):
    def test_cProgramHasNoDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile(
            "tests/data/project0/program_without_dependencies.c"))

    def test_cProgramHasNoUserDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile(
            "tests/data/project0/program_without_user_dependencies.c"))


unittest.main()
