"""
Utility to consolidate the data into a single class for step #1) Data Understanding in  CRIPS-DM methodology
"""
from mle2e import data_source as ds

DATA_URL = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
DATA_URL = "https://ndownloader.figshare.com/files/5976036"
DATA_URL = "http://lib.stat.cmu.edu/datasets/houses.zip"
DATA_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"

local_file = ds.get_data(DATA_URL)
summary_dtbl = ds.load_data(local_file)
print(summary_dtbl.to_pandas().head())