import unittest
import mle2e.data_source as ds
from mle2e import DataTypes as dt

if __name__ == '__main__':
    unittest.main()


class TestCSVDS (unittest.TestCase):
    def test_get_data(self):
        country_expected = 'Algeria'
        region_expected = 'AFRICA'

        datasource = ds.MLE2EDS("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")
        mydf = datasource.get_data
        country_actual = mydf.Country[0]
        region_actual = mydf.Region[0]

        self.assertEqual(country_expected, country_actual, "Countries compared")
        self.assertEqual(region_expected, region_actual, "Region compared")
