@echo off

if exist output.csv del output.csv
if exist logfile.txt del logfile.txt

c:\python27\python.exe readinput.py %1% > logfile.txt

Notepad logfile.txt
