#!/bin/bash
# Make a php copy of any html files

# top directory where input  and ouput netcdf files are saved
#PATH="/home/mohau/Documents/Data-processing-pile-line/DATASIXH" # To foulder

#PATH="/home/mohau/Documents/Data-processing-pile-line/DATA" # To foulder

#models whose netcdf files are to be processes: note model name is extractable from the input file names
#FILES=( "ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45" ) 

#FILES=( "ACC85" "CCS85" "CNR85" "GFD85" "MPI85" "NOR85" ) 

#FILES=( "ACC" "CCS" "CNR" "GFD" "MPI" "NOR" ) 

#parameters of interest. Assumption each input netcdf file  host all of the parameters
#PARAM=( "fg" "fg_ave" "epot_ave" "eg_ave" "epan" "fnee_ave" "fpn_ave" )

#PARAM=( "eg_ave" )

#REG_NAME="Afri"

#ORIG_TSCALE="sixhourly"

#OUTFILE="outfile"

#OUTFILESUB="FLUX"

#OUTSTAT_TEMPSCALE="mm_SELTIME"

#KEYSTAT_STEPS="sltspSUM"

#NSETS=30

#NOFFSEt=60

#STARTDATE=2035-01-01T06:00:00
#ENDDATE=2035-12-31T00:00:00

#STARTDATE=1970-01-01T06:00:00
#ENDDATE=1972-12-31T00:00:00

doSelTSpanStats(){

  #create array for user inputs. $FILES and $PAREAM and $PATH  given for testing
  DIR_arr=("${!1}")
  PAR_arr=("${!2}")
  DIR_PATH=$3
  OUT_FILE=$4
  OUT_FILESUB=$5
  STT_DATE=$6
  END_DATE=$7
  REG_NAME=$8 
  ORIG_TSCALE=$9
  STAT_TSCALE=${10}
  STAT_STEPS=${11}
  N_SETS=${12}
  N_OFFSET=${13}
       
  declare -A stsSTAT_arr=( ["sltspMEAN"]="timselmean" ["sltspSUM"]="timselsum" ["sltspMAX"]="timselmax" ["sltspMIN"]="timselmin" ["sltspRNG"]="timselrange" ["sltspSTD"]="timselstd" ["sltspSTD1"]="timselstd1" ["sltspVAR"]="timselvar" ["sltspVAR"]="timselvar1")

  cd $DIR_PATH #enter main directory

  #create the given output file if it does not exist
  if [ ! -d $OUT_FILE ]; 
    then
      /bin/mkdir $OUT_FILE
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
	  then 
	    /bin/mkdir $file
	    cd $file
	    /bin/mkdir $OUT_FILESUB
	    cd ../
	fi
	
	for i in "${PAR_arr[@]}"
	  do
	    echo "*************extracting $i timeseries from $file****************************"

	    temp1=$REG_NAME"-"$i"-"$file"-"$ORIG_TSCALE".nc"
	    temp2=$REG_NAME"-"$i"-"$file"-"$AGGR_T0".nc"
	    OutFIle=$REG_NAME"-"$i"-"$file"-"$STAT_STEPS"-"$STT_DATE"-"$END_DATE".nc"

	    /usr/bin/cdo -select,name=$i *.nc $temp1
	    /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $temp1 $temp2

	    echo "started from $ORIG_TSCALE time scale"
                echo "****cdo: getting dailly $STAT_STEPS of $i from $ORIG_TSCALE data in $file***************"
                        
                if [[ ( "$ORIG_TSCALE" == "hourly" ) || ( "$ORIG_TSCALE" == "sixhourly" ) ]];
	      then
                  echo $STAT_TSCALE
	                	                    
                    /usr/bin/cdo -b 64 -shifttime,1sec -${stsSTAT_arr[$STAT_STEPS]},$N_SETS,$N_OFFSET -shifttime,-1sec $temp2 $OutFIle
                               
                  else

                    /usr/bin/cdo -b 64 -${stsSTAT_arr[$STAT_STEPS]},$N_SETS,$N_OFFSET $temp2 $OutFIle

                    echo $STAT_STEPS

                 fi
                                                           
	     /bin/rm $temp1
	     /bin/rm $temp2
	              
                 #move output to the  output directory
	     /bin/mv $OutFIle $file/$OUT_FILESUB
	          
	 done
	 
             # move output directory to the top common ouput directory
	 /bin/mv $DIR_PATH/$file/$OUT_FILESUB/$file $DIR_PATH/$OUT_FILE/$OUT_FILESUB

           fi

       fi
       cd ../.. #exit the two level subdirectory
   done

}
	
#uncomment for stand alone testing
#doSelTSpanStats "FILES[@]" "PARAM[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" "$STARTDATE" "$ENDDATE" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$NSETS" "$NOFFSET"
	
		
