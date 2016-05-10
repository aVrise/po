 awk '{if ( NF == 0  ) printf "\n";else if ( NF == 3 ) printf "%s ",$3}' $FileName

 #!/bin/bash

 if [ -d 5 6 7 8 9 10 ]; then
    exit 0
 else
    for i in {5..10}; do
       mkdir $i
       cd $i
       ln -s ../*
       cd ..
       sed "s/OOOO/$i/" inscan > $i/INSCAN
    done
 fi


for i in {1..9}; do  mkdir $i;  ln * $i/;rm $i/INSCAN $i/zlauncher; sed "s/OOOO/$i/" inscan > $i/INSCAN ;cp zlauncher $i/; done
for i in {1..9}; do  awk '{if ( NF == 0  ) printf "\n";else if ( NF == 3 ) printf "%s ",$3}' PLOTCON$i > m_2h_2o$i; done
grep E CURRENT | awk '{printf "%s    ",$0}' | awk '{for (i=1;i<=91;i++) {for (j=1;j<=100;j++) {for (k=1;k<=90;k++) {printf "%5d%5d%5d   %s\n",k,j,i,$(i+j+k)}}}}' > temp2
