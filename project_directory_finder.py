from os.path import isfile
from pathlib import Path
from sys import argv, stderr


def find_project_dir(c_program_path):
    parents = map(lambda path: path.as_posix(), Path(c_program_path).parents)
    project_root = next((path for path in parents if
                         isfile(f'{path}/WORKSPACE')), None)
    if not project_root:
        raise (FileNotFoundError(
            f'Can not locate project root directory for c_program_path={c_program_path}. Does the project root directory contain WORKSPACE file? Have you specified c_program_path relative to the directory invoking this script?'))
    return project_root + '/'


def main():
    if len(argv) != 2:
        stderr.write(
            "Need argument [c_program_path]\n")
        invalid_argument_to_exit_shell_error_code = 128
        exit(invalid_argument_to_exit_shell_error_code)
    print(find_project_dir(argv[1]))


if __name__ == '__main__':
    main()
