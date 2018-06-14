#!/bin/bash

declare -A DICT

get_dictionary (){
 #===============================================================================
 # The function calls readfrom.sh for Doctionary KEYS and VALUES
 # and  the  KEY  and VALUES characters are  first stored in independent arrays
 # a globally accessible Dictionary made of indexable array DICT is then populated
 #===============================================================================
  mapfile -t lines < intext.txt.py 

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

# call data operators depending on chosen operation
case ${DICT[OPERATIONS]} in

	SelectMerge | select_merge | selectmerge )

                 #Input variables for the select and merge module
                 DIR_arr=($(echo ${DICT[DATADIRECTORIES]} | tr ";" " "))
		 PAR_arr=($(echo ${DICT[PARAMRTER]} | tr ";" " "))
                 DIR_PATH=$(echo ${DICT[PATHTODIRECTORY]})
                 DIR_OUT=$(echo ${DICT[OUTPUTFILE]})
                 DIR_OUTSUB=$(echo ${DICT[LOWESTDIRECTORY]})

	         echo "The parameter(s) ${PAR_arr[@]} will be extracted from multiple files and merged into the respective single file(s)"
		 echo "data in the file(s):  ${DIR_arr[@]} will be processed and saved IN file 'INPUT' within the given path"
                 read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
                 echo ${DIR_arr[@]}

                 # test case files 
                 PATH="/home/mohau/Documents/Data-processing-pile-line/DATA"
                 FILES=( "ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45" )
	         PARAM=( "fg" "fg_ave" "epot_ave" "eg_ave" "epan" "fnee_ave" "fpn_ave" ) 

		# test for similarity between text file inputs and hard codes  inputs
                #[ "$DIR_PATH" == "$PATH" ] && echo "paths are equal" || echo "paths are distinct"]

                #[ "${DIR_arr[*]}" == "${FILES[*]}" ] && echo "dir are equal" || echo "dir are distinct"

	        #[ "${PAR_arr[*]}" == "${PARAM[*]}" ] && echo "params are equal" || echo "parms are distinct"
               
                #[ "$DIR_PATH" == "$PATH" ] && echo "paths are equal" || echo "paths are distinct"]

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
       AverageTemporally)

                 echo "temporal averaging is selected "
                 DIR_arr=($(echo ${DICT[DATADIRECTORIES]} | tr ";" " "))
		 PAR_arr=($(echo ${DICT[PARAMRTER]} | tr ";" " "))
                 DIR_PATH=$(echo ${DICT[PATHTODIRECTORY]})
                 DIR_OUT=$(echo ${DICT[OUTPUTFILE]})
                 DIR_OUTSUB=$(echo ${DICT[LOWESTDIRECTORY]})

                 echo "The parameter(s) ${PAR_arr[@]} will be extracted from multiple files and merged into the respective single file(s)"
                 echo "data in the file(s):  ${DIR_arr[@]} will be processed and saved IN file 'INPUT' within the given path"
                 read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
                
                source ./dotimeaverage.sh
 
                time_average "DIR_arr[@]" "PAR_arr[@]" "$DIR_PATH" "$DIR_OUT" "$DIR_OUTSUB"
               
                ;;
	*)
		echo "Sorry, please check the consistency of inputs with prescribed standard"
		;;
  esac
