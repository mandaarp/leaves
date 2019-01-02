__author__ = 'mandar'

import unittest, sys
from maple_leave import main

class TestMapleLeave(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def get_stdout(self):
        if not hasattr(sys.stdout, 'getvalue'):
            self.fail('Need to run in buffered mode.')
        return sys.stdout.getvalue().strip()

    def test_load_files(self):
        actual_list = main.load_files(path=main.TEST_FOLDER)
        self.assertEqual(len(actual_list), 1)
        self.assertTrue('Error: Invalid MP3' in self.get_stdout())

    def test_print_values(self):
        expected_tag = 'tag'
        expected_original_text = 'original'
        expected_new_text = 'new'
        main.print_values(tag=expected_tag, original_text=expected_original_text, new_text=expected_new_text)
        actual_output = self.get_stdout()
        self.assertEqual(actual_output, '{0} > {1} > {2}'.format(expected_tag, expected_original_text, expected_new_text))