@echo off

if exist output.txt del output.txt

c:\python27\python.exe ..\findCombinedOrders.py findCombinedTestInput.csv > output.txt
echo ---------------------------------------------
fc output.txt findCombinedTestOutput.txt
