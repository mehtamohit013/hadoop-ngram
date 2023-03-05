import sys
import argparse

def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split()

def main(uni,bi,separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    uni_dict = {}

    for words in data:
        if words[1]=='1':
            uni_dict[words[0]] = int(words[2])
        else:
            tmp = (float(words[3])/bi)/(float(uni_dict[words[0]])/uni)
            print("%s%s%s%s%s%f"%("Bigram Prob of ",words[0]," ", words[2],'\t',tmp))

        
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--uni', type=str, required=True)
    parser.add_argument('--bi', type=str, required=True)
    args = parser.parse_args()
    main(int((args.uni).strip()),int((args.bi).strip()))