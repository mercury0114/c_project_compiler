import unittest

from c_files_collector import get_c_files_to_compile


class GetCFilesToCompile(unittest.TestCase):
    def test_emptyInput_returnsEmptyList(self):
        self.assertFalse(get_c_files_to_compile([]))


unittest.main()
