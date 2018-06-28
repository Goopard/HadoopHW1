"""
This is a unittest testcase for the function mapper of the job LargestWordsJob.
"""

import unittest
from largest_words_job import LongestWordsJob


class MapperTests(unittest.TestCase):
    def test_one_longest_word_in_one_word_line_line(self):
        """
        This test checks if mapper works correctly for the line with a single word with --number==1.
        """
        test_job = LongestWordsJob()
        self.assertEqual(next(test_job.mapper(None, 'word')), (None, ['word']))

    def test_one_longest_word_in_long_line(self):
        """
        This test checks if mapper works correctly for the line with many words with --number==1.
        """
        test_job = LongestWordsJob()
        self.assertEqual(next(test_job.mapper(None, 'This is a quiet long string with many words')), (None, ['string']))

    def test_two_longest_words_in_long_line(self):
        """
        This test checks if mapper words correctly for the line with many words with --number==2.
        """
        test_job = LongestWordsJob(['--number=2'])
        self.assertEqual(next(test_job.mapper(None, 'This is a quiet long string with many words')),
                         (None, ['string', 'quiet']))


if __name__ == '__main__':
    unittest.main()
