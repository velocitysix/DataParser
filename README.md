# DataParser

This repo contains two files. 

The NetlistParser.PY file allows data to be parsed via input of (Netlist Report). After parsing the data, 
the script will analzye differences between old reports and new reports and output a file with nets that were removed from the schematic
or nets that were newly added to the schematic. 


 Plotter.py

The plotter script allows you to visualzie data points outputted by a Rumba. Using its sensors, rumbas will output coordinates of where it thinks obsticles are. 
Using my program, you are able to parse the outputted X,Y coordinate data- plot in polar form, and visualize in real time where obstacles might be. 
