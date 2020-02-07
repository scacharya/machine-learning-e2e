import pandas as pd
import datatable as dtbl
import urllib.error as ue


"""
The class file to encapsulate **ALL** type of data sources
The datatable import $ pip install datatable. If this command fails for newer version of python then
 Run following directly from git repo $ pip install git+https://github.com/h2oai/datatable
"""

class MLE2EDS:

    def __init__(self, source):
        self.data_source = source
        self.data_frame = None
        self.data_table = None


    """
    Assuming the source string as https://some-site.com/data/file-name.ext
    1) check if the soruce string ends with .csv, then read it as is(remote or local) 
    2) for other file types, tgz, zip or .gzip, then a)download b) extract and c) read to dataframe 
    """

    def read_df_csv(self):
        if self.data_source.upper().endswith(".CSV"):
            try:
                self.data_frame = pd.read_csv(self.data_source)
                return self.data_frame
            except ue.URLError as urlerr:
                print("URLError occurred trying to connect", urlerr)
        else:
            print("only .csv files are supported, use datatable instead ")


    """
    datatable reads much faster, file with multiple delimeter and different format
    """
    def read_datatable(self):
        self.data_table=dtbl.fread(self.data_source)
        return self.data_table


    def show_summary(self):
        pass