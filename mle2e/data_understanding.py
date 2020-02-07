"""The file is contains utility classes and methods to read data and run some basic data checks

"""

#This file has dependency to following python libraries:
#  Pandas, Numpy, sklearn,


from mle2e import DataTypes as dt

from mle2e import data_source as ds


mydf = ds.retrieve_data("https://raw.githubusercontent.com/cs109/2014_data/master/", "countries.csv", dt.CSV)

print(mydf)