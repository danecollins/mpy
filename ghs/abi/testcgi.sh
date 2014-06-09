#!/bin/bash

command=$1
vars=$2
#echo 'Command = ' $command
#echo 'Args    = ' $vars

QUERY_STRING=$vars
export QUERY_STRING

echo $QUERY_STRING

python3 $command

