#!/bin/bash
# Make a php copy of any html files

# top directory where input  and ouput netcdf files are saved
#PATH="/home/mohau/Documents/Data-processing-pile-line/DATASIXH" # To foulder

#PATH="/home/mohau/Documents/Data-processing-pile-line/DATA"    # To foulder

#models whose netcdf files are to be processes: note model name is extractable from the input file names
#FILES=( "ACC" "CCS" "CNR" "GFD" "MPI" "NOR" ) 

#FILES=( "ACC85" "CCS85" "CNR85" "GFD85" "MPI85" "NOR85" ) 

#parameters of interest. Assumption each input netcdf file  host all of the parameters
#PARAM=( "fg" "fg_ave" "eg_ave" "epan" )

#PARAM=( "epan" "rnd24" )

#REG_NAME="Afri"

#ORIG_TSCALE="sixhourly"
#ORIG_TSCALE="DAILY"

#OUTFILE="outfile"
#OUTFILESUB="FLUX"

#STARTDATE=2035-01-01T06:00:00
#ENDDATE=2035-12-31T00:00:00

#STARTDATE=2035-01-01T00:00:00
#ENDDATE=2035-12-31T00:00:00

#OUTSTAT_TEMPSCALE="dd_SUM_mm_MYMEAN_STAT"

#KEYSTAT_STEPS="NA"


doPredefTSpanStats(){

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

    declare -A hhSTAT_arr=(["hhMEAN"]="hourmean" ["hhSUM"]="hoursum" ["hhMAX"]="hourmax" ["hhMIN"]="hourmin" ["hhRNG"]="hhrange" ["hhSTD"]="hourstd" ["hhSTD1"]="hourstd1" ["hhVAR"]="hourvar" ["hhVAR"]="hourvar1")
    declare -A hhMYSTAT_arr=(["hhMYMEAN"]="yhourmean" ["hhMYSUM"]="yhoursum" ["hhMYMAX"]="yhourmax" ["hhMYMIN"]="yhourmin" ["hhMYRNG"]="yhourrange" ["hhMYSTD"]="yhourstd" ["hhMYSTD1"]="yhourstd1" ["hhMYVAR"]="yhourvar" ["hhMYVAR"]="yhourvar1")
    declare -A ddSTAT_arr=(["ddMEAN"]="daymean" ["ddAVE"]="dayave" ["ddSUM"]="daysum" ["ddMAX"]="daymax" ["ddMIN"]="daymin" ["ddRNG"]="dayrange" ["ddSTD"]="daystd" ["ddSTD1"]="daystd1" ["ddVAR"]="dayvar" ["ddVAR1"]="dayvar1")
    declare -A ddMYSTAT_arr=(["ddMYMEAN"]="ydaymean" ["ddMYSUM"]="ydaysum" ["ddMYMIN"]="ydaymin" ["ddMYMAX"]="ydaymax" ["ddMYAVE"]="ydayave" ["ddMYRNG"]="ydayrange" ["ddMYSTD"]="ydaystd" ["ddMYSTD1"]="ydaystd1" ["ddMYVAR"]="ydayvar" ["ddMYVAR1"]="ydayvar1")

    declare -A mmSTAT_arr=(["mmMEAN"]="monmean" ["mmSUM"]="monsum" ["mmMAX"]="monmax" ["mmMIN"]="monmin" ["mmRNG"]="monrange" ["mmSTD"]="monstd" ["mmSTD1"]="monstd1" ["mmVAR"]="monvar" ["mmVAR"]="monvar1")
    declare -A mmMYSTAT_arr=(["mmMYMEAN"]="ymonmean" ["mmMYSUM"]="ymonsum" ["mmMYMIN"]="ymonmin" ["mmMYMAX"]="ymonmax" ["mmMYAVE"]="ymonave" ["mmMYRNG"]="ymonrange" ["mmMYSTD"]="ymonstd" ["mmMYSTD1"]="ymonstd1" ["mmMYVAR"]="ymonvar" ["mmMYVAR1"]="ymonvar1") 

    declare -A ssSTAT_arr=(["ssMEAN"]="seasmean" ["ssSUM"]="seassum" ["ssMAX"]="seasmax" ["ssMIN"]="seasmin" ["ssRNG"]="seasrange" ["ssSTD"]="seasstd" ["ssSTD1"]="seasstd1" ["ssVAR"]="seasvar" ["ssVAR"]="seasvar1")
	       
    declare -A ssMYSTAT_arr=(["ssMYMEAN"]="yseasmean" ["ssMYSUM"]="yseassum" ["ssMYMAX"]="yseasmax" ["ssMYMIN"]="yseasmin" ["ssMYRNG"]="yseasrange" ["ssMYSTD"]="yseasstd" ["ssMYSTD1"]="yseasstd1" ["ssMYVAR"]="yseasvar" ["ssMYVAR"]="yseasvar1")
	 
    declare -A yySTAT_arr=(["yyMEAN"]="yearmean" ["yySUM"]="yearsum" ["yyMAX"]="yearmax" ["yyMIN"]="yearmin" ["yyRNG"]="yearrange" ["yySTD"]="yearstd" ["yySTD1"]="yearstd1" ["yyVAR"]="yearvar" ["yyVAR"]="yearvar1")


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

            #store the list of files in the directory in a list
	FILES_lst=$(/bin/ls)
	# echo $FILES_lst

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

                # perform the operation on list of NetCDF files in each directory on the list
                for i in ${FILES_lst}
	      do
                    # echo $i
	        INF=$i
                    IFS='.' read -ra ADDR <<< "$INF"

                    FILENAME=${ADDR[0]}
                    EXT=${ADDR[1]}
			
	        INF=$i
	        IFS='-' read -ra ADDR <<< $FILENAME

	        PAR_NAME=${ADDR[0]}
                    echo $FILENAME
                    echo $PAR_NAME
		         		         
                    temp2=$PAR_NAME"-"$REG_NAME"-"$file"-"$OUTSTAT_TEMPSCALE".nc"

                    OutFIle=$PAR_NAME"-"$REG_NAME"-"$file"-"$OUTSTAT_TEMPSCALE"-"$STT_DATE"-"$END_DATE".nc"

                    /usr/bin/cdo -seldate,$STT_DATE,$END_DATE $i $temp2

		         
                    echo  "started from $ORIG_TSCALE time scale"
                    echo "****************cdo: getting dailly mean of $PAR_NAME from $ORIG_TSCALE data in $i*****************************"

                    if [[ ( "$ORIG_TSCALE" == "hourly" ) || ( "$ORIG_TSCALE" == "sixhourly" ) ]];
                      then
	            case $STAT_TSCALE in hh_STAT)

		  /usr/bin/cdo -b 64 -shifttime,1sec -${hhSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle
                        ;; hh_MYSTAT )

		  /usr/bin/cdo -b 64 -shifttime,1sec -${hhMYSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle
		                    
		;; dd_STAT )

		  /usr/bin/cdo -b 64 shifttime,1sec -${ddSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle

		;; dd_MYSTAT )

		  /usr/bin/cdo -b 64 shifttime,1sec -${ddMYSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle

		;; mm_STAT )
		
	              /usr/bin/cdo -b 64 shifttime,1sec -${mmSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle

		;; mm_MYSTAT )
		
	              /usr/bin/cdo -b 64 shifttime,1sec -${mmMYSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle

		;; ss_STAT )
                    
                          /usr/bin/cdo -b 64 shifttime,1sec -${ssSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle
						
		;; ss_MYSTAT )
       
                          /usr/bin/cdo -b 64 shifttime,1sec -${mmMYSTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle
		
                        ;; yy_STAT )

		  /usr/bin/cdo -b 64 shifttime,1sec -${yySTAT_arr[$STAT_STEPS]} -shifttime,-1sec $temp2 $OutFIle
                                            
		;; dd_SUM_mm_MEAN_STAT )	
		
	              /usr/bin/cdo -b 64 monmean -shifttime,1sec -daysum -shifttime,-1sec $temp2 $OutFIle

                        ;; dd_SUM_mm_MYMEAN_STAT )
	
	              /usr/bin/cdo -b 64 ymonmean -shifttime,1sec -monsum -shifttime,-1sec $temp2 $OutFIle
	                 
	            ;; mm_SUM_yy_MEAN_STAT )
	
	              /usr/bin/cdo -b 64 -yearmean -shifttime,1sec -monsum -shifttime,-1sec $temp2 $OutFIle

		;; mm_SUM_mm_MYMEAN_STAT )
		
	             /usr/bin/cdo -b 64 ymonmean -shifttime,1sec -monsum -shifttime,-1sec $temp2 $OutFIle
                        ;; mm_SUM_yy_MEAN_STAT )

                         /usr/bin/cdo -b 64 yearmean -shifttime,1sec -daysum -shifttime,-1sec $temp2 $OutFIle


	           esac

	        elif [[ ("$ORIG_TSCALE" == "daily")||("$ORIG_TSCALE" == "DAILY") ]];
	          then
	            case $STAT_TSCALE in mm_STAT )
			                	
	              /usr/bin/cdo -b 64 -${mmSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; mm_STAT )
			              
		  /usr/bin/cdo -b 64 -${mmSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; mm_MYSTAT )
			              
	              /usr/bin/cdo -b 64 -${mmMYSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; ss_STAT )
	              
                          /usr/bin/cdo -b 64 -${ssSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; ss_MYSTAT )
			              
	              /usr/bin/cdo -b 64 -${ssMYSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; ss_STAT )
			              
	              /usr/bin/cdo -b 64 -${ssSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

		;; yy_MYSTAT )
			              
	              /usr/bin/cdo -b 64 -${yyMYSTAT_arr[$STAT_STEPS]} $temp2 $OutFIle

                        ;; dd_SUM_mm_MEAN_STAT )
			                	
	              /usr/bin/cdo -b 64 -monmean -daysum $temp2 $OutFIle
                        
                        ;; dd_SUM_mm_MYMEAN_STAT )
			                	
	              /usr/bin/cdo -b 64 -ymonmean -daysum $temp2 $OutFIle

                        ;; mm_SUM_yy_MEAN_STAT )
			                	
	              /usr/bin/cdo -b 64 -yearmean -monsum $temp2 $OutFIle

		;; mm_SUM_mm_MYMEAN_STAT )
			                	
	              /usr/bin/cdo -b 64 -ymonmean -monsum $temp2 $OutFIle
		
			              
	            ;; mm_SUM_yy_MEAN_STAT )
			                
	              /usr/bin/cdo -b 64 -yearmean -monsum $temp2 $OutFIle
			            
                        esac

	      else

                    echo "Not ok"

            fi

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
#doPredefTSpanStats "FILES[@]" "PARAM[@]" "$PATH" "$OUTFILE" "$OUTFILESUB" "$STARTDATE" "$ENDDATE" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS"


