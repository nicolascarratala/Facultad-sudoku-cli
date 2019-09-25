import unittest
from test import support
from Sudoku import Sudoku


class TestSudoku(unittest.TestCase):


    def test_game_not_over(self):
        over = Sudoku().is_over()
        self.assertFalse(over)

    def test_num_in_col(self):
        x = 0
        y = 0
        n = 0
        colCorrect = Sudoku().correct_in_col(x,y,n)
        self.assertTrue(colCorrect)

    def test_num_in_row(self):
        x = 0
        y = 0
        n = 0
        rowCorrect = Sudoku().correct_in_row(x,y,n)
        self.assertTrue(rowCorrect)    

    def test_num_in_region(self):
        x = 0
        y = 0
        n = 0
        region = Sudoku().correct_in_region(x,y,n)
        self.assertTrue(region)    

    def test_num_in_position(self):
        x = 0
        y = 0
        n = 0
        position= Sudoku().position_num(x,y,n)
        self.assertTrue(position)

    


if __name__ == '__main__':
    unittest.main()