set -e
if [ -z $1 ]; then
  echo "Please enter relative path (from the current dir) to your_binary.c"
  exit 1
fi
c_source_full_path=$(realpath $1)
this_shell_script_path=$0
compiler_dir=$(dirname "$this_shell_script_path")

c_binary_path=$($compiler_dir/compile_c_binary.sh $c_source_full_path)
binary_command_line_arguments=${@:2}
chmod +x $c_binary_path ; $c_binary_path $binary_command_line_arguments
