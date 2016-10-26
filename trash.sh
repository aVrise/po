#!/bin/bash

#trash is a script to immitate trash in mac.
#DO NOT trash the "EMPTY" file.

if [ $1 ]; then
   if [ $1 == "EMPTY" ]; then
      cat ~/.trash | xargs rm -rf
      rm -f ~/.trash
      echo "All files are removed"
   else
      if [ ! -d .trashtemp ]; then
         mkdir .trashtemp
         echo $PWD/.trashtemp >> ~/.trash
      fi
      mv $1 .trashtemp/
      sed -i "s#$PWD/$1#$PWD/.trashtemp/$1#"  ~/.trash
   fi
else
   if [ -f ~/.trash ]; then
      for i in `cat ~/.trash` ; do
         echo "$i:"
         ls $i
      done
   else
      echo "There is no file in the trash"
   fi
fi
