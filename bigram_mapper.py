import re
import sys

def read_input(input):
    for line in input:
        # split the line into words; keep returning each word
        tmp = re.sub(r'[^0-9a-zA-Z]+', ' ', line.lower())
        if len(tmp.split())>=3:
            yield tmp.split()
        else:
            pass


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        n = len(words)
        for i in range(n-1):
            tmp = words[i] + ' ' + words[i+1]
            print('%s%s%d' % (tmp, separator, 1))


# how to test locally in bash/linus: cat <input> | python mapper.py
if __name__ == "__main__":
    main()
