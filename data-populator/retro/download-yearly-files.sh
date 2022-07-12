#!/bin/bash
START_YEAR=1995
END_YEAR=2013 # TODO: 2022

# Handle directories
if [ ! -d .data ]; 
then 
    mkdir .data
else
    rm -rf .data
    mkdir .data
# TODO: Handle other possible cases
fi

if [ ! -d tmp ]; 
then 
    mkdir tmp 
else
    rm -rf tmp
    mkdir tmp
fi

for (( YEAR = ${START_YEAR}; YEAR <= ${END_YEAR}; YEAR++ ))
do
    wget https://www.retrosheet.org/events/${YEAR}eve.zip -O tmp/${YEAR}eve.zip
    rm -rf .data/${YEAR} # TODO: Remove
    mkdir .data/${YEAR}
    unzip tmp/${YEAR}eve.zip .data/${YEAR}
done
