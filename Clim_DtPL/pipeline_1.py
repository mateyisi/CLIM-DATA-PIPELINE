#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:38:54 2018

@author: mohau
"""

import tkinter as tk
import subprocess
from tkinter import filedialog
import tkinter.messagebox
import datetime
from os import system as cmd

class PageTwo(tk.Frame):    
#class PageTwo():
    
   """The function creates all buttons for app. by calling all the relevant
        frames
       
       """ 
    
   def __init__(self):
       
       
       
       self.master = tkinter.Tk()
    
       self.spatial_temporal_analysispage()
       
     
         
       self.master.resizable(1, 1)
       
       
       label = tk.Label(self, text="two")
       label.grid(pady=10, padx=0) 
       
             

       
   def create_allcanvasbuttons(self):
       
       """The function creates all buttons for the app by calling all the relevant
        frames
       
       """
       self.left_frame_level1() 
       self.left_frame_level2()
       self.left_frame_level3()
       
       self.right_frame_level1()
       self.right_frame_level2()
       self.right_frame_level3()
       
   def activate_regionselection(self):
       """This function activates region bounds entry boxes
       while de-activating point entry boxes (i.e., longitude and latitude for a box)

       """
       self.label_xmin.grid(row=5, column=0, padx=0, pady=0)
       self.label_xmax.grid(row=5, column=2, padx=0, pady=0)
       self.label_ymax.grid(row=4, column=1, padx=0, pady=0)
       self.label_ymin.grid(row=6, column=1, padx=0, pady=0)
       
       self.xmin_ebox.grid(row=6, column=0,pady=0)
       self.xmax_ebox.grid(row=6, column=2,pady=0)
       self.ymin_ebox.grid(row=5, column=1,pady=0)
       self.ymax_ebox.grid(row=7, column=1,pady=0)
       
       self.label_lon.grid_forget()
       self.label_lat.grid_forget()
       self.lon_ebox.grid_forget()
       self.lat_ebox.grid_forget()
       
   def activate_pointselection(self):
       
       """This function activates point location entry boxes
       while de-activating region bounds entry boxes.
       
       """
       self.label_lon.grid(row=8, column=0, padx=0, pady=0)
       self.label_lat.grid(row=8, column=2, padx=0, pady=0)
       self.lon_ebox.grid(row=9, column=0,pady=0)
       self.lat_ebox.grid(row=9, column=2,pady=0)
       
       self.label_xmin.grid_forget()
       self.label_xmax.grid_forget()
       self.label_ymax.grid_forget()
       self.label_ymin.grid_forget()
       
       self.xmin_ebox.grid_forget()
       self.xmax_ebox.grid_forget()
       self.ymin_ebox.grid_forget()
       self.ymax_ebox.grid_forget()
       
   def activate_defaultRegion(self):
       
       self.label_xmin.grid_forget()
       self.label_xmax.grid_forget()
       self.label_ymax.grid_forget()
       self.label_ymin.grid_forget()
       
       self.xmin_ebox.grid_forget()
       self.xmax_ebox.grid_forget()
       self.ymin_ebox.grid_forget()
       self.ymax_ebox.grid_forget()
       
       self.label_lon.grid_forget()
       self.label_lat.grid_forget()
       self.lon_ebox.grid_forget()
       self.lat_ebox.grid_forget()
       
   def DisplayDir(self,var):
       
       feedback= filedialog.askdirectory()
       var.set(feedback)
       
   def operators(self):
       
           """This fucntion take the key board input of the type of operator, the key statistical
           operator, input and output time scales and it 
           
           defines the cod for the output data temporal scale, the name of the 'compound operator
           to be used' and the code for the 'key statistical operation'
           
           Note that the defined key statistical operation code have a one to one
           correspondence with cdo operators thus avoiding re-use of elements of cdo name-space
           i.e., operator names.
           
           """
           
           RUNNING = ['RUNNING STATS.','RUNNING PCNTL']
           MYRUNNING= ['MULTI YEAR RUNN. PCNTL.','MULTI YEAR RUNN. STATS.']
           SELECTTIME=['SELECT TIME STATS','SELECT TIME PCTL']

           STAT_TSCALEPt1_DICT = {'hourly':'hh_','daily':'dd_','monthly':'mm_','seasonal':'ss_',
                         'yearly':'yy_','hourly (multi year)':'hh_MY','daily (multi year)':'dd_MY',
                         'monthly (multi year)':'mm_MY','seasonal (multi year)':'ss_MY'}
           STAT_TSCALEPt2_DICT={'STATS.':'STAT','RUNNING STATS.':'RUN_STAT',
                                'RUNNING PCNTL':'RUN_PCTL','MULTI YEAR STATS.':'MYSTAT', 'MULTI YEAR PCNTL':'MYPCTL',
                                      'MULTI YEAR RUNN. STATS.':'MYRUN_STAT','MULTI YEAR RUNN. PCNTL.':'MYRUN_PCTL',
                                      'PCNTL':'PCTL','SELECT TIME STATS':'SELTIME','SELECT TIME PCTL':'SELTIME'}

           KEY_OPERATORPt1_DICT = {'hourly':'hh','daily':'dd','monthly':'mm','seasonal':'ss',
                         'yearly':'yy','hourly (multi year)':'hhMY','daily (multi year)':'ddMY',
                         'monthly (multi year)':'mmMY','seasonal (multi year)':'ssMY'}
           
           KEY_OPERATORPt2_DICT={'MIN':'MIN','MAX':'MAX','RNG':'RNG',
                                      'SUM':'SUM','AVE':'AVE','MEAN':'MEAN','STD':'STD',
                                      'STD1':'STD1','VAR':'VAR','VAR1':'VAR1','PCNTL':'PCTL'}
           
           COMP_OPERATORPt1_DICT={1:'SelTSpan',2:'PredefTSpan',3:'PredefTSpan',5:'PredefTSpan'}

           COMP_OPERATORPt2_DICT={'STATS.':'STATS','RUNNING STATS.':'RunnSTATS',
                                  'RUNNING PCNTL':'RunnPCTL','MULTI YEAR STATS.':'RunnSTATS', 'MULTI YEAR PCNTL':'PCTL',
                                  'MULTI YEAR RUNN. STATS.':'RunnSTATS','MULTI YEAR RUNN. PCNTL.':'RunnPCTL',
                                  'PCNTL':'PCTL','SELECT TIME STATS':'STATS','SELECT TIME PCTL':'PCTL'}

           self.COMP_OPERATORNPt3_DICT={'IN HOUSE':'INH','CORDEX':'CDX'}
       
           self.MYRUNNING_DICT ={1:'SUM_',2:'MEAN_','':''}

           if(self.lv3_Rdvar.get() in [1,2,3]):
               
               CNP1= COMP_OPERATORPt1_DICT[self.lv3_Rdvar.get()]
               CNP2= COMP_OPERATORPt2_DICT[self.tkvar_opr.get()]
       
               KNP1=KEY_OPERATORPt1_DICT[self.tkvar_outTscale.get()]
               KNP2=KEY_OPERATORPt2_DICT[self.tkvar_StatsOpr.get()]
              
               self.COMPOUNDOPERATOR = CNP1+CNP2

               if(self.tkvar_opr.get() in RUNNING):
               
                   self.KEY_OPERATOR='RUN'+KNP2
                   self.OPERATION_TSCALE =STAT_TSCALEPt1_DICT[self.tkvar_outTscale.get()]+STAT_TSCALEPt2_DICT[self.tkvar_opr.get()] 
                   
               elif(self.tkvar_opr.get() in SELECTTIME):
               
                   self.KEY_OPERATOR='sltsp'+KNP2
                   self.OPERATION_TSCALE =STAT_TSCALEPt1_DICT[self.tkvar_outTscale.get()]+STAT_TSCALEPt2_DICT[self.tkvar_opr.get()] 
               
               elif(self.tkvar_opr.get() in MYRUNNING):
               
                   self.KEY_OPERATOR='ddMYRUN'+KNP2
               
                   if(self.tkvar_inTScale.get()=='hourly'):
                       self.OPERATION_TSCALE =STAT_TSCALEPt1_DICT[self.tkvar_outTscale.get()]+self.MYRUNNING_DICT[self.tk_ddChoicePCTL.get()]+STAT_TSCALEPt2_DICT[self.tkvar_opr.get()]
                   else:
                       self.OPERATION_TSCALE =STAT_TSCALEPt1_DICT[self.tkvar_outTscale.get()]+STAT_TSCALEPt2_DICT[self.tkvar_opr.get()]
               else:
               
                   self.KEY_OPERATOR= KNP1+KNP2
                   self.OPERATION_TSCALE =STAT_TSCALEPt1_DICT[self.tkvar_outTscale.get()]+STAT_TSCALEPt2_DICT[self.tkvar_opr.get()] 
           
        
           elif(self.lv3_Rdvar.get()==5):
               
               CNP1= COMP_OPERATORPt1_DICT[self.lv3_Rdvar.get()]
               CNP2= COMP_OPERATORPt2_DICT['STATS.']
               
               self.COMPOUNDOPERATOR = CNP1+CNP2
    
               MIXED_KEYOPRATOR_DICT={     'daily SUM to Monthly MEAN':'dd_SUM_mm_MEAN_STAT',
                                           'daily SUM to Multi_year daily MEAN':'dd_SUM_dd_MYMEAN_STAT',
                                           'daily MEAN to Multi_year daily MEAN':'dd_SUM_dd_MYMEAN_STAT',
                                           'monthly SUM to Annual MEAN':'mm_SUM_yy_MEAN_STAT', 
                                           'monthly SUM to multi_year monthly MEAN':'mm_SUM_mm_MYMEAN_STAT'}
               
               self.KEY_OPERATOR  =  MIXED_KEYOPRATOR_DICT[self.tkvar_opr.get()]
               
               self.OPERATION_TSCALE='NA'

   def commit1(self,value):
     
       
       self.path=str(self.MyText.get()) 
       
       if(self.tk_varRegionCord.get()==1):
           
           print(self.MyText.get())
           print(self.regn_ebox.get())
       
           print(self.dir_ebox.get())
           print(self.dircont_ebox.get())
       
           print(self.xmin_ebox.get())
           print(self.ymin_ebox.get())
           print(self.xmax_ebox.get())
           print(self.ymax_ebox.get())
       elif(self.tk_varRegionCord.get()==2):
           
           print(self.path_ebox.get())
           print(self.regn_ebox.get())
       
           print(self.dir_ebox.get())
           print(self.dircont_ebox.get())
           
           print(self.lon_ebox.get())
           print(self.lat_ebox.get())
       
   def commit2(self,value):
       
       
       if(self.tk_tframevar.get()==1):
       
           print(self.tkvar_filingsyle.get())
       
           print(self.par_ebox.get())
       
           print(self.tmin1.get())
       
           print(self.tmax1.get())
       else:
          
          print(self.tkvar_filingsyle.get())
       
          print(self.par_ebox.get())
          
   def commit3(self,value):
       
       if(self.lv3_Rdvar.get()==1):
           print(self.entry_NOffset.get())
           print(self.entry_size.get())
           print(self.entry_cutoff.get())
           print(self.tkvar_opr.get())
           print(self.tkvar_StatsOpr.get())
           
           if((self.tkvar_opr.get() in self.RUNNINGSTATS) or( self.tkvar_opr.get() in self.RUNNINGSPCNTL)):
               
               print(self.entry_runwin.get())
               
       elif(self.lv3_Rdvar.get()==2):
           print(self.tkvar_inTScale.get())
           print(self.tkvar_outTscale.get())
           print(self.tkvar_opr.get())
           print(self.tkvar_StatsOpr.get())
           
           if(self.tkvar_StatsOpr.get()=='PCNTL'):
               
               print(self.entry_pcntl.get())
               
           if((self.tkvar_opr.get() in self.RUNNINGSTATS) or( self.tkvar_opr.get() in self.RUNNINGSPCNTL)):
               
               print(self.entry_runwin.get())
               
       elif(self.lv3_Rdvar.get()==3):
           
            print(self.tkvar_opr.get())    
            print(self.tkvar_StatsOpr.get())
            
   def save_all(self):
       
       self.operators()
                   
       path = str(self.MyText.get())
       if(len(path)==0):
           path='NA'
            
       region_name=str(self.regn_ebox.get())
       if(len(region_name)==0):
           region_name='NA'
       
       subfile_name=str(self.dircont_ebox.get())
       if(len(subfile_name)==0):
           subfile_name='NA'
       
       derectory_list=str(self.dir_ebox.get())
       if(len(derectory_list)==0):
           derectory_list='NA'
       
       paramters=str(self.par_ebox.get())
       if(len(paramters)==0):
           paramters='NA'
       
       input_timescale=str(self.tkvar_inTScale.get())
       if(len(input_timescale)==0):
           input_timescale='NA'
       
       
       start_analysistime=self.tmin1.get()
       if(len(start_analysistime)==0):
           start_analysistime='NA'
       
       end_analysistime=self.tmax1.get()
       if(len(end_analysistime)==0):
           end_analysistime='NA'
       
       compound_operator=str(self.COMPOUNDOPERATOR)
       if(len(compound_operator)==0):
           compound_operator='NA'
       
       key_operator=str(self.KEY_OPERATOR)
       if(len(key_operator)==0):
           key_operator='NA'
       
       operation_timescale = str(self.OPERATION_TSCALE)
       if(len(operation_timescale)==0):
           operation_timescale='NA'
       
       xmin=str(self.xmin_ebox.get())
       if(len(xmin)==0):
           xmin='NA'
       ymin=str(self.ymin_ebox.get())
       if(len(ymin)==0):
           ymin='NA'
       xmax=str(self.xmax_ebox.get())
       if(len(xmax)==0):
           xmax='NA'
       
       ymax=str(self.ymax_ebox.get())
       if(len(ymax)==0):
           ymax='NA'
       
       filing_style=str(self.tkvar_filingsyle.get())
       if(len(filing_style)==0):
           filing_style='NA'
           
           
       if filing_style=='CORDEX':
           
           filing_style='CDX'
       elif filing_style=='IN HOUSE':
           filing_style='INH'
       
       
       timesteps_NOffset=str(self.entry_NOffset.get())
       if(len(timesteps_NOffset)==0):
           timesteps_NOffset='NA'
           
       timestep_size=str(self.entry_size.get())
       if(len(timestep_size)==0):
           timestep_size='NA'
       
       timstep_cutoff=str(self.entry_cutoff.get())
       if(len(timstep_cutoff)==0):
          timstep_cutoff='NA'
       
       percentile=str(self.entry_pcntl.get())
       if(len(percentile)==0):
          percentile='NA'
       
       running_windowSize =str(self.entry_runwin.get())
       if(len(running_windowSize)==0):
          running_windowSize='NA'

       
       file = open("./intext.txt",'w')
       
       file.write("PATHTODIRECTORY $ " + format(str(path)))
       file.write("\n#___________________________________________\n")
       file.write("DATADIRECTORIES $ " + format(str(derectory_list)))
       file.write("\n#___________________________________________\n")
       file.write("INPUTFILINGSTYLE $ " + format(str(filing_style)))
       file.write("\n#___________________________________________\n")
       file.write("REGIONNAME $ " + format(str(region_name)))
       file.write("\n#___________________________________________\n")
       file.write("LOWESTDIRECTORY $ " + format(str(subfile_name)))
       file.write("\n#___________________________________________\n")
       file.write("TIMEINTERVAL $ " + format(str(start_analysistime)) +";"+ format(str(end_analysistime)))
       file.write("\n#___________________________________________\n")
       file.write("PARAMRTER $ " + format(str(paramters)))
       file.write("\n#___________________________________________\n")
       file.write("REGIONBOUNTS $ " + format(str(xmin))+";"+ format(str(xmax))+";"+ format(str(ymin))+";"+ format(str(ymax)))
       file.write("\n#___________________________________________\n")
       file.write("STARTINGTIMESCALE $ " + format(str(input_timescale)))
       file.write("\n#___________________________________________\n")
       file.write("COMPOUNDOPERATOR $ " + format(str(compound_operator)))
       file.write("\n#___________________________________________\n")
       file.write("OPERATIONTSCALE $ " + format(str(operation_timescale)))
       file.write("\n#___________________________________________\n")
       file.write("TIMESTEPS $ " + format(str(running_windowSize)))
       file.write("\n#___________________________________________\n")
       file.write("OPERATOR $ " + format(str(key_operator)))
       file.write("\n#___________________________________________\n")
       file.write("PCTL $ " + format(str(percentile)))
       file.write("\n#___________________________________________\n")
       file.write("NSETS $ " + format(str(timestep_size)))
       file.write("\n#___________________________________________\n")
       file.write("NOffset $ " + format(str(timesteps_NOffset)))
       file.write("\n#___________________________________________\n")
       file.write("CUTOFF $ " + format(str(timstep_cutoff)))
       file.write("\n#___________________________________________\n")
       file.write("OUTPUTFILE $" + 'outfile')

       file.close()
       
       print('saved')

#   def consistency_commit1(self,value):
#
#       """This function check for consistency of inputs for path to the working directory.
#       Erroy messages are thrown only for empty string inputs and non-float data types.
#       Non-existant inputs specifications are not flagged and will further be cought by 
#       cdo error handling routines.
#       
#       """
#       self.path=str(self.MyText.get())          
#       self.region=str(self.regn_ebox.get())       
#       self.direcotries=str(self.dir_ebox.get())
#       self.dataContainer=str(self.dircont_ebox.get())
#       
#       try:
#           
#           if int(self.path):
#               ...
#               
#           elif int(self.region):
#               ...
#               
#           elif int(self.direcotries):
#               ...
#               
#           elif int(self.dataContainer):
#               ...
#               
#       except ValueError:
#           
#            if not self.path:
#                
#              tkinter.messagebox.showinfo('Error:', 'empty string for path')
#             
#            elif not self.region:
#              
#              tkinter.messagebox.showinfo('Error:', 'empty string for region')
#              
#            elif not self.direcotries:
#                
#              tkinter.messagebox.showinfo('Error:', 'empty string for derectories')
#              
#            elif not self.dataContainer:
#                              
#               tkinter.messagebox.showinfo('Error:', 'empty string for data countainer sub derectory')
#                
#       
#       if(self.tk_varRegionCord.get()==1):
#           
#           try:
#
#               self.minlon=float(self.xmin_ebox.get())
#               self.minlat=float(self.ymin_ebox.get())
#               self.maxlon=float(self.xmax_ebox.get())
#               self.maxlat=float(self.ymax_ebox.get())
#               
#           except ValueError:
#              
#              tkinter.messagebox.showinfo('Error:', 'One or more of your region bounds is not numeric. Please fix them.')
#              
#       elif(self.tk_varRegionCord.get()==2):
#           
#           try:
#               
#               self.lon=float(self.lon_ebox.get())
#               self.lat=float(self.lat_ebox.get())
#               
#           except ValueError:
#              
#              tkinter.messagebox.showinfo('Error:', 'either one or both longitude and latitude value is/are not numeric. Please fix this.')
#          
#   def consistency_commit2(self,value):
#       
#       
#       """This function check for consistency of inputs for analysis, input data 'NetCDF filing style', 
#       'start' and 'end' dates.
#       Erroy messages are thrown only for empty string for inputs.
#       In the case of dates the function checks consistency with ISO format: %Y-%m-%dT%H:%M:%S".
#       Note incorrect ordering of dates in not flagged and will be further handled
#       cdo error handling flags.
#       
#       """
#       
#       self.filing_sty= str(self.tkvar_filingsyle.get())
#       
#       self.parameter=str(self.par_ebox.get())
#       
#       
#       
#       if(self.tk_tframevar.get()==1):
#       
#           try:
#               
#               if int(self.filing_sty):
#                   ...
#               elif int(self.parameter):
#                   ...
#              
#           except ValueError:
#              
#               if not self.filing_sty:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for filing style')
#                   
#               elif not self.parameter:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for parameters to be processed')
#                   
#             
#           try:
#                 
#               self.start_time=datetime.datetime.strptime(self.tmin1.get(),"%Y-%m-%dT%H:%M:%S")
#       
#               self.end_time=datetime.datetime.strptime(self.tmax1.get(),"%Y-%m-%dT%H:%M:%S")
#               
#               if datetime.datetime.strptime(self.tmin1.get(),"%Y-%m-%dT%H:%M:%S")>datetime.datetime.strptime(self.tmax1.get(),"%Y-%m-%dT%H:%M:%S"):
#                   ...
#               
#                  
#           except ValueError: 
#                  
#               tkinter.messagebox.showinfo('Error:', 'The start and/or end date is either not entered or formatted in the suggested ISO format. Please fix this.')
#           try:
#              
#              if (datetime.datetime.strptime(self.tmin1.get(),"%Y-%m-%dT%H:%M:%S") > datetime.datetime.strptime(self.tmax1.get(),"%Y-%m-%dT%H:%M:%S")):
#                   ...
#              
#           except ValueError:
#              
#              tkinter.messagebox.showinfo('Error:', 'the input time interval is Undefined. Please fix this.')
#              
#              
#               
#                       
#              
#       else:
#            
#           try:
#               
#               if int(self.filing_sty):
#                   ...
#               elif int(self.parameter):
#                   ...
#                   
#           except ValueError:
#              
#               if not self.filing_sty:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for filing style')
#                   
#               elif not self.parameter:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for parameters to be processed')
#   
#   def consistency_commit3(self,value):
#       
#       
#       """This function check for consistency of inputs for path to the working directory.
#       Erroy messages are thrown only for empty string inputs and non-float data types.
#       Non-existant inputs specifications are not flagged and will further be cought by 
#       cdo error handling routines.
#       
#       """
#       self.RUNNINGSTATS=['RUNNING STATS.','MULTI YEAR RUNN. STATS.']
#       self.RUNNINGSPCNTL=['MULTI YEAR RUNN. PCNTL.','RUNNING PCNTL']
#       self.PCNTLs=['MULTI YEAR PCNTL','PCNTL','RUNNING PCNTL','MULTI YEAR RUNN. PCNTL.'] 
#       self.MYRUNOPRTYPES=['MULTI YEAR RUNN. STATS.','MULTI YEAR RUNN. PCNTL.']
#       
#       self.operator_type=str(self.tkvar_opr.get())
#       self.stats_operator=str(self.tkvar_StatsOpr.get())
#       
#       self.input_tscale=str(self.tkvar_inTScale.get())
#       self.output_tscale=str(self.tkvar_outTscale.get())
#       
#       self.ddaggrationoperator=int(self.tk_ddChoicePCTL.get())
#       
#       self.running_window=str(self.entry_runwin.get())
#       
#       if(self.lv3_Rdvar.get()==1):
#           
#           
#           
#           # check the imput specification entries
#           try:
#              self.NOffset=float(self.entry_NOffset.get())
#              
#              self.step_size=float(self.entry_size.get())
#              
#              self.cutoff=float(self.entry_cutoff.get())
#               
#
#           except ValueError:
#              
#                   tkinter.messagebox.showinfo('Error:', 'One or more of calculation specifications is not numeric. Please fix them.')
#           #check for 'compound operator type' and 'statistical operation' selection entries      
#           try:
#              
#               if int(self.operator_type):
#                   ...
#                   
#               elif int(self.stats_operator):
#                   ...
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type of operator selection')
#                   
#               elif not self.stats_operator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the statistical operation choice')
#           #check percentile entry        
#           if(self.tkvar_opr.get() in self.PCNTLs):
#               
#               try:
#                   
#                  self.percentile=float(self.entry_pcntl.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the percentile ')
#           #check the window size entry    
#           if((self.tkvar_opr.get() in self.RUNNINGSTATS) or ( self.tkvar_opr.get() in self.RUNNINGSPCNTL)):
#               
#               print(self.entry_runwin.get())
#               
#               try:
#                   
#                  self.running_window=float(self.entry_runwin.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the running window size')
#       
#       if(self.lv3_Rdvar.get()==4):
#           
#           try:
#
#              if int(self.operator_type):
#                   ...
#                   
#              elif int(self.stats_operator):
#                   ...
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type of operator selection')
#                   
#               elif not self.stats_operator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the statistical operation choice')
#                   
#       if(self.lv3_Rdvar.get()==3):
#           
#           try:
#              
#               if int(self.operator_type):
#                   ...
#                   
#               elif int(self.stats_operator):
#                   ...
#                   
#               elif int(self.input_tscale):
#                   ...
#                   
#               elif int(self.output_tscale):
#                   ...
#                   
#               elif int(self.ddaggrationoperator):
#                   ...
#                       
#                           
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type of operator selection')
#                   
#               elif not self.stats_operator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the statistical operation choice')
#                   
#               elif not self.input_tscale:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the input time scale choice')
#                   
#               elif not self.output_tscale:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the output time scale choice')
#               
#               elif not self.ddaggrationoperator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the operation to daily time scale')
#                   
#           
#                   
#           if((self.tkvar_opr.get() in self.MYRUNOPRTYPES)):
#               
#               print(self.entry_runwin.get())
#               
#               try:
#                   
#                  self.running_window=float(self.entry_runwin.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the running window size')
#            #check percentile entry        
#           if(self.tkvar_opr.get() in self.PCNTLs):
#               
#               try:
#                   
#                  self.percentile=float(self.entry_pcntl.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the percentile ')
#
#                   
#                   
#       if(self.lv3_Rdvar.get()==2):
#           
#           try:
#              
#               if int(self.operator_type):
#                   ...
#                   
#               elif int(self.stats_operator):
#                   ...
#                   
#               elif int(self.input_tscale):
#                   ...
#                   
#               elif int(self.output_tscale):
#                   ... 
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type of operator selection')
#                   
#               elif not self.stats_operator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the statistical operation choice')
#                   
#               elif not self.input_tscale:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the input time scale choice')
#                   
#               elif not self.output_tscale:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the output time scale choice')
#                   
#                   
#                   
#           #check percentile entry        
#           if(self.tkvar_opr.get() in self.PCNTLs):
#               
#               try:
#                   
#                  self.percentile=float(self.entry_pcntl.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the percentile ')
#           #check the window size entry    
#           if((self.tkvar_opr.get() in self.RUNNINGSTATS) or ( self.tkvar_opr.get() in self.RUNNINGSPCNTL)):
#               
#               print(self.entry_runwin.get())
#               
#               try:
#                   
#                  self.running_window=float(self.entry_runwin.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the running window size')
#           #check percentile entry        
#           if(self.tkvar_opr.get() in self.PCNTLs):
#               
#               try:
#                   
#                  self.percentile=float(self.entry_pcntl.get())
#                  
#               except ValueError:
#                  
#                   tkinter.messagebox.showinfo('Error:', 'A non-empty or integer value is expected for the percentile ')
#
#       
#       
#
#       if(self.lv3_Rdvar.get()==4):
#           
#           try:
#
#              if int(self.operator_type):
#                   ...
#                   
#              elif int(self.stats_operator):
#                   ...
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type of operator selection')
#                   
#               elif not self.stats_operator:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the statistical operation choice')
#                   
#       if(self.lv3_Rdvar.get()==5):
#           
#           try:
#
#              if int(self.operator_type):
#                   ...
#                   
#              elif int(self.input_tscale):
#                   ...
#                   
#           except ValueError:
#              
#               if not self.operator_type:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the type mixed a operator selection')
#                   
#               elif not self.input_tscale:
#                   
#                   tkinter.messagebox.showinfo('Error:', 'empty string for the for input time scale') 
          
                    
   def analysisParameterAnddate_selection(self):
       
       
       """Method for gridding analysis start and end time entry option.
       
       """
       
       self.label_stdate.grid(row=4, column=0, padx=0, pady=0)
       self.label_enddate.grid(row=4, column=1, padx=0, pady=0)
       
       self.tmin1.grid(row=5, column=0,pady=0)
       self.tmax1.grid(row=5, column=1,pady=0)
       
       
   def specify_DefAnalysisTimeOptions(self):
       
       self.label_stdate.grid_forget()
       self.label_enddate.grid_forget()
       
       self.tmin1.grid_forget()
       self.tmax1.grid_forget()
       
             
   def userdefinedtimesets_analysis(self):
       
       
       """Method for activating non-relevant input options and activating
       relevant input options under user-defined analysis time scale 
      option.
       
       """
       
       #self.label_inTscale.grid_forget()
       #self.label_outTscale.grid_forget()
       
       #self.popup_inTscale.grid_forget()
       #self.popup_outTscale.grid_forget()
       
       self.label_inTscale.grid(row=5, column=0, padx=0, pady=0)
       
       self.choices_inTScale=['hourly','daily','monthly','seasonal','yearly','hourly (multi year)','daily (multi year)','monthly (multi year)','seasonal (multi year)']                            
       self.tkvar_inTScale=tk.StringVar(self.right_midframe3)               
       self.popup_inTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_inTScale, self.choices_inTScale[0],*self.choices_inTScale,command=self.inTScale_func)
       self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
       self.tkvar_inTScale.set('')
       
       
     
       #NOffset, step size and cutoff entry boxes       
       self.label_NOffset.grid(row=1, column=0, padx=0, pady=0)
       self.label_size.grid(row=1, column=1, padx=0, pady=0)
       self.label_cutoff.grid(row=1, column=2, padx=0, pady=0)
       
       self.entry_NOffset.grid(row=2, column=0,pady=0)
       self.entry_size.grid(row=2, column=1,pady=0)
       self.entry_cutoff.grid(row=2, column=2,pady=0)
       
       self.label_oprType.grid_forget()
       self.label_oprType= tk.Label(self.right_midframe3,text='Operator Type')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)
       
       #operator type drop down menu
       self.popup_oprtype.grid_forget()
       self.choices_oprtype=['SELECT TIME STATS','SELECT TIME PCTL']
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
       
       self.popup_oprtype.grid_forget()
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype,command=self.stats_func)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
       
       #disable input time scale, output time scale, operator and pencentile options
       
       
       
       self.label_StatsOpr.grid_forget()
       self.popup_StatsOpr.grid_forget()
       
             
       self.label_pcntl.grid_forget()
       self.entry_pcntl.grid_forget()
       
       
       self.C2.grid_forget()
       self.C3.grid_forget()
       
       
                   
       
       
       
     
   def calenderbased_analysis(self):
       
       
       """Method for activating non-relevant input options and activating
       relevant input options under pre-defined statisical
       analysis option.
       
       """
           
       
       self.label_inTscale.grid(row=5, column=0, padx=0, pady=0)
       
       
       self.label_outTscale.grid_forget()
       self.popup_outTscale.grid_forget()
       
      
       self.popup_inTscale.grid_forget()
       
       
       self.label_oprType.grid_forget()
       self.label_oprType= tk.Label(self.right_midframe3,text='Operator Type')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)
       
       self.popup_oprtype.grid_forget()
       
       self.choices_oprtype=['STATS.','PCNTL','RUNNING STATS.', 'RUNNING PCNTL']
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
                
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype,command=self.stats_func)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
       
       self.choices_inTScale=['hourly','daily','monthly','seasonal','yearly','hourly (multi year)','daily (multi year)','monthly (multi year)','seasonal (multi year)']                            
       self.tkvar_inTScale=tk.StringVar(self.right_midframe3)               
       self.popup_inTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_inTScale, self.choices_inTScale[0],*self.choices_inTScale,command=self.inTScale_func)
       self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
       self.tkvar_inTScale.set('')
       
       self.label_StatsOpr.grid_forget()
       self.popup_StatsOpr.grid_forget()
       #drop down for operator type 
       
       self.label_outTscale.grid_forget()
       self.popup_outTscale.grid_forget()
       
       #dis apple NOffset, size and cutoff entry options
       self.label_NOffset.grid_forget()
       self.label_size.grid_forget()
       self.label_cutoff.grid_forget()
       
       self.entry_NOffset.grid_forget()
       self.entry_size.grid_forget()
       self.entry_cutoff.grid_forget()

       self.C2.grid_forget()
       self.C3.grid_forget()
           
    
       
       
   def calenderbased_multiyearanalysis(self):
       
       
       """Method for activating non-relevant input options and activating
       relevant input options under pre-defined multi-year running statisical
       analysis option.
       
       """
       

       self.label_StatsOpr.grid_forget()
       self.popup_StatsOpr.grid_forget()
       #drop down for operator type 
       self.popup_outTscale.grid_forget()
       
       #dis apple NOffset, size and cutoff entry options
       self.label_NOffset.grid_forget()
       self.label_size.grid_forget()
       self.label_cutoff.grid_forget()
       
       self.entry_NOffset.grid_forget()
       self.entry_size.grid_forget()
       self.entry_cutoff.grid_forget()
       
       
       
       self.label_inTscale.grid(row=5, column=0, padx=0, pady=0)
       
       
       self.label_outTscale.grid_forget()
       self.popup_outTscale.grid_forget()
       
       self.popup_inTscale.grid_forget()
       
       
       
       self.popup_oprtype.grid_forget()
       
       
       self.label_oprType.grid_forget()
       self.label_oprType= tk.Label(self.right_midframe3,text='Operator Type')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)
       
       self.choices_oprtype=['MULTI YEAR RUNN. STATS.','MULTI YEAR RUNN. PCNTL.']
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
                
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype,command=self.stats_func_multiyear)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
       
       
       self.choices_inTScale=['hourly','daily']                             
       self.tkvar_inTScale=tk.StringVar(self.right_midframe3)               
       self.popup_inTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_inTScale, self.choices_inTScale[0],*self.choices_inTScale,command=self.inTScale_func)
       self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
       self.tkvar_inTScale.set('')
       
       self.label_runwin= tk.Label(self.right_midframe3,text='Run. Window size')
       self.label_runwin.grid_propagate(0)
       self.label_runwin.grid(row=11, column=1, padx=0, pady=0)
       
       self.entry_runwin= tk.Entry(self.right_midframe3, text='entry running window size')
       self.entry_runwin.grid_propagate(0)
       self.entry_runwin.grid(row=12, column=1,pady=5)
       
       
       
       
       
       #choose sum or mean
       self.tk_ddChoicePCTL=tk.IntVar()
       
       self.C2 = tk.Radiobutton(self.right_midframe3, text='Sum to daily',variable=self.tk_ddChoicePCTL,value=1)
       self.C2.grid_propagate(0)
       
       
       self.C2.grid(row=7, column=1, padx=0, pady=0)
       
       self.C3 = tk.Radiobutton(self.right_midframe3, text='Ave. to daily',variable=self.tk_ddChoicePCTL,value=2)
       self.C3.grid_propagate(0)
       self.C3.grid(row=8, column=1, padx=0, pady=0)
       
       
       

   def calenderbased_mixedoperatoranalysiss(self):
       
       
       """Method for de-activating non-relevant input options and activating
       relevant input options under mixed time scale operator option
       
       """
       
       self.label_outTscale.grid_forget()
       self.popup_outTscale.grid_forget()
       
       

       self.label_StatsOpr.grid_forget()
       self.popup_StatsOpr.grid_forget()
       #drop down for operator type 
       self.popup_outTscale.grid_forget()
       
       #dis apple NOffset, size and cutoff entry options
       self.label_NOffset.grid_forget()
       self.label_size.grid_forget()
       self.label_cutoff.grid_forget()
       
       self.entry_NOffset.grid_forget()
       self.entry_size.grid_forget()
       self.entry_cutoff.grid_forget()
       
       self.C2.grid_forget()
       self.C3.grid_forget()
       
       self.label_inTscale.grid(row=5, column=0, padx=0, pady=0)
       
       
      
       
       self.label_oprType.grid_forget()
       self.label_oprType= tk.Label(self.right_midframe3,text='Combined Operators')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)
       
       
       self.popup_oprtype.grid_forget()
       
       self.choices_oprtype=['daily SUM to Monthly MEAN','daily MEAN to Multi_year daily MEAN','daily SUM to Multi_year daily MEAN','monthly SUM to Annual MEAN',  'monthly SUM to multi_year monthly MEAN']
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
       
       self.popup_oprtype.grid_forget()
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
       
       self.popup_inTscale.grid_forget()
       self.choices_inTScale=['hourly','daily']                             
       self.tkvar_inTScale=tk.StringVar(self.right_midframe3)               
       self.popup_inTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_inTScale, self.choices_inTScale[0],*self.choices_inTScale)
       self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
       self.tkvar_inTScale.set('')
       
       self.label_runwin.config(state='disabled')
       self.entry_runwin.config(state='disabled')
       self.label_pcntl.config(state='disabled')
       self.entry_pcntl.config(state='disabled')
       

   def spatioteomporalsubsetting_seletion(self):
       
       
       """Method for de-activating non-relevant input options and activating
       relevant input options under spatio-temporal subsetting option.
       
       """
       
       self.label_NOffset.grid_forget()
       self.label_size.grid_forget()
       self.label_cutoff.grid_forget()
       
       self.entry_NOffset.grid_forget()
       self.entry_size.grid_forget()
       self.entry_cutoff.grid_forget()
       
       self.label_oprType.grid_forget()
       self.label_oprType= tk.Label(self.right_midframe3,text='Operator Type')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)

       
       self.choices_oprtype=['Spatial Subsetting']
       
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
       
       self.popup_oprtype.grid_forget()
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype,command=self.stats_func)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
       
       self.label_inTscale.grid_forget()
       self.label_outTscale.grid_forget()
       
       self.popup_inTscale.grid_forget()
       self.popup_outTscale.grid_forget()
       
       self.label_StatsOpr.grid_forget()
       self.popup_StatsOpr.grid_forget()
                   
       self.label_runwin.config(state='disabled')
       self.entry_runwin.config(state='disabled')
       self.label_pcntl.config(state='disabled')
       self.entry_pcntl.config(state='disabled')
     
       
       self.C2.grid_forget()
       self.C3.grid_forget()
       
   def Outstats_func(self,value):
      
      self.OuTStats=value
      
      #print(self.OuTStats)
              
   def OutTScale_func(self,value):
       
       self.OuTScale=value       
       #print(self.OuTScale)
              
   def inTScale_func(self,value):
       
        
        """function called upon clicking the input time scales. It desplays
        the available allowed output time scales on a drop down menu.
        
        """
       
        RUNNING = ['RUNNING STATS.','RUNNING PCNTL']
       
    
          
        if (self.lv3_Rdvar.get()==3) :
            
            self.choices_OutTScale=['daily']
                
                
            
        else:
            
            self.choices_OutTScale=['hourly','daily','monthly','seasonal','yearly','hourly (multi year)','daily (multi year)','monthly (multi year)','seasonal (multi year)']
            
            self.choices_OutTScaleA=['hourly','daily','monthly','seasonal','yearly']
            self.choices_OutTScaleB=['hourly (multi year)','daily (multi year)','monthly (multi year)','seasonal (multi year)']
            
            
            if(value in self.choices_OutTScaleA):
                
                start=self.choices_OutTScaleA.index(value)
        
                self.choices_OutTScale=(self.choices_OutTScaleA[start: len(self.choices_OutTScaleA)+1])+(self.choices_OutTScaleB[(start): len(self.choices_OutTScaleB)])
                
            elif(value in self.choices_OutTScaleB):
                
                start=self.choices_OutTScaleB.index(value)
                self.choices_OutTScale=(self.choices_OutTScaleB[start: len(self.choices_OutTScaleB)])
                
            elif(self.popup_oprtype.get() in RUNNING):
                
                self.choices_OutTScale=['daily']
                
        
        
        self.label_outTscale.grid(row=5, column=2, padx=0, pady=0)
        
        self.tkvar_outTscale=tk.StringVar(self.right_midframe3)
        self.popup_outTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_outTscale, self.choices_OutTScale[0],*self.choices_OutTScale,command=self.OutTScale_func)
        self.popup_outTscale.grid(row=6,column=2,padx=0, pady=0)
        
        self.tkvar_outTscale.set('')
        #tkvar1.trace("w", self.inTScale_func)
        
        
        
        return(value)
        
   

       

       
   def stats_func_multiyear(self,value):
           
           """function for displaying the options under multi year running 
           statistical operations.
           
           """
       
           MYPCNL='MULTI YEAR RUNN. PCNTL.'  
       
           if(self.lv3_Rdvar.get()==3):
               
              if(value==MYPCNL):
                   
                    self.choices_StatsOpr=['PCNTL']
                    self.entry_pcntl= tk.Entry(self.right_midframe3)
                    self.entry_pcntl.grid_propagate(0)
                    self.entry_pcntl.grid(row=10, column=1,pady=5)
                    
                    
              elif(value=='MULTI YEAR RUNN. STATS.'):
          
                   self.choices_StatsOpr=['MIN','MAX','RNG','SUM','AVE','MEAN','STD','STD1','VAR','VAR1']
                   
                   self.label_pcntl.config(state='disabled')
                   self.entry_pcntl.config(state='disabled')
              
                
              self.label_StatsOpr.grid(row=3,column=2,padx=0, pady=0)
              self.tkvar_StatsOpr=tk.StringVar(self.right_midframe3)
           
              self.popup_StatsOpr= tk.OptionMenu(self.right_midframe3,self.tkvar_StatsOpr, self.choices_StatsOpr[0],*self.choices_StatsOpr)
              self.popup_StatsOpr.grid(row=4,column=2,padx=0, pady=0)
              self.tkvar_StatsOpr.set('')
          
                
                  
              
              
          
       
           
   def stats_func(self,value):
       
       
       """The method plots the buttongs within the right mid-frame. 
       
       It is called by the bottons within the right mid_frames frames.
       
       The outputs are displayed of the right mid frames. 
       
       """
         
       Stats=['MULTI YEAR STATS.','STATS.','RUNNING STATS.','SELECT TIME STATS']
       PCNTLs=['RUNNING PCNTL','PCNTL','MULTI YEAR PCNTL','SELECT TIME PCTL'] 
       SUBSETTING=['Temp Subsetting', 'Spatial Subsetting']
       
       self.RUNNINGSTATS=['RUNNING STATS.']
       self.RUNNINGSPCNTL=['RUNNING PCNTL']
      
      
       
       self.popup_outTscale.grid_forget()
       self.label_StatsOpr.grid(row=3, column=2, padx=0, pady=0)
       #self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
           
       if value in Stats:
           
          self.label_NOffset.grid(row=1, column=0, padx=0, pady=0)
          self.label_size.grid(row=1, column=1, padx=0, pady=0)
          self.label_cutoff.grid(row=1, column=2, padx=0, pady=0)
       
          self.entry_NOffset.grid(row=2, column=0,pady=0)
          self.entry_size.grid(row=2, column=1,pady=0)
          self.entry_cutoff.grid(row=2, column=2,pady=0)
          
          
          self.label_runwin.config(state='disabled')
          self.entry_runwin.config(state='disabled')
          
          if value in self.RUNNINGSTATS:
              
              self.label_runwin= tk.Label(self.right_midframe3,text='Run Window size')
              self.label_runwin.grid_propagate(0)
              self.label_runwin.grid(row=11, column=1, padx=0, pady=0)
       
              self.entry_runwin= tk.Entry(self.right_midframe3, text='entry running window size')
              self.entry_runwin.grid_propagate(0)
              self.entry_runwin.grid(row=12, column=1,pady=0)
              
             
              
          
          if(self.lv3_Rdvar.get()==2):
          
              self.label_NOffset.grid_forget()
              self.label_size.grid_forget()
              self.label_cutoff.grid_forget()
          
              self.entry_NOffset.grid_forget()
              self.entry_cutoff.grid_forget()
              self.entry_size.grid_forget()
              
          self.label_pcntl.config(state='disabled')
          self.entry_pcntl.config(state='disabled')
          
          self.choices_StatsOpr=['MIN','MAX','RNG','SUM','AVE','MEAN','STD','STD1','VAR','VAR1']          
          self.tkvar_StatsOpr=tk.StringVar(self.right_midframe3)  
          self.popup_StatsOpr= tk.OptionMenu(self.right_midframe3,self.tkvar_StatsOpr, self.choices_StatsOpr[0],*self.choices_StatsOpr,command=self.Outstats_func)
          self.popup_StatsOpr.grid(row=4,column=2,padx=0, pady=0)
          self.tkvar_StatsOpr.set('')
                           
       elif value in PCNTLs:
          
          choices_StatsOpr=['PCNTL']
        
          #place percentile lable and grid box
         
         
           
          self.tkvar_StatsOpr=tk.StringVar(self.right_midframe3)
          
          self.popup_StatsOpr= tk.OptionMenu(self.right_midframe3,self.tkvar_StatsOpr, choices_StatsOpr[0],*choices_StatsOpr)
          self.popup_StatsOpr.grid(row=4,column=2,padx=0, pady=0)
          self.tkvar_StatsOpr.set('')
          
          self.label_pcntl= tk.Label(self.right_midframe3,text='Percentile')
          self.label_pcntl.grid_propagate(0)
          self.label_pcntl.grid(row=9, column=1, padx=0, pady=0)
       
          self.entry_pcntl= tk.Entry(self.right_midframe3)
          self.entry_pcntl.grid_propagate(0)
          self.entry_pcntl.grid(row=10, column=1,pady=5)
          
          self.label_runwin.config(state='disabled')
          self.entry_runwin.config(state='disabled')
          
          
          if value in self.RUNNINGSPCNTL:
              
              
              self.label_runwin= tk.Label(self.right_midframe3,text='Run. Window size')
              self.label_runwin.grid_propagate(0)
              self.label_runwin.grid(row=11, column=1, padx=0, pady=0)
       
              self.entry_runwin= tk.Entry(self.right_midframe3, text='entry running window size')
              self.entry_runwin.grid_propagate(0)
              self.entry_runwin.grid(row=12, column=1,pady=5)
              
              
     
       elif value in SUBSETTING:
          
           
           self.label_runwin.config(state='disabled')
           self.entry_runwin.config(state='disabled')
           
           self.label_pcntl.config(state='disabled')
           self.entry_pcntl.config(state='disabled')
              
           
          
           self.label_NOffset.grid_forget()
           self.label_size.grid_forget()
           self.label_cutoff.grid_forget()
          
           self.entry_NOffset.grid_forget()
           self.entry_cutoff.grid_forget()
           self.entry_size.grid_forget()
             
           self.label_inTscale.grid_forget()
           self.label_outTscale.grid_forget()
              
           self.popup_inTscale.grid_forget()
           self.popup_outTscale.grid_forget()
              
           self.label_runwin.grid_forget()
           self.entry_runwin.grid_forget()
              
           self.label_inTscale.grid_forget()
           self.label_outTscale.grid_forget()
              

          
          
           self.choices_StatsOpr=['spatial','temporal','spatio-temporal']
           
           self.tkvar_StatsOpr=tk.StringVar(self.right_midframe3)
       
           self.popup_StatsOpr= tk.OptionMenu(self.right_midframe3,self.tkvar_StatsOpr, self.choices_StatsOpr[0],*self.choices_StatsOpr)
           self.popup_StatsOpr.grid(row=4,column=2,padx=0, pady=0)
           self.tkvar_StatsOpr.set('')
          
   def left_frame_level1(self):
       
       
       """The method create buttons and labels for the layer 1 of the left frame
       
       """
              
       self.tk_varRegionCord=tk.IntVar()
       self.tk_varRegionCord.set(2)
       
       
       R0 = tk.Radiobutton(self.left_midframe1, text='Output Region Cord.',variable=self.tk_varRegionCord,value=1,command=self.activate_regionselection)
       R0.grid_propagate(1)
       R0.grid(row=4, column=0, padx=0, pady=25)
       
       R1 = tk.Radiobutton(self.left_midframe1, text='Output Point Cord.',variable=self.tk_varRegionCord,value=2,command=self.activate_pointselection)
       R1.grid_propagate(1)
       R1.grid(row=5, column=0, padx=0, pady=25)
       
       R2 = tk.Radiobutton(self.left_midframe1, text='Use Input Region',variable=self.tk_varRegionCord,value=3,command=self.activate_defaultRegion)
       R2.grid_propagate(1)
       R2.grid(row=6, column=0, padx=0, pady=25)
             
  
   def right_frame_level1(self):
       
       
       """The method create buttons and labels for the layer 1 of the right frame
       
       """
       
             
       label_path = tk.Label(self.left_midframe1, text='Parent Directory')
       label_path.grid_propagate(1)
       label_path.grid(row=0, column=0, padx=0, pady=15)
       

       
       label_regionName = tk.Label(self.left_midframe1, text='Region Name')
       label_regionName.grid_propagate(1)
       label_regionName.grid(row=1, column=0, padx=0, pady=15)
       
       label_directories = tk.Label(self.left_midframe1,text='Sub-directories')
       label_directories.grid_propagate(1)
       label_directories.grid(row=2, column=0, padx=0, pady=25)
       
       
       self.MyText= tk.StringVar()
       
       path_button = tk.Button(self.right_midframe1,text='Browse',command=lambda:self.DisplayDir(self.MyText)) 
       path_button .grid_propagate(1)
       path_button .grid(row=0, column=0, pady=15)
       #self.right_midframe1.bind("<Button-1>",self.DisplayDir)
       path_button.bind("<Button-2>",self.DisplayDir)
       
     
       self.path_ebox = tk.Entry(self.right_midframe1,textvariable=self.MyText)
       self.path_ebox.grid_propagate(1)
       self.path_ebox.grid(row=0, column=2, pady=15)
       
       self.regn_ebox = tk.Entry(self.right_midframe1)
       self.regn_ebox.grid_propagate(1)
       self.regn_ebox.grid(row=1, column=0,pady=15)
       
       #directories
       label_dir = tk.Label(self.right_midframe1, text=' (Semicolon Separated List)')
       label_dir.grid_propagate(1)
       label_dir.grid(row=2, column=0, padx=0, pady=0)
       
       self.dir_ebox = tk.Entry(self.right_midframe1)        
       self.dir_ebox.grid_propagate(1)
       self.dir_ebox.grid(row=3, column=0, pady=0)
               
       label_dircont0 = tk.Label(self.right_midframe1, text=' ')
       label_dircont0.grid_propagate(1)
       label_dircont0.grid(row=1, column=2, padx=0, pady=0)
       
       label_dircont = tk.Label(self.right_midframe1, text='NetCDF Container')
       label_dircont.grid_propagate(1)
       label_dircont.grid(row=2, column=2, padx=0, pady=0)
       
       self.dircont_ebox = tk.Entry(self.right_midframe1, text='Data Container Entry')        
       self.dircont_ebox.grid_propagate(1)
       self.dircont_ebox.grid(row=3, column=2, pady=0)
       
       #region
       
       self.label_xmin = tk.Label(self.right_midframe1, text='Xmin')
       self.label_xmin.grid_propagate(1)
       self.label_xmin.grid(row=5, column=0, padx=0, pady=0)
       
       self.label_xmax = tk.Label(self.right_midframe1, text='Xmax')
       self.label_xmax.grid_propagate(1)
       self.label_xmax.grid(row=5, column=2, padx=0, pady=0)
       
       self.label_ymax= tk.Label(self.right_midframe1, text='Ymax')
       self.label_ymax.grid_propagate(1)
       self.label_ymax.grid(row=4, column=1, padx=0, pady=0)
       
       self.label_ymin= tk.Label(self.right_midframe1, text='Ymin')
       self.label_ymin.grid_propagate(1)
       self.label_ymin.grid(row=6, column=1, padx=0, pady=0)
       
       
       self.xmin_ebox = tk.Entry(self.right_midframe1)
       self.xmin_ebox.grid_propagate(1)
       self.xmax_ebox = tk.Entry(self.right_midframe1)
       self.xmax_ebox.grid_propagate(1)
       self.ymin_ebox = tk.Entry(self.right_midframe1)
       self.ymin_ebox.grid_propagate(1)
       self.ymax_ebox = tk.Entry(self.right_midframe1)
       self.ymax_ebox.grid_propagate(1)
       
       
       self.xmin_ebox.grid(row=6, column=0,pady=0)
       self.xmax_ebox.grid(row=6, column=2,pady=0)
       self.ymin_ebox.grid(row=5, column=1,pady=0)
       self.ymax_ebox.grid(row=7, column=1,pady=0)
       
       #point
       self.label_lon= tk.Label(self.right_midframe1, text='Lon')
       self.label_lon.grid_propagate(1)
       self.label_lon.grid(row=8, column=0, padx=0, pady=10)
       
       self.label_lat= tk.Label(self.right_midframe1, text='Lat')
       self.label_lat.grid_propagate(1)
       self.label_lat.grid(row=8, column=2, padx=0, pady=10)
       
       self.lon_ebox = tk.Entry(self.right_midframe1,text='Lan entry box')
       self.lon_ebox.grid_propagate(1)
       self.lat_ebox = tk.Entry(self.right_midframe1, text='Lat entry box')
       self.lat_ebox.grid_propagate(1)
       
       self.lon_ebox.grid(row=9, column=0,pady=0)
       self.lat_ebox.grid(row=9, column=2,pady=0)       
      
       
       commit_button1=tk.Button(self.right_midframe1,text='Commit',command=lambda:self.consistency_commit1(self))
       commit_button1.grid_propagate(0)
       commit_button1.grid(row=10, column=1,pady=10,padx=0)
       self.right_midframe1.bind("<Button-1>",self.commit1)
       #self.save_button.bind("<Button-1>",self.commit3)

   def left_frame_level2(self):
       
       
       """The method create buttons and labels for the layer 2 of the left frame
       
       """
       
       self.label_filingStyle = tk.Label(self.left_midframe2,text='Filing Style')
       self.label_filingStyle.grid_propagate(0)
       self.label_filingStyle.grid(row=0, column=0, padx=0, pady=10)
              
       self.list_parameters = tk.Label(self.left_midframe2,text='Input Parameter(s)')
       self.list_parameters.grid_propagate(0)
       self.list_parameters.grid(row=1, column=0, padx=0, pady=30)
       
       self.tk_tframevar=tk.IntVar()
       self.tk_tframevar.set(1)
       
       R1 = tk.Radiobutton(self.left_midframe2, text='Time Frame',variable=self.tk_tframevar,value=1,command=self.analysisParameterAnddate_selection)
       R1.grid_propagate(0)
       R1.grid(row=2, column=0, padx=0, pady=20)
       
       R2 = tk.Radiobutton(self.left_midframe2, text='Input Time Frame',variable=self.tk_tframevar,value=2,command=self.specify_DefAnalysisTimeOptions)
       R2.grid_propagate(0)
       R2.grid(row=3, column=0, padx=0, pady=20)
          
         
   def right_frame_level2(self):
       
       
       """The method create buttons and labels for the layer 2 of the right frame
       
       """
       
       self.filing_syle = tk.Label(self.right_midframe2, text='NetCDF Filing Style')
       self.filing_syle.grid_propagate(1)
       self.filing_syle.grid(row=0, column=0, padx=0, pady=0)
              
       choices_filingsyle=['','IN HOUSE','CORDEX']
       
       self.tkvar_filingsyle=tk.StringVar(self.right_midframe3)
       
       popup_filingSty= tk.OptionMenu(self.right_midframe2,self.tkvar_filingsyle, choices_filingsyle[0],*choices_filingsyle)
       popup_filingSty.grid(row=1,column=0,padx=0, pady=10)
       
       self.tkvar_filingsyle.set('')
       
       label_parebox = tk.Label(self.right_midframe2, text='Parameter(s)')
       label_parebox.grid_propagate(1)
       label_parebox.grid(row=2, column=0, padx=0, pady=0)
       
       self.par_ebox = tk.Entry(self.right_midframe2, text='Parameter Entry Box')        
       self.par_ebox.grid_propagate(1)
       self.par_ebox.grid(row=3, column=0, pady=10)
      
       self.label_stdate = tk.Label(self.right_midframe2, text='Start Date')
       self.label_stdate.grid_propagate(1)
       self.label_stdate.grid(row=4, column=0, padx=0, pady=0)
              
       self.label_enddate = tk.Label(self.right_midframe2, text='End Date')
       self.label_enddate.grid_propagate(1)
       self.label_enddate.grid(row=4, column=1, padx=0, pady=0)
       
       self.tmin1 = tk.Entry(self.right_midframe2)
       self.tmin1.grid_propagate(1)
       self.tmax1 = tk.Entry(self.right_midframe2)
       self.tmax1.grid_propagate(1)
       
       self.tmin1.grid(row=5, column=0,pady=0)
       self.tmax1.grid(row=5, column=1,pady=0)
       
       commit_button2=tk.Button(self.right_midframe2,text='Commit',command=lambda:self.consistency_commit2(self))
       commit_button2.grid_propagate(0)
       commit_button2.grid(row=6, column=1,pady=50,padx=0)
       self.right_midframe3.bind("<Button-1>",self.commit2)
       #self.save_button.bind("<Button-1>",self.commit3)
              
   def left_frame_level3(self):
       
       
       """The method create buttons and labels for the layer 3 of the left frame
       
       """
       
       self.lv3_Rdvar=tk.IntVar() # level 3 radio button options variable
       self.lv3_Rdvar.set(1)
       
       self.R1 = tk.Radiobutton(self.left_midframe3, text='User-Def. T-Scale',variable=self.lv3_Rdvar,value=1,command=self.userdefinedtimesets_analysis)
       self.R1.grid_propagate(1)
       self.R1.grid(row=4, column=1, padx=0, pady=20)
              
       self.R2 = tk.Radiobutton(self.left_midframe3, text='Pre-Def. T-scale',variable=self.lv3_Rdvar,value=2,command=self.calenderbased_analysis)
       self.R2.grid_propagate(1)
       self.R2.grid(row=5, column=1, padx=0, pady=20)
       
       self.R3 = tk.Radiobutton(self.left_midframe3, text='Pre-Def. T-Scale (Multi-Yr Run. Avs)',variable=self.lv3_Rdvar,value=3,command=self.calenderbased_multiyearanalysis)
       self.R3.grid_propagate(1)
       self.R3.grid(row=2, column=1, padx=0, pady=20)
       
       self.R4 = tk.Radiobutton(self.left_midframe3, text='Spatio-Temporal Sub-Setting',variable=self.lv3_Rdvar,value=4,command=self.spatioteomporalsubsetting_seletion)
       self.R4.grid_propagate(1)
       self.R4.grid(row=3, column=1, padx=0, pady=20)
       
       
       self.R5 = tk.Radiobutton(self.left_midframe3, text='Pre-Def. T-Scale (Mixed Operators)',variable=self.lv3_Rdvar,value=5,command=self.calenderbased_mixedoperatoranalysiss)
       self.R5.grid_propagate(1)
       self.R5.grid(row=1, column=1, padx=0, pady=20)
       
       
           
       self.R4 = tk.Label(self.left_midframe3, text='Operator')
       self.R4.grid_propagate(1)
       self.R4.grid(row=6, column=1, padx=0, pady=20)               
               
           
           
           
          

            
   def right_frame_level3(self):
       
       """The method create buttons and labels for the layer 3 of the right frame
       
       """
       
       
            
       self.label_NOffset = tk.Label(self.right_midframe3,text='NOffset')
       self.label_NOffset.grid_propagate(1)
       self.label_NOffset.grid(row=1, column=0, padx=0, pady=0)
       
       self.label_size= tk.Label(self.right_midframe3,text='Nsets')
       self.label_size.grid_propagate(1)
       self.label_size.grid(row=1, column=1, padx=0, pady=0)
       
       self.label_cutoff= tk.Label(self.right_midframe3,text='Nskip')
       self.label_cutoff.grid_propagate(1)
       self.label_cutoff.grid(row=1, column=2, padx=0, pady=0)
       
       self.entry_NOffset = tk.Entry(self.right_midframe3,text='NOffset entry')
       self.entry_NOffset.grid_propagate(1)
       self.entry_NOffset.grid(row=2, column=0,padx=0,pady=5)
       
       self.entry_size = tk.Entry(self.right_midframe3, text='Entry Nsets')
       self.entry_size.grid_propagate(1)
       self.entry_size.grid(row=2, column=1,padx=0,pady=5)
                
       self.entry_cutoff = tk.Entry(self.right_midframe3,text='Entry Nskip')
       self.entry_cutoff.grid_propagate(1)
       self.entry_cutoff.grid(row=2, column=2,padx=0,pady=5)
       
             
       self.label_StatsOpr= tk.Label(self.right_midframe3,text='Statistical Operation')
       self.label_StatsOpr.grid_propagate(0)
       self.label_StatsOpr.grid(row=3, column=2, padx=0, pady=0)       
     
       self.label_oprType= tk.Label(self.right_midframe3,text='Operator Type')
       self.label_oprType.grid_propagate(1)
       self.label_oprType.grid(row=3, column=0, padx=0, pady=0)
       
       self.choices_oprtype=['STATS.','RUNNING STATS.','RUNNING PCNTL','MULTI YEAR RUNN. STATS.','MULTI YEAR RUNN. PCNTL.','PCNTL']
       

       
       self.tkvar_opr=tk.StringVar(self.right_midframe3)
       
       self.popup_oprtype= tk.OptionMenu(self.right_midframe3,self.tkvar_opr, self.choices_oprtype[0],*self.choices_oprtype,command=self.stats_func)
       self.popup_oprtype.grid(row=4,column=0,padx=0, pady=0)
       self.tkvar_opr.set('')
              

       
       self.choices_StatsOpr=['']          
       self.tkvar_StatsOpr=tk.StringVar(self.right_midframe3)  
       self.popup_StatsOpr= tk.OptionMenu(self.right_midframe3,self.tkvar_StatsOpr, self.choices_StatsOpr[0],*self.choices_StatsOpr,command=self.Outstats_func)
       self.popup_StatsOpr.grid(row=4,column=2,padx=0, pady=0)
       
       self.label_inTscale= tk.Label(self.right_midframe3,text='Input Time Scale')
       self.label_inTscale.grid_propagate(1)
       self.label_inTscale.grid(row=5, column=0, padx=0, pady=0)
       
       self.label_outTscale= tk.Label(self.right_midframe3,text='Output Time Scale')
       self.label_outTscale.grid_propagate(1)
       self.label_outTscale.grid(row=5, column=2, padx=0, pady=0)
       
       self.tkvar_outTscale=tk.StringVar(self.right_midframe3)
       self.choices_OutTScale=['']
       self.popup_outTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_outTscale, self.choices_OutTScale[0],*self.choices_OutTScale)
       self.popup_outTscale.grid(row=6,column=2,padx=0, pady=0)       
       
      
       self.choices_inTScale=['']
       self.tkvar_inTScale=tk.StringVar(self.right_midframe3)
       
       self.popup_inTscale= tk.OptionMenu(self.right_midframe3,self.tkvar_inTScale, self.choices_inTScale[0],*self.choices_inTScale,command=self.inTScale_func)
       self.popup_inTscale.grid(row=6,column=0,padx=0, pady=0)
       self.tkvar_inTScale.set('')
       
       
       
                  
       #choose sum or mean
       self.tk_ddChoicePCTL=tk.IntVar()
       #self.tk_ddChoicePCTL.set()
       self.C2 = tk.Radiobutton(self.right_midframe3, text='Sum to Daily',variable=self.tk_ddChoicePCTL,value=1)
       self.C2.grid_propagate(0)
       self.C2.grid(row=7, column=1, padx=0, pady=0)
       
       self.C3 = tk.Radiobutton(self.right_midframe3, text='Ave. to Daily',variable=self.tk_ddChoicePCTL,value=2)
       self.C3.grid_propagate(0)
       self.C3.grid(row=8, column=1, padx=0, pady=0)
       
       self.label_pcntl= tk.Label(self.right_midframe3,text='Percentile')
       self.label_pcntl.grid_propagate(0)
       self.label_pcntl.grid(row=9, column=1, padx=0, pady=0)
       
       self.entry_pcntl= tk.Entry(self.right_midframe3, text='entry pecentile')
       self.entry_pcntl.grid_propagate(0)
       self.entry_pcntl.grid(row=10, column=1,pady=5)
       
       self.label_runwin= tk.Label(self.right_midframe3,text='Run. Window Size')
       self.label_runwin.grid_propagate(0)
       self.label_runwin.grid(row=11, column=1, padx=0, pady=0)
       
       self.entry_runwin= tk.Entry(self.right_midframe3, text='Entry Running Window Size')
       self.entry_runwin.grid_propagate(0)
       self.entry_runwin.grid(row=12, column=1,padx=0,pady=5)
                  
       self.save_button=tk.Button(self.right_midframe3,text='Commit',command=lambda:self.consistency_commit3(self))
       self.save_button.grid_propagate(0)
       self.save_button.grid(row=13, column=1,padx=0,pady=20)
       self.right_midframe3.bind("<Button-1>",self.commit3)
       #self.save_button.bind("<Button-1>",self.commit3)
                           

                                                    
   def left_canvasframes(self):
       
       
       
       """The function create three sub-frames within a parent and three title frames
         on the left main.
          The parent_frame span the canvas.
 
                 +---------------------------------+---------------------+
                 |        titile frm 1             |                     |
                 +--------------+------------------+                     |
                 |left mid frm1 | right mid frm 1  |                     | 
                 +--------------+------------------+                     |
                 |        titile frm 2             |                     |
                 +--------------+------------------+                     |
                 |left mid frm2 | right mid frm 2  |                     | 
                 |              |                  |                     |
                 +--------------+------------------+---------------------+
                 |        titile frm 3             |                     |
                 +--------------+------------------+                     |
                 |left mid frm3 | right mid frm 3  |   xterm embedded    | 
                 |              |                  |                     |
                 +--------------+------------------+                     |
                 |        bottom frm               |                     |
                 +---------------------------------+---------------------+

       The frames are denoted by frames
        
       """
       
       self.canvasAndMainFrame()
       #parent frame is the left canvas main frame
       
       self.title_frame1 = tk.Frame(self.Parent_frame,width=840, height=20, background='gray',relief=tk.RAISED)
       self.title_frame1.grid_propagate(1)
       self.title_frame1.grid(row=0, column=0)
       
       self.mid_frame1 = tk.Frame(self.Parent_frame,width=840, height=400, background='gray')
       self.mid_frame1.grid_propagate(0)
       self.mid_frame1.grid(row=2, column=0) 
       
       #layer 1
              
       self.left_midframe1 = tk.Frame(self.mid_frame1,width=280, height=400, background='blue')
       self.left_midframe1.grid_propagate(0)
       self.left_midframe1.grid(row=0, column=0)

       self.right_midframe1 = tk.Frame(self.mid_frame1,width=620, height=400)
       self.right_midframe1.grid_propagate(0)
       self.right_midframe1.grid(row=0, column=1)
              
        #leyer2 
       self.title_frame2 = tk.Frame(self.Parent_frame,width=840, height=20, background='gray',relief=tk.RAISED)
       self.title_frame2.grid_propagate(1)
       self.title_frame2.grid(row=3, column=0,)
       
       self.mid_frame2 = tk.Frame(self.Parent_frame,width=840, height=280, background='gray')
       self.mid_frame2.grid_propagate(0)
       self.mid_frame2.grid(row=4, column=0) 
       
       self.left_midframe2 = tk.Frame(self.mid_frame2,width=280, height=280, background='blue')
       self.left_midframe2.grid_propagate(0)
       self.left_midframe2.grid(row=0, column=0)

       self.right_midframe2 = tk.Frame(self.mid_frame2,width=620, height=280)
       self.right_midframe2.grid_propagate(0)
       self.right_midframe2.grid(row=0, column=1)
       
       #layer 3
       self.title_frame3 = tk.Frame(self.Parent_frame,width=840, height=20, background='gray',relief=tk.RAISED)
       self.title_frame3.grid_propagate(0)
       self.title_frame3.grid(row=5, column=0,)
       
       self.mid_frame3 = tk.Frame(self.Parent_frame,width=840, height=580, background='gray')
       self.mid_frame3.grid_propagate(0)
       self.mid_frame3.grid(row=6, column=0) 
       
       
       self.left_midframe3 = tk.Frame(self.mid_frame3,width=280, height=580, background='blue')
       self.left_midframe3.grid_propagate(0)
       self.left_midframe3.grid(row=0, column=0)

       self.right_midframe3 = tk.Frame(self.mid_frame3,width=620, height=580)
       self.right_midframe3.grid_propagate(0)
       self.right_midframe3.grid(row=0, column=1)
       
       self.bottom_frame = tk.Frame(self.Parent_frame,width=840, height=4, background='gray',relief=tk.RAISED)
       self.bottom_frame.grid_propagate(1)
       self.bottom_frame.grid(row=7, column=0)
       
   def spatial_temporal_analysispage(self):
       
       tk.Frame.__init__(self, self.master)
       
       
       self.left_canvasframes()
       self.menu_bar()
       self.create_allcanvasbuttons()

   def menu_bar(self):
       
       
       """The mothod implements the menu bar and adds all the menu commands
       
       """
       
       
       
       self.master.menu_bar=tk.Menu()

       self.file_list=tk.Menu(self)
       
      
       self.menu=tk.Menu(self)
       self.master.config(menu=self.menu)
       
       self.menu.add_cascade(label="File", menu=self.file_list)
       
       self.menu.add_command(label="Build",command=self.save_all)
       self.menu.add_command(label="Terminal",underline=1, command=self.embedUNIX_termianl2)
       
       H0=tk.Frame(self.canvas_rightTP, height=300,width=540)
       H=tk.Frame(self.canvas_rightTP, height=30,width=540)
       H0.grid(row=0,column=0,padx=0)
       H.grid(row=1,column=0,padx=0)
       tk.Label(H,text="/dev/pts/").grid(row=0,column=0,padx=0)
       self.tty_index = tk.Entry(H,width=6)
       self.tty_index.insert(0, "1")
       self.tty_index.grid(row=0,column=2)
       
       b = tk.Button(H,text="RUN", command=self.send_entry_to_terminal)
       b.grid(row=0,column=4)
       
       
       
     
     
       
   def send_entry_to_terminal(self,*args):
      """*args needed since callback may be called from no arg (button)
      or one arg (entry)
      """
      command="./core.sh"
      #command="ls -l"
      tty="/dev/pts/%s" % self.tty_index.get()
      cmd("%s <%s >%s 2> %s" % (command,tty,tty,tty))
       
   def embedUNIX_termianl2(self):
       
        
       """The function embed a unix terminal

       """
       root =tk.Tk()
       
       f=tk.Frame(root)
       tk.Label(f,text="/dev/pts/").grid(row=0,column=0,padx=0)
       self.tty_index = tk.Entry(f,width=6)
       self.tty_index.insert(0, "1")
       self.tty_index.grid(row=0,column=2)
             
       f.grid(row=0,column=1)
       b2 = tk.Button(f,text="RUN", command=self.send_entry_to_terminal)
       b2.grid(row=0,column=3)
      
       self.termf = tk.Frame(root, height=1200,width=1200)
       self.termf.grid(row=1,column=1)
       wid = self.termf.winfo_id()
       #subprocess.Popen('xterm -into %d -geometry 540x300 -sb & ' % wid,shell=True)
       cmd('xterm -into %d -geometry 160x50 -sb -e "tty; sh" &' % wid)
       
   def embedUNIX_termianl(self):

       """The function embed a unix terminal

       """
       self.termf = tk.Frame(self.canvas_rightBTM, height=300,width=540)
       self.termf.grid(row=1,column=1)
       wid = self.termf.winfo_id()
       #subprocess.Popen('xterm -into %d -geometry 540x300 -sb & ' % wid,shell=True)
       cmd('xterm -into %d -geometry 160x50 -sb -e "tty; sh" &' % wid)
       
   def canvasAndMainFrame(self):
       
       """This function creates the canvases for the main page of the app.
       The layout of the canvas is demonstrated bellow:  
                         
                         
      +----------+---------------------------------+----------------------+
      |          |column 1                         |    coumn 2           |
      +----------+---------------------------------+----------------------+
      | row 1    |left canvas                      |    Top right canvas  |
      | row 2    |                                 |    Bottom canvas     |
      +----------+---------------------------------+----------------------+  
      
       In this case the sub-frames are demonstrated by star bound regions               
                      
       """
       
       #left canvas covers the page from top to bottom
       self.canvas_left = tk.Canvas(self.master)                          
       self.Parent_frame = tk.Frame(self.canvas_left) #left main frame
       self.vsb = tk.Scrollbar(self.master, orient="vertical", command=self.canvas_left.yview)
       self.canvas_left.configure(yscrollcommand=self.vsb.set,width=840,height=840)
       self.canvas_left.grid_propagate(1)
       self.vsb.grid(row=0, column=1,sticky=tk.NS)
       self.canvas_left.grid(row=0, column=0)
       self.canvas_left.create_window((4,4), window=self.Parent_frame, anchor="nw",  tags="self.Parent_frame")
       self.Parent_frame.bind("<Configure>", self.scrollbar_configure)
       
       
       
       # right canvas has two sub-canvus
       self.canvas_right = tk.Canvas(self.master, width=540,height=540, background="#ffffff")
       self.Parent_frame0 = tk.Frame(self.canvas_right,background="gray")
       self.canvas_right.grid_propagate(1)
       self.Parent_frame0.grid(row=0, column=2)
       self.canvas_right.grid(row=0, column=2)
       
       #top canvas
       self.canvas_rightTP = tk.Canvas(self.canvas_right,width=540,height=230)
       self.canvas_rightTP.grid(row=0, column=2)
       
       #bottom canas
       self.canvas_rightBTM = tk.Canvas(self.canvas_right,width=540,height=520)
       self.canvas_rightBTM.grid_propagate(1)
       self.canvas_rightBTM.grid(row=1, column=2)
       self.embedUNIX_termianl()
            
   def configure_gui(self):
      
       self.master.title('Data Processing Pipeline')
       self.master.geometry("1200x600")
         
       self.master.resizable(1, 1)
       
   
   def scrollbar_configure(self, event):
        """Reset the scroll region to encompass the inner frame

        """
        self.canvas_left.configure(scrollregion=self.canvas_left.bbox("all"))
if __name__ == '__main__':
   
   app = PageTwo()
   
   app.mainloop()
   
