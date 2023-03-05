import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    ans = 0

    for words in data:
        ans+=1
    
    print("%d"%(ans))

if __name__=='__main__':
    main()