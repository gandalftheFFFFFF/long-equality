from unittest import TestCase
from improved import max_equal_gap_seq


class Test(TestCase):

    def test_straight(self):
        self.assertEquals(max_equal_gap_seq([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_zeros(self):
        self.assertEquals(max_equal_gap_seq([4, 3, 4, 5, 1, 4]), [4, 4, 4])

    def test_three_elements(self):
        self.assertEquals(max_equal_gap_seq([0, 2, 5]), [0, 2])

    def test_unique(self):
        self.assertEquals(max_equal_gap_seq([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_short_edge_case(self):
        self.assertEquals(max_equal_gap_seq([0, 1]), [0, 1])

    def test_short_edge_case_zeros(self):
        self.assertEquals(max_equal_gap_seq([0, 0]), [0, 0])

    def test_two_sequences(self):
        self.assertEquals(max_equal_gap_seq([1, 3, 5, 6, 8, 10, 12]), [6, 8, 10, 12])
