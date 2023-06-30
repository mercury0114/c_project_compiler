from sys import argv


if len(argv) != 2:
    print("Usage:")
    print("python3 files_collector.py ./relative/path/to/c/file")
    exit(1)

with open(argv[1]) as c_file:
    for line in c_file:
        print(line)