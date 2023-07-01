def collect_user_includes(file_lines):
    return [line for line in file_lines if line.startswith("#include \"")]


def extract_header_path(user_include):
    return user_include[10:-1]


def get_user_headers_paths(c_file_path):
    return []


def read_lines_from(file_path):
    with open(file_path) as f:
        return f.read().splitlines()
