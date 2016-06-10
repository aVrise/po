#!/bin/bash

if [ -f PROCARtip ]; then
   rm -f PROCARtip
fi

File='demo'

nspin=$(grep ISPIN INCAR | sed 's/ //g' | sed 's/[^0-9]//g')
nkpts=$(sed -n '2s/:/#/pg' $File | awk  '{print $4}')
nbands=$(sed -n '2s/:/#/pg' $File | awk  '{print $8}')
nions=$(sed -n '2s/:/#/pg' $File | awk  '{print $12}')
grep -w k-point $File | awk '{print $1,$2,$4,$5,$6,$9}' > _kpo.pro
grep -w band $File | awk '{print $3,$2,$5,$8}' > _band.pro
grep -w $nions $File | grep -v band > _ion.pro
i=1
j=1
k=1
#echo $nspin,$nkpts,$nbands,$nions

while [ $i -le $nspin ] ; do
   i=$(($i+1))
   while [ $j -le $nkpts ] ; do
      j=$(($j+1))
      echo >> PROCARtip.pro
      sed -n '1p' _kpo.pro >> PROCARtip.pro
      sed -i '1d' _kpo.pro
      while [ $k -le $nbands ] ; do
         k=$(($k+1))
         echo >> PROCARtip.pro
         sed -n '1p' _band.pro >> PROCARtip.pro
         sed -i '1d' _band.pro
         echo >> PROCARtip.pro
         echo "ion      s     py     pz     px    dxy    dyz    dz2    dxz    dx2    tot" >> PROCARtip.pro
         sed -n '1,3p' _ion.pro >> PROCARtip.pro
         sed -i '1,3d' _ion.pro
      done
      k=1
   done
   j=1
done

echo > PROCARtip
echo $nkpts $nbands $nspin >> PROCARtip
awk '{print $2,$3,$4,$5,$6,$7,$8,$9,$10,$11}' PROCARtip.pro >> PROCARtip
rm -f PROCARtip.pro _ion.pro _band.pro _kpo.pro
