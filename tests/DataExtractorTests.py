import unittest
import os
import pandas as pd

from core.backend import DataExtractor


class DataExtractorTests(unittest.TestCase):

    def setUp(self):
        self.data_extractor = DataExtractor(['Late_shifts.csv', 'Missed_meds.csv', 'Missed_Shifts.csv'])

    def test_reader_valid_files(self):
        expected_file_list = ['Late_shifts.csv', 'Missed_meds.csv', 'Missed_Shifts.csv']
        file_list = self.data_extractor.reader()

        self.assertEqual(file_list, expected_file_list)

    def test_reader_invalid_file(self):
        self.data_extractor.files.append('non_existent_file.csv')
        file_list = self.data_extractor.reader()

        self.assertEqual(len(file_list), 3)
        # self.assertIn('Failed to process file: non_existent_file.csv.', print(file_list))

    def test_filter_young_persons(self):
        with open('young_person.txt', 'w') as yp_file:
            yp_file.write('casper moyo\n')
            yp_file.write('Lola James\n')

        filtered_file_list = self.data_extractor.filter()

        self.assertEqual(len(filtered_file_list), 3)

    def test_add_young_person(self):
        young_persons_list = self.data_extractor.add_young_person('casper moyo')

        self.assertEqual(young_persons_list[-1], 'casper moyo')

    def test_delete_young_person(self):
        with open('young_person.txt', 'w') as yp_file:
            yp_file.write('casper moyo\n')
            yp_file.write('Lola James\n')

        updated_young_persons_list = self.data_extractor.delete_young_person('Lola James')

        self.assertEqual(len(updated_young_persons_list), 1)
        self.assertNotIn('Lola James', updated_young_persons_list)


if __name__ == '__main__':
    unittest.main()
