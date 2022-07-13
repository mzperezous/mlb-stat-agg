"""
    Download and unzip year-by-year files from RetroSheet.

    Data: Historical game event level
"""

import os
import requests

def download_year_eve(year):
    cwd = os.getcwd()
    basename = f'{cwd}/{year}eve.zip'
    return basename