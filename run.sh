d=$1
f=$2
year=`date +'%Y'`

file="./$year/src/$d.py"
data="./$year/data/$d.txt"

if [ -z $f ];
then
    python $file
else
    python $file $data
fi
