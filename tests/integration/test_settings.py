import unittest
from settings import Settings
from os import path
import random
import string

class TestSettings(unittest.TestCase):
    # def setUp(self):
        
    def test_it_creates_a_config_file_on_the_home_directory_on_init(self):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(5))
        Settings("./tmp/" + result_str)

        self.assertTrue(path.exists("./tmp/" + result_str))



        

