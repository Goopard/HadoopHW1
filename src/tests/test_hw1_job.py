"""
This is a unittest testcase for the job LargestWordsJob.
"""

import unittest

from io import BytesIO

from largest_words_job import LongestWordsJob


class JobTest(unittest.TestCase):
    def test_one_longest_word_from_some_text(self):
        """
        This test checks if the job works correctly for some simple ont-line text with --number==1.
        """
        with open('test_inputs\\test_one_longest_word_from_some_text_input.txt', 'rb') as file:
            stdin = BytesIO(file.read())
        test_job = LongestWordsJob()
        test_job.sandbox(stdin=stdin)
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
        with open('test_inputs\\test_two_longest_words_from_some_text_input.txt', 'rb') as file:
            stdin = BytesIO(file.read())
        test_job = LongestWordsJob(['--number=2'])
        test_job.sandbox(stdin=stdin)
        result = []
        with test_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = test_job.parse_output_line(line)
                result.append(value)
        self.assertEqual(result, ['second\n', 'forth\n', '\n'])
