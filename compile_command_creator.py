from sys import argv
from c_paths_collector import get_c_paths_to_compile

if len(argv) != 3:
    print("Usage:")
    print("python3 files_collector.py project_dir relative/path/to/c/file")
    exit(1)
project_dir = argv[1]
c_program_path = argv[2]

c_paths = get_c_paths_to_compile(project_dir, c_program_path)
print(f"gcc {c_program_path} {' '.join(c_paths)}")
