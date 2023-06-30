def collect_user_includes(file_lines):
    return [line for line in file_lines if line.startswith("#include \"")]
