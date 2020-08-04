ver=$1
name=SzaboSolutions
targ=release/$name-$ver
mkdir $targ
for i in {1..7}
do
  cp chap$i/chap$i.pdf $targ
done
cp appendix/appendix.pdf $targ

mkdir $targ/codes
for j in chap1/1-1.nb "chap4/4-11,12.nb" chap5/5-7.nb appendix/C-3.py appendix/C-4.py
do
  cp $j $targ/codes
done

tar czvf $targ.tar.gz $targ


