set -e
if [ -z $1 ]; then
  echo "Please enter relative path (from the current dir) to your_program.c"
  exit 1
fi
dr=$(dirname "$0")
c_program_path=$PWD/$1
project_root_dir=$(python3 -B $dr/project_directory_finder.py $c_program_path)
c_paths=$(python3 -B $dr/c_paths_collector.py $c_program_path)
cd $project_root_dir 
gcc -Wall -Wextra -g -o /tmp/binary -I./ $c_paths
chmod +x /tmp/binary ; /tmp/binary "${@:2}"
