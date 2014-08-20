@echo off
echo.

if [%1]==[] GOTO USAGE

echo copying Guided Help to MWO tree at: %1

set dest=%1\ghs

if NOT EXIST %dest% mkdir %dest%


copy  ..\server.py %dest%
copy  ..\index.html %dest%

if NOT EXIST %dest%\abi mkdir %dest%\abi
copy  ..\abi\*.py %dest%\abi
if NOT EXIST %dest%\css mkdir %dest%\css
copy  ..\css\*.css %dest%\css

copy ..\vb\Start_GH_Server.bas %1%\scripts

GOTO END

:USAGE

echo USAGE: copyto "mwo_install_dir"
echo        must be installed into MWO_install_dir

:END