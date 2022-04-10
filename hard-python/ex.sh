#!/usr/bin/env bash

# Generates a folder containing template file for exercises

if [[ $# -ne 1 ]]
then
    echo "Usage: ./ex.sh folder_name"
else
    mkdir $1 && cd $1 && cp ../main.py ./main.py   
fi

