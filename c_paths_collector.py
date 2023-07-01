from sys import argv
from headers_collector import get_user_headers_paths
from os.path import exists, join


class CPathsCollector:
    def __init__(self, project_dir):
        self.project_dir = project_dir
        self.checked_h_paths = set()
        self.collected_c_paths = set()

    def get_more_c_paths(self, c_program_path):
        h_paths = get_user_headers_paths(join(self.project_dir,
                                              c_program_path))
        unchecked_h = [h for h in h_paths if h not in self.checked_h_paths]
        c_paths = [h[:-1] + "c" for h in unchecked_h]
        return list(filter(lambda c: c not in self.collected_c_paths and
                           exists(join(self.project_dir, c)), c_paths))

    def run_recursively(self, c_path):
        unchecked_c_paths = self.get_more_c_paths(c_path)
        any(map(self.collected_c_paths.add, unchecked_c_paths))
        any(map(self.run_recursively, unchecked_c_paths))


def get_c_paths_to_compile(project_dir, c_program_path):
    collector = CPathsCollector(project_dir)
    collector.run_recursively(c_program_path)
    return sorted(list(collector.collected_c_paths))


def main():
    if len(argv) != 3:
        print("Usage:")
        print("python3 c_paths_collector.py project_dir relative/path/to/c")
        exit(1)
    project_dir = argv[1]
    c_program_path = argv[2]
    c_paths = get_c_paths_to_compile(project_dir, c_program_path)
    print(' '.join(c_paths))


if __name__ == '__main__':
    main()
