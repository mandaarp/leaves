__author__ = 'mandar'

import unittest
from maple_leave import main

class TestMapleLeave(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_files(self):
        actual_list = main.load_files(path=main.TEST_FOLDER)
        self.assertEqual(len(actual_list), 1)