"""
    Download and unzip year-by-year files from RetroSheet.

    Data: Historical game event level
"""

import os
import requests
from zipfile import ZipFile


def download_year_eve(year):

    thisdir = os.path.dirname(os.path.abspath(__file__))
    basename = f'{year}eve.zip'

    tmpdir = f'{thisdir}/tmp'
    filename = f'{tmpdir}/{basename}'
    if not os.path.isfile(tmpdir):
        os.makedirs(tmpdir, exist_ok=True)
    url = f'https://www.retrosheet.org/events/{basename}'

    datadir = f'{thisdir}/.data'

    try:
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

