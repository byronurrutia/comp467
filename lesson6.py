import argparse

parser = argparse.ArgumentParser(description="import and count text file lines")
parser.add_argument("-r", "--read", type=str, help="name of the file")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true", help="print text lines")

args = parser.parse_args()
def importFile(fileName):
    file = open(fileName, "r")
    fileLines = file.readlines()
    print("File read!")
    return fileLines

if __name__ == '__main__':
    fileLines = importFile(args.read)
    if args.verbose:
        for line in fileLines:
            print(line)