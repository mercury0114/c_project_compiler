from sys import argv, stderr
from headers_collector import get_user_headers_paths
from os.path import dirname, exists, isfile, join
from pathlib import Path


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


def find_project_dir(c_program_path):
    parents = map(lambda path: path.as_posix(), Path(c_program_path).parents)
    project_root = next((path for path in parents if
                         isfile(f'{path}/WORKSPACE')), None)
    if not project_root:
        raise (FileNotFoundError(
            f'Can not locate project root directory for c_program_path={c_program_path}. Does the project root directory contain WORKSPACE file? Have you specified c_program_path relative to the directory invoking this script?'))
    return project_root


def main():
    if len(argv) != 3:
        stderr.write(
            "Need arguments [project_dir] and [relative/path/to/c]\n")
        invalid_argument_to_exit_shell_error_code = 128
        exit(invalid_argument_to_exit_shell_error_code)
    project_dir = argv[1]
    c_program_path = argv[2]
    c_paths = get_c_paths_to_compile(
        project_dir, c_program_path)
    print(' '.join(c_paths))


if __name__ == '__main__':
    main()
