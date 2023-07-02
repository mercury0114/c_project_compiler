from headers_collector import get_user_headers_paths
from os.path import exists, join
from project_directory_finder import find_project_dir
from sys import argv, stderr


class CPathsCollector:
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.checked_h_paths = set()
        self.collected_c_paths = set()

    def get_more_c_paths(self, c_path):
        h_paths = get_user_headers_paths(join(self.project_dir,
                                              c_path))
        unchecked_h = [
            h for h in h_paths if h not in self.checked_h_paths]
        c_paths = [
            h[:-1] + "c" for h in unchecked_h]
        return list(filter(lambda c: c not in self.collected_c_paths and
                           exists(join(self.project_dir, c)), c_paths))

    def run_recursively(self, c_path):
        unchecked_c_paths = self.get_more_c_paths(
            c_path)
        any(map(self.collected_c_paths.add,
            unchecked_c_paths))
        any(map(self.run_recursively, unchecked_c_paths))


def get_c_paths_to_compile(project_dir, c_path_relative_to_project_dir):
    collector = CPathsCollector(project_dir)
    collector.run_recursively(
        c_path_relative_to_project_dir)
    return sorted(list(collector.collected_c_paths))


def main():
    if len(argv) != 2:
        stderr.write(
            "Need argument [c_program_path]\n")
        invalid_argument_to_exit_shell_error_code = 128
        exit(invalid_argument_to_exit_shell_error_code)
    project_root_dir = find_project_dir(argv[1])
    c_program_path_relative_to_root = argv[1].replace(project_root_dir, '')
    stderr.write(project_root_dir + '\n')
    stderr.write(c_program_path_relative_to_root + '\n')
    c_paths = get_c_paths_to_compile(project_root_dir,
                                     c_program_path_relative_to_root)
    print(f'{c_program_path_relative_to_root} ' + ' '.join(c_paths))


if __name__ == '__main__':
    main()
