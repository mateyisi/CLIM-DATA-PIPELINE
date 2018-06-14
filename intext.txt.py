
#*********************************************************SET INPUTS*****************************************************
# Input data PARAMETERS: Options; PR, eg_av, evap, 

PARAMRTER $ fg ; fg_ave ; 

#epot_ave ; eg_ave ; epan ; fnee_ave ; fpn_ave

#fg_ave; epot_ave ; eg_ave ; epan ; fnee_ave ; fpn_ave

# available DIRECTORIES to whose data is to be processed
# Options: RCP4.5 ("ACC45" "CCS45" "CNR45" "GFD45" "MPI45" "NOR45")
#          RCP8.5 ("ACC85" "CCS85" "CNR85" "GFD85" "MPI85" "NOR85")
#          Default: ALL

PATHTODIRECTORY $ /home/mohau/Documents/Data-processing-pile-line/DATA
DATADIRECTORIES $ CCS45 ; CNR45 ; GFD45 ; MPI45 ; NOR45
OUTPUTFILE $ out
LOWESTDIRECTORY $ FLUX

#****************************************************DATA OPERATIONS************************************************
# Data OPREATIONS : Options; SelectExtent; AverageTemporally; AverageSpatially, Regrid

OPERATIONS $ AverageTemporally

# STARTING SOUECE DATA time scale (default for CORDEX data is SIXHOURLY): potions: SIXHOURLY, DAILLY, MONTHLY
 
STARTINGDATA $ SixHourly

# FOR Temporal AVEAGIONG: possible output timescales are: sixhourly, dailly_sum, dailly_average, monthly_sum, longterm_monthly_sum,
# longterm_monthly_sum, annual_average, annual_sum, longterm_annual_sum, longterm_annual_average, wmoseas_mean,wmoseas_sum

TIMEAVERAGETO $ na   

# For Spatial REMAPPING OPERATIONS: possible REMAPPINGMETHOD/interpolation methords are; NA, bilinear, IDWM,
#                                                                                         nextneighbouring,
REMAPPINGMETHOD $ na

# FOR Regidding extra options will come here

REGRIDBY $ na
#********************************************** OUTPUT DATA CHARACTERISTIC EXTENT***************************************

# Set TIME INTERVAL (Date Format:yyy-mm-dd,hr:mn:sc)
# for data merge operation: default option is; NA

TIMEINTERVAL $ 2000-10-01,00:00:00; 2000-10-2010,00:00:00

# for subsetting operations give new data spataial EXTENT 
#(Cordinate Format: deg.sc, Order east-lontitude; lat-west-longitude; South-longitude)
# is set to 'NA' same spatatial extent as input will be kept
 
REGIONBOUNTS $  -20.20;20.40;-40.0;50.04

REGIONNAME $ Africa 

