#!/bin/bash

for YEAR in {1915..2021}
do
    wget https://www.retrosheet.org/events/${YEAR}eve.zip -O tmp/${YEAR}eve.zip
    rm -rf .data/${YEAR} # TODO: Remove
    mkdir .data/${YEAR}
    unzip tmp/${YEAR}eve.zip .data/${YEAR}
done