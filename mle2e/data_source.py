import datatable as dtbl
import os as os
from pathlib import Path
import zipfile, urllib.request, shutil, tarfile

"""
The file handles **ALL** type of data sources (wish list)
The datatable import $ pip install datatable. If this command fails for newer version of python then
 un following directly from git repo $ pip install git+https://github.com/h2oai/datatable
"""


"""
Utility to get data based on various operation 
This function is only needed for the calling functions and pass the *known* data source
DATA_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"
"""
def get_data(file_name):
    check_data_dir()
    return check_data_file(file_name)


"""
check if data directory exists under the workspace, create one if it does not
"""
def check_data_dir():
    thispath = os.getcwd()+"/data"
    if not os.path.exists(path=thispath):
        os.makedirs(thispath, 0o777, False )


"""
check if the data file already exists locally, if not download
if the downloaded data is compressed, decompress it
"""
def check_data_file(url):
    if url.upper().endswith(".ZIP") or url.upper().endswith(".TGZ"):
        return check_and_download_acrhive_file(url)
    elif url.upper().endswith(".CSV"):
        return check_and_download_csv_file(url)
    else:
        pass

"""
check for remote zip files, download and extract if does not exist locally
"""
def check_and_download_acrhive_file(someurl):
    url_split = someurl.split("/")
    last_elem = len(url_split)-1
    file_to_download = url_split[last_elem]
    datadir = os.getcwd() + "/data/"
    file_path = Path(datadir+file_to_download)
    if file_path.is_file():
        print("File exists in data directory, not downloading")
    else:
        print("File does not exist in data directory, downloading and extracting...")
        if someurl.upper().endswith(".ZIP"):
            with urllib.request.urlopen(someurl) as response, open(file_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                with zipfile.ZipFile(file_path) as zf:
                    os.chdir(datadir)
                    zf.extractall()
        elif someurl.upper().endswith(".TGZ"):
            with urllib.request.urlopen(someurl) as response, open(file_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
                tar = tarfile.open(datadir+file_to_download, 'r')
                os.chdir(datadir)
                for item in tar:
                    tar.extract(item)
        else:
            pass
    return file_path

"""
Check and download csv 
"""
def check_and_download_csv_file(url):
    url_split = url.split("/")
    last_elem = len(url_split) - 1
    file_to_download = url_split[last_elem]
    datadir = os.getcwd() + "/data/"
    file_path = Path(datadir + file_to_download)
    response = urllib.request.urlopen(url)
    with open(os.path.join(datadir, file_to_download), 'w+b') as f:
        f.write(response.read())
    return file_path

"""
Read the file using datatable 
"""
def load_data(filename):
    ##try opening .csv file instad
    try:
        filetoopen = str(filename).replace(".tgz", ".csv",1)
        data_table = dtbl.fread(filetoopen, fill=True)
        return data_table
    except RuntimeError as re:
        print("Unable to read the file into datatable, trying to downlaod", re)