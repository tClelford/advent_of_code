d=$1
f=$2
year=`date +'%Y'`

file="./$year/src/$d.py"
data="./$year/data/$d.txt"

if [ $f="-d" ]
then
    python $file $data
else
    python $file
fi
