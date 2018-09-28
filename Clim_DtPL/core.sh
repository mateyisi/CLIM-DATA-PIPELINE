#!/bin/bash

declare -A DICT

get_dictionary (){
 #===============================================================================
 # The function calls readfrom.sh for Doctionary KEYS and VALUES
 # and  the  KEY  and VALUES characters are  first stored in independent arrays
 # a globally accessible Dictionary made of indexable array DICT is then populated
 #===============================================================================
  #mapfile -t lines < intext.txt.py #Hand made
  mapfile -t lines < intext.txt     #gui made

  source ./dictionary.sh 

  KEYS=$(make_dictionary 0 ${lines[@]}) # array of keys from input text file

  VALUES=$(make_dictionary 1 ${lines[@]}) # array of specification  for all keys

  KEYS_arr=( $(echo $KEYS | tr " " " ") ) 

  VALUES_arr=( $(echo $VALUES | tr " " " ") )
  
 

  for i in ${!KEYS_arr[@]}; do

    DICT[${KEYS_arr[$i]}]=${VALUES_arr[$i]} 

  done

}

#=============================MAIN================================================
# Main body of the code where source scripts of CDO operatores are called and
# corresponding arguments are passed for each operation case.
#=================================================================================

get_dictionary

#Input variables all compund operators
DIR_arr=($(echo ${DICT[DATADIRECTORIES]} | tr ";" " "))
PAR_arr=($(echo ${DICT[PARAMRTER]} | tr ";" " "))
DIR_PATH=$(echo ${DICT[PATHTODIRECTORY]})
DIR_OUT=$(echo ${DICT[OUTPUTFILE]})
DIR_OUTSUB=$(echo ${DICT[LOWESTDIRECTORY]})
TIMEPERIOD=($(echo ${DICT[TIMEINTERVAL]} | tr ";" " "))
REG_NAME=$(echo ${DICT[REGIONNAME]}) 
ORIG_TSCALE=$(echo ${DICT[STARTINGTIMESCALE]})
OUTSTAT_TEMPSCALE=$(echo ${DICT[OPERATIONTSCALE]})
KEYSTAT_STEPS=$(echo ${DICT[OPERATOR]})
TIMESTEPS=$(echo ${DICT[TIMESTEPS]})
FILING_STYLE=$(echo ${DICT[INPUTFILINGSTYLE]})

COMPOUND_OPERATOR=$(echo ${DICT[COMPOUNDOPERATOR]})

PCNTL=$(echo ${DICT[PCTL]})
NSETS=$(echo ${DICT[NSETS]})
OFFSETN=$(echo ${DICT[NOFFSET]})


echo "The parameter(s) ${PAR_arr[@]} will be processed"
echo "data in the file(s):  ${DIR_arr[@]} will be processed and saved IN file 'INPUT' within the given path"
#read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
# call data operators depending on chosen operation
case $COMPOUND_OPERATOR in SelectMerge | select_merge | selectmerge )
  
  # extrect input paramter from multiples netcdf files into a single netcdf files
  source ./extractparameter.sh 
 
  # run with hardcoded text inputs
  # select_parameter "FILES[@]" "PARAM[@]" "$PATH" "$DIR_OUT" "$DIR_OUTSUB"
  # run with inputs from text file
  echo "************************************************" 
  select_parameter "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB"
;;
AverageSpatially | averagespatially | AVERAGESPATIALLY |average_spatially)

  echo "Spatial averaging is selected "
		
  ;;

 PredefTSpanSTATS )

   case $FILING_STYLE in INH )
           
     echo "*********************"
                
     source ./PredefTSpan_STATS_INH.sh

     doPredefTSpanStats "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS"

     ;;
                  
    CDX )

      source ./PredefTSpan_STATS_CDX.sh
      doPredefTSpanStats "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS"

                       
      ;;
               
      esac

    ;;
    
    PredefTSpanPCTL )

      case $FILING_STYLE in INH )
           
         echo "*********************"
                
         source ./PredefTSpan_PCTL_INH.sh

         doPredefTSpan_PCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$PCNTL"
      ;;
                  
      CDX )

         source ./PredefTSpan_PCTL_CDX.sh

         doPredefTSpan_PCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$PCNTL"

      ;;
               
      esac

    ;;

    PredefTSpanRunnPCTL )
                      
              
      case $FILING_STYLE in INH )
                
        source ./PredefTSpan_RunnPCTL_INH.sh 

        doPredefTSpanRunnPCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$TIMESTEPS" "$PCNTL"
                
                                       
      ;;
                  
      CDX )

        source ./PredefTSpan_RunnPCTL_CDX.sh

        doPredefTSpanRunnPCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$TIMESTEPS" "$PCNTL"

      esac

    ;;

    PredefTSpanRunnSTATS )

      case $FILING_STYLE in INH )
                
        source ./PredefTSpan_RunnSTATS_INH.sh 

        doPredefTSpanRunnSTATS "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$TIMESTEPS" 
                                         
      ;;
      CDX )

        source ./PredefTSpan_RunnSTATS_CDX.sh

        doPredefTSpanRunnSTATS "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$TIMESTEPS"
    
       esac

   ;;

   SelTSpanSTATS )
                      
     case $FILING_STYLE in INH )
                
       source ./SelTSpan_STATS_INH.sh

       doSelTSpanStats "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$NSETS" "$OFFSETN" 
                
     ;;
                  
     CDX )

       source ./SelTSpan_STATS_CDX.sh

       doSelTSpanStats "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$NSETS" "$OFFSETN"
    
       esac

   ;;

   SelTSpanPCTL )
                      
     case $FILING_STYLE in INH )
                
       source ./SelTSpan_PCTL_INH.sh

       doSelTSpanPCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$NSETS" "$OFFSETN" "$PNCTL" 
  
     ;;
     CDX )

       source ./SelTSpan_PCTL_CDX.sh

       doSelTSpanPCTL "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB" "${TIMEPERIOD[0]}" "${TIMEPERIOD[1]}" "$REG_NAME" "$ORIG_TSCALE" "$OUTSTAT_TEMPSCALE" "$KEYSTAT_STEPS" "$NSETS" "$OFFSETN" "$PNCTL"
    
     esac

   ;;
   esac
