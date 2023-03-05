import sys
import argparse

def read_input(input):
    for line in input:
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
        if len(words)!=0:
            if len(words)==2:
                print('%s%s%d%s%s' % (words[0], separator,  1, separator, words[1]))
            else:
                print('%s%s%d%s%s' % (words[0], separator, 2, separator, words[1]+' '+words[2]))
        else:
            pass


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
