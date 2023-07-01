from re import findall


def collect_user_includes(file_lines):
    return [line for line in file_lines if line.startswith('#include "')]


def extract_header_path(user_include):
    return findall('#include "(.*)"', user_include)[0]


def get_user_headers_paths(c_file_path):
    includes = collect_user_includes(read_lines_from(c_file_path))
    return [extract_header_path(include) for include in includes]


def read_lines_from(file_path):
    with open(file_path) as f:
        return f.read().splitlines()
