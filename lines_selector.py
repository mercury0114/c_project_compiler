def collect_include_lines(file_lines):
    return [line for line in file_lines if line.startswith("#include <")]
