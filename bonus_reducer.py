#!/usr/bin/env python
"""An advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator)


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    # groupby groups multiple word-count pairs by word
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    curr_count = 0
    curr_word = ''

    for current_word, group in groupby(data, itemgetter(0)):
        # print(group)
        try:
            total_count = sum(int(count) for current_word, count in group)
            # print(total_count)
            if total_count>curr_count:
                curr_count=total_count
                curr_word = current_word
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    print("%s%s%d" % (curr_word, separator, curr_count))


if __name__ == "__main__":
    main()
