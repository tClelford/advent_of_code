day=$1
year=`date +'%Y'`

ppath="./$year/src/$day.py"
dpath="./$year/data/$day.txt"

touch $ppath
touch $dpath

cp ./template.py $ppath