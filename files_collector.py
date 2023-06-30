from sys import argv


def collect_include_lines(c_file_path):
    with open(argv[1]) as c_file:
        return [line for line in c_file if line.startswith("#include")]


if len(argv) != 2:
    print("Usage:")
    print("python3 files_collector.py ./relative/path/to/c/file")
    exit(1)

include_lines = collect_include_lines(argv[1])
print(include_lines)
