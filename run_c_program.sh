set -e
project_root_dir=$1
relative_c_program_path=$2

c_paths=$(python3 -B c_paths_collector.py $project_root_dir $relative_c_program_path)
cd $project_root_dir
set -x
gcc -o /tmp/binary -I./ $relative_c_program_path $c_paths

chmod +x /tmp/binary | /tmp/binary
