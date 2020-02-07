import mle2e
import pandas as pd
import os
import tarfile
import urllib
from mle2e import DataTypes as dt


# SOURCE = "http://lib.stat.cmu.edu/datasets/"
SOURCE = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
FILE_NAME = "housing.tgz"
LOCAL_DIR = "/Users/acharysx/projects/data/tempdir"



##check if the housing/housing.csv file already exists locally,if yes read it to data frame
# if not, check if housing/housing.tgz file exists in the location, unzip it and read it to data frame
## else dowinlad the file, extract and read it to dataframe


def fetch_remote(url, filename):
    pass


def read_csv_file(csv_file_name):
    pass


def extract_file(compressedFile):
    pass

"""
def check_file(path_name):
    # chceck if localdir directory exists
    return os.path.isfile(path_name)


print("file" , LOCAL_DIR,  "exists?", check_file(LOCAL_DIR))

dir= os.path.join("../", "/tempdir")
os.chdir("/tmp")
if not os.path.exists(dir):
    os.makedirs(dir, 777, exist_ok=True)

"""
class ADS:
    def __init__(self, source, dbobj):
        self.datasource = source
        self.dataobject = dbobj

class CSVDS(ADS):

    def __init__(self, source, dbobj, type):
        super().__init__(source, dbobj)
        self.datatype=type

    def get_data(self):
        print("1. csvds.get_data",self.datasource,self.dataobject)
        data_loc = self.datasource + self.dataobject
        print("2. data_loc=", data_loc)
        data_frame= pd.read_csv(data_loc)
        print(data_frame)
        return data_frame

def retrieve_data(ds, dbobj, type):

    print("starting retrieve_data")
    if type == dt.CSV:
        print("in retrieve_data type=", type)
        ds = CSVDS(ds, dbobj, type)
        print("===>>>in retrieve_data datasource=", ds)
        df = ds.get_data()
        print("===>>>in retrieve_data dataframe=", df)
        return df


