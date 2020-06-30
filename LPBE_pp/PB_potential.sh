#!/bin/bash
#Creator: Stephan N. Steinmann
#Help can be obtained from:
# stephan.steinmann@ens-lyon.fr
#Purpose: Compute the electronic Free Energy as a function of the electrochemical potential
#Requirements: 	vasp 5.x Output files (OUTCAR and "out" from stdout) in folders that are named according to their NELECT tag.
# 		Or provided by this package
#               Gnuplot, awk
#How to use it: 
#a) make sure you have at least 3 converged charge states, including the neutral system. 
#b) Run the script in the "main" folder, i.e., in the folder where the subfolders with the names of the NELECT values are located.
#   Use as: PB_potential.sh NELECT_Neutral 
#Output:
#b) dat file: Data used for fitting in gnuplot.
#c) fit.plot Inputfile for gnuplot: useful if you have to delete data points that deviate from the parabola because of charge-spilling into the background
#d) fit.log: log file for the fit, containing the paramerters for the parabola
#e) dat.dat: values of the parabola in a regular interval, given in the fit.plot file
#f) charge.dat: the values of the charge as a function of the electrochemical potential
#g) pot.png: image showing the fitted G(V) parabola and the corresponding points.
#h) charge.png: same, but the electronic charge as a function of the electrochemical potential
#Info:
# We strongly recommend to use at least an implicit solvent model, e.g., 
# https://github.com/henniggroup/VASPsol
fin(){
if [ -e $1 ] ; then
if [ "x`grep 'reached required accuracy - stopping structural energy minimisation' $1`" == "x" ] ; then
echo "Unfinished"
else
echo "OK"
fi
else
echo "Running"
fi
}

#Check out files
for i in `find . -name print-out` ; do j=`dirname $i`; echo $i `awk '/FERMI_SHIFT/{E=$3*1} END{if(E==0){print "ProblemWithFermiShift"}}' $i` `fin $j/OUTCAR` ; done

#Setup the necessary files:
#echo "3" > 3
#Gnuplot fitting file: change the interval and resolution to match your needs.
exec 3> fit.plot
cat >&3 <<-EOF
set term png
set xlabel "Potential(vs SHE)/V"
set ylabel "G/eV"
set output "pot.png"
f(x)=a*x*x+b*x+c
f2(x)=a2*x*x+b2*x+c2
fit f(x) 'dat' u 1:4 via a,b,c
fit f2(x) 'dat' u 1:5 via a2,b2,c2
plot 'dat' u 1:4 ti "data", f(x) ti "fit"
set ylabel "Electrons/e"
set output "charge.png"
plot 'dat' u 1:5 ti "data", f2(x) ti "fit"
#Change for resolution:
set samples 9
set table "dat.dat"
set format y "%+-14.6f"
#Change for interval of your interest
plot [-2.000:2.0000] f(x)
set table "charge.dat"
set format y "%+-14.6f"
set samples 15
plot [-2.000:1.5000] f2(x)
print f(-2)

EOF

exec 3>&-

#Define the function to extract useful data from OUTCAR and out files:
get_el(){
line=$2
if [ -e $1/OUTCAR ] ; then
# print "NELECT" "Total Energy" "E-fermi" "fermi_shift"
echo `awk '/NELECT/{print $3}' $1/OUTCAR` `awk '/y=/{E=$7}/E-fermi/{F=$3} END{print E, F}' $1/OUTCAR` `awk -v n=$line '{if($0~/FERMI_SHIFT/){A=$3}}END{printf "%10.5f\n", A*1.0}' $1/print-out*`
elif [ -e $1/OUTCAR.gz ] ; then
echo `awk '/NELECT/{print $3}' $1/OUTCAR` `zgrep 'E-fermi\|y=' $1/OUTCAR.gz | awk '/y=/{E=$7}/E-fermi/{F=$3} END{print E, F}'` `awk -v n=$line '{if($0~/FERMI_SHIFT/){A=$3}}END{printf "%10.5f\n", A*1.0}' $1/print-out*`
else
echo "No OUTCAR or OUTCAR.gz file"
fi
}


#Store the arguments from the command line:
ref=$1

echo "Processing"
for i in `ls -d */ `  ; do 
>&2 echo $i 
get_el $i $point ; done | sed '/No/d' | sort  -k 1,1 > raw
awk  -v a=`awk '/NELECT/{print $3}' $ref/OUTCAR` '{
N[NR]= $1;
E[NR]=$2;
EF[NR]=$3;
EV[NR]=$4;
W[NR]=-$4-$3;
if($1==a){ref=NR}}
END{#Int=0;
#Reference point
# "Potential vs SHE", "delta(NELECT)", "Total Energy", "G=Total Energy+Workfunction*delta(NELECT)", "NELECT", "workfunction"
printf "%10.3f %s %10.6f %10.6f %s %10.3f\n", W[ref]-4.44,0.0,E[ref],E[ref],N[ref],W[ref]
#Positively charged
for(i=ref-1;i>=1;i--){
if(i<ref){
#Int+=(N[i]-N[i+1])*(EV[i]+EV[i+1])/2;
printf "%10.3f %s %10.6f %10.6f %s %10.3f\n", W[i]-4.44,(N[i]-N[ref]), E[i], E[i]+W[i]*(N[i]-N[ref]),N[i],W[i]
}}
Int=0
#Negatively charged
for(i=ref+1;i<=NR;i++){
if(i>ref){
printf "%10.3f %s %10.6f %10.6f %s %10.3f\n", W[i]-4.44,(N[i]-N[ref]), E[i], E[i]+W[i]*(N[i]-N[ref]),N[i],W[i]
}}
}' raw > dat
gnuplot < fit.plot 2> fit.log

#Clean up:
#rm raw 3
