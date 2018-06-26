"""
This is the module that contains the job that finds the N longest words in some given input text file.
"""

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
from functools import reduce
from operator import add


class LongestWordsJob(MRJob):
    """
    This is the job that finds the N longest words in the given text file.
    """

    OUTPUT_PROTOCOL = RawValueProtocol

    def configure_options(self):
        """
        This method configures the options of the job: it adds argument "--number", which is responsible for the number
        of the longest words that will be returned by the job.
        """
        super(MRJob, self).configure_options()
        self.add_passthrough_option('--number', type='int', default=1)

    def mapper(self, _, line):
        """
        This is the mapper function of the job, which will be applied to each line of the input text file. This function
        finds the --number longest words in the line and yields them as a list.
        """
        number = self.options.number
        if line:
            words = sorted(line.split(), key=len, reverse=True)
            max_word = words[:number]
            yield None, max_word

    def reducer(self, key, values):
        """
        This is a reducer function of the job, which will be applied to all the lists of words returned by all of the
        mappers and will return the --number longest of them as a single text (one word per line).
        """
        values = reduce(add, values, [])
        number = self.options.number
        words = sorted(values, key=len, reverse=True)
        max_word = words[:number]
        yield None, '\n'.join(max_word) + '\n'


if __name__ == '__main__':
    LongestWordsJob.run()
