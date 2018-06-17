#!/bin/bash
# Make a php copy of any html files

# top directory where input  and ouput netcdf files are saved
PATH="/home/mohau/Documents/Data-processing-pile-line/DATA" # To foulder
#models whose netcdf files are to be processes: note model name is extractable from the input file names
FILES=( "ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45" ) 
#parameters of interest. Assumption each input netcdf file  host all of the parameters
PARAM=( "fg" "fg_ave" "epot_ave" "eg_ave" "epan" "fnee_ave" "fpn_ave" )

REG_NAME="Afri"

ORIG_TSCALE="sixhourly"

#AGGREGATETI="ddAVE_mmAVE_yyAVE"

#AGGREGATETI="ddSUM"
#AGGREGATETI="ddSUM_mmAVE"
AGGREGATETI="ddSUM_mmAVE_yyAVE"


OUTFILE="outfile"

OUTFILESUB="FLUX"

STARTDATE=2035-01-01T06:00:00
ENDDATE=2035-12-31T00:00:00



time_average(){

#create array for user inputs. $FILES and $PAREAM and $PATH  given for testing
DIR_arr=("${!1}")
PAR_arr=("${!2}")
DIR_PATH=$3
OUT_FILE=$4
OUT_FILESUB=$5
STT_DATE=$6
END_DATE=$7

REG_NAME=$8 

ORIG_TSCALE=${10}

AGGR_T0=$9


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
      cd $file/$OUT_FILESUB/

      #Extract model name from the file name
      IN=$file
      IFS='-' read -ra ADDR <<< "$IN"
      model=${ADDR[0]}

      echo $model
      echo $file

     #check that user input model is also in the folders at the working directory

     if [[ " ${DIR_arr[@]} " == *"$model"* ]];
        then
          # make directory for storing outputs if dies not exist
           if [[ ! -d $file ]];
               then /bin/mkdir $file
                    cd $file
                    /bin/mkdir $OUT_FILESUB
                   cd ../
           fi

           for i in "${PAR_arr[@]}"
  	     	do
    	     	 echo "*************extracting $i timeseries from $file****************************"
                
                 
                if [[ ( "$ORIG_TSCALE" == "hourly" ) || ( "$ORIG_TSCALE" == "sixhourly" ) ]];
                  then

                    
                     case $AGGR_T0 in
                              ddAVE )
                        cho  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting dailly mean of $i from $file****************************************"

                        /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                        /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
		        /usr/bin/cdo shifttime,1sec -daymean -shifttime,-1sec  $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
			/bin/rm *$ORIG_TSCALE".nc"
                        /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                        #move output to the  output directory
                        /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB
                       
			;; ddAVE_mmAVE )

                        echo  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting montly mean of $i from $file daily averages*************************"

                         /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                         /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         /usr/bin/cdo monmean -shifttime,1sec -daymean -shifttime,-1sec $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
                         /bin/rm *$ORIG_TSCALE".nc"
                         /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         #move output to the  output directory
                         /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB


	         	;; ddAVE_mmAVE_yyAVE )
                        
                        echo  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting montly mean of $i from $file daily averages*************************"

                         /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                         /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         /usr/bin/cdo yearmean -shifttime,1sec -daymean -shifttime,-1sec $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
                         /bin/rm *$ORIG_TSCALE".nc"
                         /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         #move output to the  output directory
                         /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB

                       ;; ddSUM )
                        cho  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting dailly sum of $i from $file******************************************"

                        /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                        /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                        /usr/bin/cdo shifttime,1sec -daysum -shifttime,-1sec  $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
                        /bin/rm *$ORIG_TSCALE".nc"
                        /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                        #move output to the  output directory
                        /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB

                        ;; ddSUM_mmAVE )

                        echo  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting montly mean of $i from $file daillyy sum*************************"

                         /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                         /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         /usr/bin/cdo monmean -shifttime,1sec -daysum -shifttime,-1sec $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
                         /bin/rm *$ORIG_TSCALE".nc"
                         /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         #move output to the  output directory
                         /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB


                        ;; ddSUM_mmAVE_yyAVE )

                        echo  "started from $ORIG_TSCALE time scale"
                        echo "****************cdo: getting monthly mean of $i from $file dailly sum***************************"

                         /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
                         /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         /usr/bin/cdo yearmean -shifttime,1sec -daysum -shifttime,-1sec $REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"
                         /bin/rm *$ORIG_TSCALE".nc"
                         /bin/rm *$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
                         #move output to the  output directory
                         /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB

                       ;;

                    esac

                 fi 
                 # call cdo operators for parameter selection and merging files to form a time series.

                 # /usr/bin/cdo -select,name=$i *.nc $REG_NAME"-"$i"-"$file"-SIXHOURLY.nc"
                 # /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $REG_NAME"-"$i"-"$file"-SIXHOURLY.nc" $REG_NAME"-"$i"-"$file"-SIXHOURLY-"$STT_DATE"-"$END_DATE".nc"
     	         # xcdo -seasmean -settaxis,2035-01-01,00:00:00,1month -monmean -shifttime,1sec -daymean -shifttime,-1sec $i-SIXHOURLY.nc $PATH$file/FLUX/$file/FLUX/SEASNAL/"ccam_$model-RCP45-$i-SEASAV-203501_209912-.nc"
                 # /usr/bin/cdo monmean -shifttime,1sec -daymean -shifttime,-1sec  $REG_NAME"-"$i"-"$file"-SIXHOURLY-"$STT_DATE"-"$END_DATE".nc" $REG_NAME"-"$i"-"$file"-"$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc"

     	         # /bin/rm *"SIXHOURLY.nc"
                 # /bin/rm *$REG_NAME"-"$i"-"$file"-SIXHOURLY-"$STT_DATE"-"$END_DATE".nc"

                  #move output to the  output directory
                 #  /bin/mv *$AGGR_T0"-"$STT_DATE"-"$END_DATE".nc" $file/$OUT_FILESUB
                  #/bin/mv *-monthly-$STT_DATE"-"$END_DATE".nc" $DIR_PATH/$OUT_FILE/$OUT_FILESUB
               
           done
           # move output directory to the top common ouput directory
           /bin/mv $DIR_PATH/$file/$OUT_FILESUB/$file $DIR_PATH/$OUT_FILE/$OUT_FILESUB
     fi
   fi
   cd ../.. #exit the two level subdirectory
 done

}

#uncomment for stand alone testing
time_average "FILES[@]" "PARAM[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" "$STARTDATE" "$ENDDATE" "$REG_NAME" "${AGGREGATETI}" "$ORIG_TSCALE"


