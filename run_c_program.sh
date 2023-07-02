set -e
c_program_path=$1
project_root_dir=$(python3 -B project_directory_finder.py $c_program_path)
c_paths=$(python3 -B c_paths_collector.py $c_program_path)
cd $project_root_dir 
gcc -o /tmp/binary -I./ $c_paths
chmod +x /tmp/binary ; /tmp/binary
