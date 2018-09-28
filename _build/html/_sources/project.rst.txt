Project Summary
===============

Climate data pipeline is a collection of scripts based on bash and R programming language for processing of climate data. The climate data pipeline makes use of statistical and alrithmetic functions, data selection and sampling tools as well as spatial interpolation processing capabilities availed in th Climate Data Operator (CDO) and R raster package. The present version of the pipeline is most suited for processing of Climate model outputs and forecasts.


Goals:
______

To enable:
 
* easy reproducibility of analyis.
* sharing of climate data analysis protocols
* semi-automation of repeatative climate data analysis tasks
* Interactive visualization of analysis steps within a single platform.
* conversion of data from various data formats to NetCDF format and standardised naming conventions and allow capturing of metadata associated with various data versions.

Key Compontents:
________________

The climate data operator consists of:
	
* a graphical user interface (GUI) which can be used in two ways:
   * to generate a text user interface (TUI)
   * to execute the pipeline sub-scrits

* a collection of shell scripts which can be prompted through the user interfact or
  by running the parent shell scripts or core.

Usage:
______

The pipeline presenly work on a linux operating system. 
To access the CDO operators the user has to install:

1) CDO compinelled with NetCDF support
2) python and tkinter
3) xterm unix terminal

Python and tkinter is mostly need for the GUI.
In the case of analysis done on a remote servor, the GUI may be used to
generate the TUI which will be submitted along with the input scripts.






