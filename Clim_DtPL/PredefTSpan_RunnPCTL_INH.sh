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

#OUTSTAT_TEMPSCALE="hh_RUNPCTL"

#KEYSTAT_STEPS="RUNPCTL"

#TIMESTEPS=5

#PCNT=90

#STARTDATE=2035-01-01T06:00:00
#ENDDATE=2035-12-31T00:00:00

#STARTDATE=1970-01-01T06:00:00
#ENDDATE=1972-12-31T00:00:00

doPredefTSpanRunnPCTL(){

 #create array for user inputs. $FILES and $PAREAM and $PATH  given for testing
 DIR_arr=("${!1}")
 PAR_arr=("${!2}")
 DIR_PATH=$3
 OUT_FILE=$4
 OUT_FILESUB=$5
 STT_DATE=$6
 END_DATE=$7
 REG_NAME=$8 
 ORIG_TSCALE=${9}
 STAT_TSCALE=${10}
 STAT_STEPS=${11}
 ddT_STEPS=${12}
 PERCENT=${13}

 declare -A ddMYRUNPCTLs_arr=( ["ddMYRUNPCTL"]="ydrunpctl" )
 declare -A ddMYRUNMIN_arr=( ["ddMYRUNPCTL"]="ydrunmin" )
 declare -A ddMYRUNMAX_arr=( ["ddMYRUNPCTL"]="ydrunmax" )

 declare -A RUNPCTLs_arr=( ["RUNPCTL"]="runpctl" )
  
 cd $DIR_PATH #enter main directory

 #create the given output file if it does not exist
 if [ ! -d $OUT_FILE ]; then
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
 
	       if [[ ( "$ORIG_TSCALE" == "dailly" ) && ("$STAT_TSCALE" == "dd_RUNMYPCTL") ]];
                     then                            

                       /usr/bin/cdo -b 64 -${ddMYRUNPCTLs_arr[$STAT_STEPS]},$PERCENT,$ddT_STEPS $temp2 -${MYRUNMIN_arr[$STAT_STEPS]} $temp2 -${MYRUNMAX_arr[$STAT_STEPS]} $temp2 $OutFIle
                             
                   else

                     case $STAT_TSCALE in hh_RUN_PCTL | dd_RUN_PCTL | mm_RUN_PCTL | ss_RUN_PCTL | yy_RUN_PCTL )

                       /usr/bin/cdo -b 64 -${RUNPCTLs_arr[$STAT_STEPS]},$PERCENT,$ddT_STEPS $temp2 $OutFIle
                          
                     esac

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
#doPredefTSpanRunnPCTL "FILES[@]" "PARAM[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" "$STARTDATE" "$ENDDATE" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$TIMESTEPS" "$PCNT" 
	
		
