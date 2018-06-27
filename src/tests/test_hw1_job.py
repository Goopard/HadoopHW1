"""
This is a unittest testcase for the job LargestWordsJob.
"""

import unittest
import sys

from io import BytesIO

from largest_words_job import LongestWordsJob


class JobTest(unittest.TestCase):
    def setUp(self):
        with open('test_inputs\\test_one_longest_word_from_some_text_input.txt', 'rb') as file:
            self.first_test_stdin = BytesIO(file.read())
        with open('test_inputs\\test_two_longest_words_from_some_text_input.txt', 'rb') as file:
            self.second_test_stdin = BytesIO(file.read())

    def test_one_longest_word_from_some_text(self):
        """
        This test checks if the job works correctly for some simple ont-line text with --number==1.
        """
        test_job = LongestWordsJob(['-o test_outputs\\test_one_longest_word_from_some_text'])
        test_job.sandbox(stdin=self.first_test_stdin)
        result = []
        with test_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = test_job.parse_output_line(line)
                result.append(value)
        self.assertEqual(result, ['familiarize\n', '\n'])

    def test_two_longest_words_from_some_text(self):
        """
        This functions checks if the job works correctly for some multiple lines of text with --number==2.
        """
        test_job = LongestWordsJob(['--number=2', '-o test_outputs\\test_two_longest_words_from_some_text'])
        test_job.sandbox(stdin=self.second_test_stdin)
        result = []
        with test_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = test_job.parse_output_line(line)
                result.append(value)
        try:
            self.assertEqual(result, ['second\n', 'fourth\n', '\n'])
        except AssertionError:
            self.assertEqual(result, ['fourth\n', 'second\n', '\n'])


if __name__ == '__main__':
    unittest.main()
