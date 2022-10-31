ver=$1
name=SzaboSolutions
targ=release/$name-$ver
mkdir -p release
mkdir -p $targ
for i in {1..7}
do
  cd chap$i
  latexmk -xelatex  -halt-on-error -shell-escape chap$i
  cp chap$i.pdf ../$targ
  cd ..
done
cd appendix
latexmk -xelatex  -halt-on-error -shell-escape appendix
cp appendix.pdf ../$targ
cd ..

mkdir -p $targ/codes
for j in chap1/1-1.nb chap1/1-3.nb "chap4/4-11,12.nb" "chap4/4-14,15.nb" chap5/5-7.nb chap5/5-9+.nb chap5/5-12.nb chap5/5-16+.nb chap6/6-6.nb appendix/C-3.py appendix/C-4.py
do
  cp $j $targ/codes
done

#tar czvf $targ.tar.gz $targ


