import numpy as np
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield line[0:5], len(line.split())

    def reducer(self, key, values):
        yield key, np.average(list(values))
        yield key, sum(values)

if __name__ == '__main__':
    MRWordFrequencyCount.run()