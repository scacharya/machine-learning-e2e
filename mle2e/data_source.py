import pandas as pd
from mle2e import DataTypes as dt

"""
The class file to encapsulate **ALL** type of data sources
"""

class MLE2EDS:

    def __init__(self, source):
        self.data_source = source

    """
    Assuming the source string as https://some-site.com/data/file-name.ext
    1) check if the soruce string ends with .csv, then read it as is(remote or local) 
    2) for other file types, tgz, zip or .gzip, then a)download b) extract and c) read to dataframe 
    """

    @property
    def get_data(self):
        if self.data_source.upper().endswith(".CSV"):
            return pd.read_csv(self.data_source)
        else:
            pass
            ##Read for other files like tgz, zip gzip etc
            ##"if the file does not exist locally, then download and extract it"
            ##if extracted file is csv, read it
            ## if extracted file is text with speficic delimeter, then read it accordingly

    """
    datatable reads much faster, file with multiple delimeter and different format
    """
    def get_data_table(self):
        return dt.fread(self.data_source)


