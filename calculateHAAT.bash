#!/bin/bash

#*******************************************************************************
# Mofolo Mofolo; mmofolo@csir.co.za
# November 2016
#
# extract_haat.sh: 
# Bash script to calculate HAAT given TV transmitter information
#*******************************************************************************

# make sure filename supplied at a shell prompt else die

 
TXinfo="1++BW++Gaborone++DVB-T2++HOR++Operational++478++22++5++90++95"

[[ $# -eq 0  || $# -lt 3  ]] && { echo "Usage: $0 latitude longitude antennaHeight "; exit 1; } 

#echo -e "$1 \t $2 \t$3 "
latitude=$1 
longitude=$2
antennaHeight=$3
echo -e "$latitude \t $longitude \t$antennaHeight "

# Directory where splat saves the genetated point-to-point analyis
rdir="/home/ubuntu/data/dataset_monitor/splat_results/"
# Check if directory exists
if [ ! -d "$rdir" ]; then
  # directory doesn't exist, create it:
  echo -e "Creating new directory... $rdir"
  mkdir $rdir
fi

#Terrian files are under the following directory"
terrian="/home/ubuntu/data/Africa_sdf/"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# clean directories

rm -rf $rdir*

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create Longlry rice parameters
create_lrp(){
  dielectric=15.000	# Earth Dielectric Constant (Relative permittivity)
  conductivity=0.005	# Earth Conductivity (Siemens per meter)
  bending=301.000	      # Atmospheric Bending Constant (N-Units)
  climate=3		      # Radio Climate
  
  #create_lrp $frequency $polarisation $maxERP $timePercentage $locationPercentage
  frequency=$1		# Frequency in MHz (20 MHz to 20 GHz)
  polarization=$2	# Polarization (0 = Horizontal, 1 = Vertical)
  maxERP=$(echo "scale=2; $3*1000" |bc) # Transmitter Effective Radiated Power in Watts (optional)
  timePercentage=$(echo "scale=3; $4/100" |bc)
  locationPercentage=$(echo "scale=3; $5/100" |bc)
   
  # Print out all known variables
  echo -e "$maxERP \t ; Transmitter Effective Radiated Power in Watts"
  echo -e "$dielectric\t ; Earth Dielectric Constant (Relative permittivity)"
  echo -e "$conductivity\t ; Earth Conductivity (Siemens per meter)"
  echo -e "$bending\t ; Atmospheric Bending Constant (N-Units)"
  echo -e "$frequency\t ; Frequency in MHz (20 MHz to 20 GHz)"
  echo -e "$climate \t ; Radio Climate"
  echo -e "$locationPercentage \t ; Fraction of situations"
  echo -e "$timePercentage \t ; Fraction of time"
  
  # Check the polarization of the antenna for the transmitter
  if [ "$polarization" == "VERT" ]; then
     echo -e "1 \t ; Polarization (0 = Horizontal, 1 = Vertical)"
  else # Horizontal
     echo -e "0 \t ; Polarization (0 = Horizontal, 1 = Vertical)"
  fi 
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create transmitter file (.qth)
create_qth(){
	# $TX_NAME $latitude $longitude $antennaHeight
    echo -e "$1\n$2\n$3\n$4meters"
}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extract antenna HAAT
antenna_haat(){

   awk -F"Antenna height above average terrain: " -v OFS="\t" '{print $2}' \
             | sed -ne 's/[^0-9]*\(\([0-9]\.\)[0-9][^.]\).*/\1/p'
}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run splat to calculate and extract HAAT
IFS="++" read -r -a TXarray <<< "$TXinfo"
for index in "${!TXarray[@]}"
do
    echo "$index ${TXarray[index]}"
done

recordNumber=${TXarray[0]}
countryCode=${TXarray[2]}
siteName=${TXarray[4]}
programme=${TXarray[6]}
#latitude=${TXarray[8]}
#longitude=${TXarray[10]}
polarisation=${TXarray[8]}
status=${TXarray[10]}
frequency=${TXarray[12]}
channel=${TXarray[14]}
maxERP=${TXarray[16]}
#antennaHeight=${TXarray[22]}
timePercentage=${TXarray[18]}
locationPercentage=${TXarray[20]}

TX_NAME=$siteName$recordNumber$countryCod

# Create transmitter (.qth) file
TX_qth_LON=$(echo $longitude*-1 | bc)
create_qth $TX_NAME $latitude $TX_qth_LON $antennaHeight > $rdir"$TX_NAME.qth"

# Longley-Rice model parameter (.lrp) file 
create_lrp $frequency $polarisation $maxERP $timePercentage $locationPercentage > $rdir"$TX_NAME.lrp"

# -------------------- Point to Area Splat analysis --------------------------
cd $rdir # enter subdirectory
splat -t $rdir"$TX_NAME.qth" -d $terrian -c 10 -ngs -sc -plo -m 1.333 -kml -metric  

# -------------------------------- Extract HAAT ------------------------------
HAAT=$(cat "$TX_NAME-site_report.txt" | antenna_haat)
cd .. # exit subdirectory

# ------------------------ Save results ino a file ------------------------ 
if [ -z "$HAAT" ];
then
  echo -e "$antennaHeight"
else
  echo -e "$HAAT" 
fi
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~