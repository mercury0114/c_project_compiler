from re import findall


def collect_user_includes(file_lines):
    return [line for line in file_lines if line.startswith('#include "')]


def extract_header_path(user_include):
    header_path = findall('#include "(.*)"', user_include)[0]
    if '/' not in header_path:
        raise (ValueError(
            f'{header_path} not allowed in project root dir. Move it to some subdirectory, e.g.: library/{header_path}'))
    return header_path


def get_user_headers_paths(c_file_path):
    includes = collect_user_includes(read_lines_from(c_file_path))
    return [extract_header_path(include) for include in includes]


def read_lines_from(file_path):
    with open(file_path) as f:
        return f.read().splitlines()
