#!/bin/bash

if [ $4 ] ; then
        AtomSeq=$4
fi

awk -v images=$3 -v AtomSeq=$AtomSeq '

BEGIN{
        _exit_=0;
        ar[0]=images;
        ar[1]=AtomSeq;
        file=0;
        AtomNum=0;
        parts=ar[0]+1;
        for(i in ar){
                j=int(ar[i]);
                if(j!=ar[i]){
                        _exit_=2
                        print "Integer numbers are expected at the 3rd and 4th argument."
                        exit 2
                }
        }
}

{
        if(FNR==10&&NR!=10)
                file+=1;
        b[file,FNR]=$0;
        if(NR==7){
                for(i=1;i<=NF;i++){
                        AtomNum+=$i;
                }
                if(ar[1]<0||ar[1]>AtomNum){
                        print "Wrong Input at the 4th argument."
                        _exit_=1
                        exit 1;
                }
        }
        for(i=1;i<=NF;i++){
                a[file,FNR,i]=$i;
                if(i<=3)
                        if($i<0)
                                a[file,FNR,i]=$i+1;
                        else if($i>1)
                                a[file,FNR,i]=$i-1;
                }
        }

END{
if(_exit_)
        exit _exit_;
if(ar[1]!=0)
        for(j=ar[0];j>=1;j--){
                RowNum=ar[1]+9;
                printf "%20.16f%20.16f%20.16f%4s%4s%4s\n",a[1,RowNum,1]+(a[0,RowNum,1]-a[1,RowNum,1])*j/parts,a[1,RowNum,2]+(a[0,RowNum,2]-a[1,RowNum,2])*j/parts,a[1,RowNum,3]+(a[0,RowNum,3]-a[1,RowNum,3])*j/parts,a[0,RowNum,4],a[0,RowNum,5],a[0,RowNum,6];
        }
else{
        RowNum=AtomNum+9;
        for(j=ar[0];j>=1;j--){
                for(i=1;i<=RowNum;i++){
                        if(i<10)
                                print b[0,i] > parts-j;
                        else
                                printf "%20.16f%20.16f%20.16f%4s%4s%4s\n",a[1,i,1]+(a[0,i,1]-a[1,i,1])*j/parts,a[1,i,2]+(a[0,i,2]-a[1,i,2])*j/parts,a[1,i,3]+(a[0,i,3]-a[1,i,3])*j/parts,a[0,i,4],a[0,i,5],a[0,i,6] > parts-j;
                        }
                }
        }
}' $1 $2
