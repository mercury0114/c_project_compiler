set -e
c_files=$(python3 -B c_paths_collector.py $1 $2)
cd $1
command="gcc -o /tmp/binary -I./ $2 $c_files"
echo "Compiling with command:"
echo "$command"
$command
chmod +x /tmp/binary
/tmp/binary
