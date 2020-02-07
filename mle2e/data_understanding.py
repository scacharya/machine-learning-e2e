"""The file is contains utility classes and methods to read data and run some basic data checks

"""

#This file has dependency to following python libraries:
#  Pandas, Numpy, sklearn,


from mle2e import DataTypes as dt
from mle2e import data_source as ds
import urllib.error as ue


try:
    #mydf = ds.retrieve_data("https://raw.githubusercontent.com/cs109/2014_data/master/", "countries.csv", dt.CSV)
    mydf = ds.MLE2EDS("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv").get_data

    print(mydf.head())
except ue.URLError as urlerr:
    print("URLError occurred trying to connect", urlerr)

