import ChessCell
import unittest

class ChessCellTest(unittest.TestCase):
    def is_free_test(self):
        c1 = ChessCell()
        self.assertEqual(c1.is_free(), True)