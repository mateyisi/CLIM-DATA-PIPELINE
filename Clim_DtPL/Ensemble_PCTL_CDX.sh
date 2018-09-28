#!/bin/bash

# top directory where input  and ouput netcdf files are saved
PATH="/home/mohau/Documents/Data-processing-pile-line/PCNTL-2035-2099" # To foulder
#models whose netcdf files are to be processes: note model name is extractable from the input file names
FILES=( "eg_ave-RCP45-10-ENS_PCNTL" "eg_ave-RCP45-50-ENS_PCNTL" "eg_ave-RCP45-90-ENS_PCNTL" ) 

OUTFILE="outfile"
OUTFILESUB="FLUX"

REG_NAME="Afri"

#STARTDATE='NA'
#ENDDATE='NA'
STARTDATE=2035-05-16T12:00:00
ENDDATE=2041-05-16T12:00:00

select_parameter(){

#create array for user inputs: $FILES and $PATH  given for testing
DIR_arr=("${!1}")
DIR_PATH=$2
OUT_FILE=$3
OUT_FILESUB=$4
REG_NAME=$5 

STAT_STEPS=$6
STT_DATE=$7
END_DATE=$8

cd $DIR_PATH #enter main directory

#create the given output file if it does not exist
if [ ! -d $OUT_FILE ]; then
  /bin/mkdir $OUT_FILE
  cd $OUT_FILE
  /bin/mkdir $OUT_FILESUB
  cd ../
fi
#list files in the working main derectory
filenames=$( '/bin/ls' )

 for file in $filenames 
  do
    if [ -d $DIR_PATH/$file/ ];        #check a file is of type dictory
      then   
      cd $file/FLUX/                   #enter two lavel subdirectories

      #Extract model name from the file name
      IN=$file
      IFS='-' read -ra ADDR <<< "$IN"
      PAR=${ADDR[0]}
      SCENARIO=${ADDR[1]}
      PERCENT=${ADDR[2]}
      echo "=================================================="
      echo "Succesfully Processed: $PERCENT the ensemble percentile"
      echo "In derectory:" $file

     #check that user input model is also in the folders at the working directory

     if [[ " ${DIR_arr[@]} " == *"$file"* ]];
        then
           # make directory for storing outputs if dies not exist
           if [[ ! -d $file ]];
             then 
               /bin/mkdir $file
               cd $file
               /bin/mkdir $OUT_FILESUB
               cd ../
              
               OutFIle=$REG_NAME"-"$PAR"-"$SCENARIO"-"$PERCENT"th-"$STT_DATE"-"$END_DATE".nc"
               temp2=$REG_NAME"-"$PAR"-"$SCENARIO".nc"
               echo "The output is: "$OutFIle
              
               
               case ${#STT_DATE} in 2)
                

                 /usr/bin/cdo enspctl,$PERCENT *.nc $OutFIle

                 echo ${#STT_DATE}
  
               ;; 19 )
               
            
               /usr/bin/cdo enspctl,$PERCENT *.nc $temp2
               /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $temp2 $OutFIle
               /bin/rm $temp2
              

              ;; esac 
  
              /bin/mv $OutFIle $file/$OUT_FILESUB
              /bin/mv $DIR_PATH/$file/$OUT_FILESUB/$file $DIR_PATH/$OUT_FILE/$OUT_FILESUB
                 
             
           fi
      fi

   fi
   cd ../.. #exit the two level subdirectory
 done

}

#uncomment for stand alone testing
select_parameter "FILES[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" "$REG_NAME" "$KEYSTAT_STEPS" "$STARTDATE" "$ENDDATE"



