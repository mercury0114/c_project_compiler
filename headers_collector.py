def collect_user_includes(file_lines):
    return [line for line in file_lines if line.startswith("#include \"")]


def extract_headers_paths(user_includes):
    return [include[10:-1] for include in user_includes]
