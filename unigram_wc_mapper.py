import re
import sys

def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print('%s%s%d' % ("UNIGRAM_WORD_COUNT", separator, 1))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
