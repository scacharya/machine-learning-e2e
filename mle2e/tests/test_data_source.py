import unittest
import mle2e.data_source as ds

if __name__ == '__main__':
    unittest.main()


class TestMLE2EDS (unittest.TestCase):

    def setUp(self) -> None:
        self.datasource = ds.MLE2EDS("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

    def test_read_df_csv(self):
        country_expected = 'Algeria'
        region_expected = 'AFRICA'
        this_df = self.datasource.read_df_csv()
        self.assertEqual(country_expected, this_df.Country[0], "Countries compared")
        self.assertEqual(region_expected, this_df.Region[0], "Region compared")

    def test_read_datatable(self):
        country_expected = 'Algeria'
        region_expected = 'AFRICA'
        this_dtbl = self.datasource.read_datatable()
        self.assertEqual(country_expected, this_dtbl[0,0], "Countries compared")
        self.assertEqual(region_expected, this_dtbl[0,1], "Region compared")

    def tearDown(self) -> None:
        self.datasource = None