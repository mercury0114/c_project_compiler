c_files=$(python3 -B c_paths_collector.py $1 $2)
cd $1
gcc -o /tmp/binary -I./ $2 $c_files
chmod +x /tmp/binary
/tmp/binary
