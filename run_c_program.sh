set -e
dr=$(dirname "$0")
c_program_path=$PWD/$1
project_root_dir=$(python3 -B $dr/project_directory_finder.py $c_program_path)
c_paths=$(python3 -B $dr/c_paths_collector.py $c_program_path)
cd $project_root_dir 
gcc -o /tmp/binary -I./ $c_paths
chmod +x /tmp/binary ; /tmp/binary
