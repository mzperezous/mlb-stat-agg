from download_yearly_files import download_year_eve
import os

def test_download_year_eve():
    output = download_year_eve(2005)
    cwd = os.getcwd()
    assert output == f'{cwd}/2005eve.zip'