"""
Utility to consolidate the data into a single class for step #1) Data Understanding in  CRIPS-DM methodology
"""

from mle2e import data_source as ds

DATA_URL = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
data_source = ds.MLE2EDS(DATA_URL)

data_source.show_summary()