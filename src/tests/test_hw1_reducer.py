"""
This is a unittest testcase for the function reducer of the job LargestWordsJob.
"""

import unittest
from largest_words_job import LongestWordsJob


class ReducerTests(unittest.TestCase):
    def test_one_longest_word_from_one_word(self):
        """
        This test checks if reducer works correctly for the input data of a single word with --number==1.
        """
        test_job = LongestWordsJob()
        values = [['word']]
        self.assertEqual(next(test_job.reducer(None, values)), (None, 'word\n'))

    def test_one_longest_word_from_many_words(self):
        """
        This test checks if reducer works correctly for the input data of multiple words with --number==1.
        """
        test_job = LongestWordsJob()
        values = (['word'], ['abacaba'], ['abacabadabacaba'])
        self.assertEqual(next(test_job.reducer(None, values)), (None, 'abacabadabacaba\n'))

    def test_two_longest_words_from_many_words(self):
        """
        This tests checks if reducer works correctly for the input data of multiple words with --number==2.
        """
        test_job = LongestWordsJob(['--number=2'])
        values = (['word'], ['abacaba', 'adacadabadacada'], ['abacabadabacaba'])
        self.assertEqual(next(test_job.reducer(None, values)), (None, 'abacabadabacaba\nadacadabadacada\n'))


if __name__ == '__main__':
    unittest.main()
