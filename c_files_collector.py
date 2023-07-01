from headers_collector import get_user_headers_paths


def get_c_files_to_compile(c_program_path):
    headers = get_user_headers_paths(c_program_path)
    return [header[:-1] + "c" for header in headers]
