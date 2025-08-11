import unittest

from jb_60.function_example.utils import utils


class multipleExample(unittest.TestCase):
    def setUp(self):
        print('into set up')
        self.num1=1
        self.num2=2

    def test_add(self):
        utils()
        print('testing summery')


        assert self.num1+self.num2==3,'the summery of 1 and 2 is not 3'

    def test_minus(self):
        print('testing diff')


        assert self.num1-self.num2==3 ,'the diff of 4 and 1 is not 3'
    def test_multiple_with_error(self):


        assert self.num1*self.num2==5 , 'the result of multiple action is not as expected'