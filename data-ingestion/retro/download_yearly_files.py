#!/usr/bin/env python3
"""
    Download and unzip year-by-year files from RetroSheet.

    Data: Historical game event level
"""

import sys
import getopt
import os
import requests
from zipfile import ZipFile


def download_year_eve(year):

    thisdir = os.path.dirname(os.path.abspath(__file__))
    basename = f'{year}eve.zip'

    zipdir = f'{thisdir}/.zip'
    filename = f'{zipdir}/{basename}'
    if not os.path.isfile(zipdir):
        os.makedirs(zipdir, exist_ok=True)
    url = f'https://www.retrosheet.org/events/{basename}'

    datadir = f'{thisdir}/.data'

    try:
        print(f'Downloading EVE from {year}...')
        # Download the ZIP
        response = requests.get(url)
        open(filename, 'wb').write(response.content)

        # Unzip to ./.data/<year>
        year_dir = f'{datadir}/{year}'
        if os.path.isfile(year_dir):
            os.rmdir(year_dir)
        with ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(year_dir)

        return True
    except Exception as e:
        print(e)
        print(f'Couldn\'t download .eve file for {year}')
        return False


def download_year_range_eve(start_year, end_year):

    for year in range(start_year, end_year + 1):
        success = download_year_eve(year)

        if not success:
            print(f'Failed downloading {year} EVE.')


if __name__ == "__main__":
    argv = sys.argv[1:]
    start = 1999
    end = 2021

    try:
        options, args = getopt.getopt(argv, 'f:l', ['first=', 'last='])

        for opt, arg in options:
            if opt in ('-f', '--first'):
                start = int(arg)
            elif opt in ('-l', '--last'):
                end = int(arg)

        download_year_range_eve(start, end)
        sys.exit(0)

    except getopt.GetoptError:
        error_message = "Usage: download_yearly_files.py [-f | --first year1] [-l | --last year2]\n"
        error_message += "\t-f or --first\n\t\t year1: First year to pull\n"
        error_message += "\t-l or --last\n\t\t year2: Last year to pull"
        print(error_message)

        sys.exit(1)

