#!/bin/bash
DIR=$(pwd)
DATA_DIR=${DIR}/.data
TMP_DIR=${DIR}/tmp
START_YEAR=1995
END_YEAR=2013 # TODO: 2022

# Handle directories
if [ ! -d ${DATA_DIR} ]; 
then 
    mkdir ${DATA_DIR}
else
    rm -rf ${DATA_DIR}
    mkdir ${DATA_DIR}
# TODO: Handle other possible cases
fi

if [ ! -d ${TMP_DIR} ]; 
then 
    mkdir ${TMP_DIR} 
else
    rm -rf ${TMP_DIR}
    mkdir ${TMP_DIR}
fi

for (( YEAR = ${START_YEAR}; YEAR <= ${END_YEAR}; YEAR++ ))
do
    wget https://www.retrosheet.org/events/${YEAR}eve.zip -O ${TMP_DIR}/${YEAR}eve.zip
    rm -rf ${DATA_DIR}/${YEAR} # TODO: Remove
    mkdir ${DATA_DIR}/${YEAR}
    unzip ${DATA_DIR}/${YEAR}eve.zip ${DATA_DIR}/${YEAR}
done
