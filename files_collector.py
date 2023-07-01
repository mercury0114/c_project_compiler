from sys import argv

from headers_collector import collect_user_includes
from headers_collector import extract_headers_paths
from headers_collector import read_lines_from


def collect_include_lines(c_file_path):
    with open(argv[1]) as c_file:
        return [line for line in c_file if line.startswith("#include")]


if len(argv) != 2:
    print("Usage:")
    print("python3 files_collector.py ./relative/path/to/c/file")
    exit(1)

lines = read_lines_from(argv[1])
user_includes = collect_user_includes(lines)
headers = extract_headers_paths(user_includes)
print(headers)
