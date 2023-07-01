import unittest

from c_files_collector import get_c_files_to_compile


class GetCFilesToCompile(unittest.TestCase):
    def test_cProgramHasNoDependencies_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile(
            "data/program_without_dependencies.c"))


unittest.main()
