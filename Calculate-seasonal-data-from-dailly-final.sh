
#!/bin/bash
# Make a php copy of any html files

cd /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/


declare -a arrAV=("fg" "fg_ave" "epot_ave" "eg_ave" "epan" "fnee_ave" "fpn_ave")
declare -a arrSUM=("sunhours" "evap")


RCP45_FILES=("ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45")

RCP85_FILES=("ACC85" "CCS85" "CNR85" "GFD85" "MPI85" "NOR85")

foldernames=$(ls)

for file in $foldernames
 
 do
   echo $file
   if [ -d /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/ ];then   
      cd /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/
      
      #Extract model name from the file name
      IN=$file
      IFS='_' read -ra ADDR <<< "$IN"
      model=${ADDR[1]}
      
      #Calculate seasonal averages and sums with CDO for RCP4.5 scenario files
      if [[ " ${RCP45_FILES[*]} " == *"$model"* ]];
	then
           for i in "${arrAV[@]}"
  	     	do 
    	     	  echo "$i"
     	          cdo -select,name=$i *.nc $i-SIXHOURLY.nc
  
     	          cdo -seasmean -settaxis,2035-01-01,00:00:00,1month -monmean -shifttime,1sec -daymean -shifttime,-1sec $i-SIXHOURLY.nc /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/SEASNAL/"ccam_$model-RCP45-$i-SEASAV-203501_209912-.nc"

     	          rm $i-SIXHOURLY.nc
    
           done
           
        #Perform seasonal sumes with CDO for RCP4.5 scenario files
	   for i in "${arrSUM[@]}"
             	do 
             	  echo "$i"
     
             	  cdo -select,name=$i *.nc $i-SIXHOURLY.nc
             	  cdo -b 64 shifttime,1sec -daysum -shifttime,-1sec $i-SIXHOURLY.nc "temp-$i-DAILLY.nc"    
             	  cdo -seasmean -settaxis,2035-01-01,00:00:00,1month -monmean temp-$i-DAILLY.nc /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/SEASNAL/"ccam_$model-RCP45-$i-SEASSUM-203501_209912-.nc"
     
     
             	  rm $i-SIXHOURLY.nc
             	  rm temp-$i-DAILLY.nc   
           done

    	  
      fi
      #Calculate seasonal averages and sums with CDO for RCP4.5 scenario files
      if [[ " ${RCP85_FILES[*]} " == *"$model"* ]];
	then
        # process RCP8.5 paramters to be averaged
    	for i in "${arrAV[@]}"
  	     	do 
    	     	  echo "$i"
     	          cdo -select,name=$i *.nc $i-SIXHOURLY.nc
  
     	          cdo -seasmean -settaxis,1979-01-01,00:00:00,1month -monmean -shifttime,1sec -daymean -shifttime,-1sec $i-SIXHOURLY.nc /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/SEASNAL/"ccam_$model-RCP85-$i-SEASAV-197901_209912-.nc"

     	          rm $i-SIXHOURLY.nc
    
         done
         # process RCP8.5 paramters to be summed
         for i in "${arrSUM[@]}"
             	do 
             	  echo "$i"
     
             	  cdo -select,name=$i *.nc $i-SIXHOURLY.nc
             	  cdo -b 64 shifttime,1sec -daysum -shifttime,-1sec $i-SIXHOURLY.nc "temp-$i-DAILLY.nc"    
             	  cdo -seassum -settaxis,1979-01-01,00:00:00,1month -monsum temp-$i-DAILLY.nc /media/mohau/Seagate\ Backup\ Plus\ Drive/CCAM_JULY2017_DATA/$file/FLUX/SEASNAL/"ccam_$model-RCP85-$i-SEASSUM-197901_209912-.nc"
     
     
             	  rm $i-SIXHOURLY.nc
             	  rm temp-$i-DAILLY.nc   
           done
       
      fi   
  #else

  fi
  cd ../..
done

