day=$1
year=`date +'%Y'`

ddir="./$year/$day"
mkdir $ddir

touch "$ddir/data.txt"

touch $ppath
touch $dpath

cp ./template.py "$ddir/solve.py"
