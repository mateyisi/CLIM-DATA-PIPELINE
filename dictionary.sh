#!/bin/bash

#mapfile -t lines < intext.txt.py 

make_dictionary(){

 
 declare -A CleanLines 
 #shift
 declare -A DICT # Dictionary of KEY and SPECIFICATIONS 
 #shift
 local ar_ind=$1


  # Standardize the input by removing  commented lines and
  # white spaces
  for((i=0; i< ${#lines[@]}; ++i))
    do
     case ${lines[$i]} in

       ''|\#*) continue ;;         # skip blank lines and lines starting with #

     esac

     # remove tabs or white spaces
     CleanLine=(`echo ${lines[$i]} | sed 's/[[:space:]]//g'`) 

     CleanLines[$i]=$CleanLine

   done

    #make separate lists KEY $ specifications

    for i in ${CleanLines[@]} 
     do
       # echo $i

       arr=( $(echo $i | tr "\$" " ") ) #KEY SPESIFICATIONS ARRAY

       DICT[${arr[0]}]=${arr[1]}         # IMPLIMENT DICTIONARY

     done

    # echo ${SPECS[@]}

     KEYS=(${!DICT[@]})
     SPECS=(${DICT[@]})

    # echo ${SPECS[@]}
    # echo ${KEYS[@]} 

     if [ $ar_ind -eq 0 ]
     then

       echo ${KEYS[@]}         # skip blank lines and lines starting with #

     else [ $ar_ind -eq 1 ]
 
       echo ${SPECS[@]}         # skip blank lines and lines starting with #
     fi


  }


#make_dictionary 0 ${lines[@]}


