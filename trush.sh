#!/bin/bash

#trush is a script to immitate trush in mac.
#DO NOT trush the "EMPTY" file.

if [ $1 ]; then
   if [ $1 == "EMPTY" ]; then
      cat ~/.trush | xargs rm -rf
      rm -f ~/.trush
      echo "All files are removed"
   else
      if [ ! -d .trushtemp ]; then
         mkdir .trushtemp
         echo $PWD/.trushtemp >> ~/.trush
      fi
      mv $1 .trushtemp/
      sed -i "s#$PWD/$1#$PWD/.trushtemp/$1#"  ~/.trush
   fi
else
   if [ -f ~/.trush ]; then
      for i in `cat ~/.trush` ; do
         echo "$i:"
         ls $i
      done
   else
      echo "There is no file in the trush"
   fi
fi
