@echo off

if exist output.csv del output.csv

c:\python27\python.exe readinput.py testinput0.txt
echo ---------------------------------------------
fc output.csv testoutput0.csv

if exist output.csv del output.csv

c:\python27\python.exe readinput.py testinput1.txt
echo ---------------------------------------------
fc output.csv testoutput1.csv