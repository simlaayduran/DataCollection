import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
from src import clean
import json


class CleanTest(unittest.TestCase):
    # def setUp(self):
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
        

    def test_title(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_1.json", "./data/result1.json")
        self.assertEquals(0, os.stat("./data/result1.json").st_size) 

    def test_2(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_2.json", "./data/result2.json")
        self.assertEquals(0, os.stat("./data/result2.json").st_size)

    def test_3(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_3.json", "./data/result3.json")
        self.assertEquals(0, os.stat("./data/result3.json").st_size)

    def test_4(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_4.json", "./data/result4.json")
        self.assertEquals(0, os.stat("./data/result4.json").st_size)

    def test_5(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_5.json", "./data/result5.json")
        self.assertEquals(0, os.stat("./data/result5.json").st_size)

    def test_6(self):
        # Just an idea for a test; write your implementation
        clean.main("./test/fixtures/test_6.json", "./data/result6.json")
        with open("./data/result6.json", 'r') as f:
            w = json.load(f)

        self.assertEquals(["nba","basketball", "game", "soccer"], w["tags"])  
        
    
if __name__ == '__main__':
    unittest.main()