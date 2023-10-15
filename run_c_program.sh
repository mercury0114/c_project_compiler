set -e
if [ -z $1 ]; then
  echo "Please enter relative path (from the current dir) to your_binary.c"
  exit 1
fi
c_binary_full_path=$(realpath $1)

this_shell_script_full_path=$0
compiler_dir=$(dirname "$this_shell_script_full_path")

cd $compiler_dir
project_root_dir=$(python3 -B project_directory_finder.py $c_binary_full_path)
c_paths=$(python3 -B c_paths_collector.py $c_binary_full_path)

cd $project_root_dir 
gcc -Wall -Wextra -g -o /tmp/binary -I./ $c_paths
binary_command_line_arguments=${@:2}
chmod +x /tmp/binary ; /tmp/binary $binary_command_line_arguments
