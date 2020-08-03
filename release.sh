ver=$1
name=SzaboSolutions
mkdir release/$name-$ver
for i in {1..7}
do
  cp chap$i/chap$i.pdf ../$name-$ver
done
cp appendix/appendix.pdf ../$name-$ver

tar czvf ../$name-$ver.tar.gz ../$name-$ver


