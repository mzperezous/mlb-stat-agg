import download_yearly_files
import os


def test_download_year_eve():
    outdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    tmpdir = f'{outdir}/tmp'
    filename = f'{outdir}/tmp/2005eve.zip'

    datadir = f'{outdir}/.data/2005'

    # Handle tmp and data dirs
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        if not os.path.isfile(tmpdir):
            os.makedirs(tmpdir, exist_ok=True)

    if not os.path.isfile(datadir):
        os.makedirs(datadir, exist_ok=True)

    # Run test
    download_yearly_files.download_year_eve(2005)

    # Check for file
    assert os.path.isfile(filename)


def test_download_and_process_years():
    outdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    datadir = f'{outdir}/.data'

    for i in range(2005, 2013):
        year_dir = f'{datadir}/{i}'
        if os.path.isfile(year_dir):
            os.remove(year_dir)

    download_yearly_files.download_year_range_eve(2005, 2012)
    for i in range(2005, 2013):
        year_dir = f'{datadir}/{i}'
        print(year_dir)
        assert os.path.exists(year_dir)

