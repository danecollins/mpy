@echo off

call :cleanup

copy 61.9_prior_reports\61-9_2012.01.31.txt input_61-9.txt

echo starting initial processing
c:\python27\python.exe readinput.py
echo Starting account allocations
c:\python27\python.exe post_process_output.py
c:\python27\python.exe simplify.py
ren output_simple.csv output_2012.01.31.csv

exit






:cleanup

if exist output.csv       del output.csv
if exist output_split.csv del output_split.csv
if exist input_61-9.txt   del input_61-9.txt
exit /b