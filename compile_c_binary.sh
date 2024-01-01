# The script will compile your_binary.c and output the compiled binary path
set -e
if [ -z $1 ]; then
  echo "Please enter relative path (from the current dir) to your_binary.c"
  exit 1
fi
c_source_full_path=$(realpath $1)
c_binary_name=$(basename $1 | sed -e 's/\.[^\.]*$//g')

this_shell_script_full_path=$0
compiler_dir=$(dirname "$this_shell_script_full_path")

cd $compiler_dir
project_root_dir=$(python3 -B project_directory_finder.py $c_source_full_path)
c_paths=$(python3 -B c_paths_collector.py $c_source_full_path)

cd $project_root_dir 
gcc -Wall -Wextra -g -o /tmp/$c_binary_name -I./ $c_paths
echo /tmp/$c_binary_name
