from sys import argv
from c_paths_collector import get_c_paths_to_compile

if len(argv) != 3:
    print("Usage:")
    print("python3 files_collector.py project_dir relative/path/to/c/file")
    exit(1)

print(get_c_paths_to_compile(argv[1], argv[2]))
