#!/bin/bash
# Make a php copy of any html files

# top directory where input  and ouput netcdf files are saved
PATH="/home/mohau/Documents/Data-processing-pile-line/DATA" # To foulder
#models whose netcdf files are to be processes: note model name is extractable from the input file names
FILES=( "ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45" ) 
#parameters of interest. Assumption each input netcdf file  host all of the parameters
PARAM=( "fg" "fg_ave" "epot_ave" "eg_ave" "epan" "fnee_ave" "fpn_ave" )

OUTFILE="outfile"

OUTFILESUB="FLUX"

time_average(){

#create array for user inputs. $FILES and $PAREAM and $PATH  given for testing
DIR_arr=("${!1}")
PAR_arr=("${!2}")
DIR_PATH=$3
OUT_FILE=$4
OUT_FILESUB=$5

cd $DIR_PATH #enter main directory

#create the given output file if it does not exist
if [ ! -d $OUT_FILE ]; then
  /bin/mkdir $OUT_FILE
  cd $OUT_FILE
  /bin/mkdir $OUT_FILESUB
  cd ../
fi
#list files in the working main derectory
foldernames=$( '/bin/ls' )

 for file in $foldernames 
  do
     #check a file is of type dictory
    if [ -d $DIR_PATH/$file/ ];       
      then  
      #enter two lavel subdirectories director 
      cd $file/FLUX/                   

      #Extract model name from the file name
      IN=$file
      IFS='_' read -ra ADDR <<< "$IN"
      model=${ADDR[0]}

      echo $model
      echo $file

     #check that user input model is also in the folders at the working directory

     if [[ " ${DIR_arr[@]} " == *"$model"* ]];
        then

           for i in "${PAR_arr[@]}"
  	     	do 
    	     	 # echo "extracting $i timeseries from $file "
                 # call cdo operators for parameter selection and merging files to form a time series.
 
                  /usr/bin/cdo -select,name=$i *.nc $i"_"$file"_SIXHOURLY.nc"
     	          #cdo -seasmean -settaxis,2035-01-01,00:00:00,1month -monmean -shifttime,1sec -daymean -shifttime,-1sec $i-SIXHOURLY.nc $PATH$file/FLUX/$file/FLUX/SEASNAL/"ccam_$model-RCP45-$i-SEASAV-203501_209912-.nc"
                  /usr/bin/cdo monmean -shifttime,1sec -daymean -shifttime,-1sec $i"_"$file"_SIXHOURLY.nc" $i"_"$file"_monthly.nc"

     	          /bin/rm *_SIXHOURLY.nc

                  /bin/mv *monthly.nc $DIR_PATH/$OUT_FILE/$OUT_FILESUB
           done
     fi
   fi
   cd ../.. #exit the two level subdirectory
 done

}

#uncomment for stand alone testing
#time_average "FILES[@]" "PARAM[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" 

