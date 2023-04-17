# Create an Argparse script...​

# ​

# Add arguments for importing any text file and a "verbose" option that prints each line if that option is flagged. Print the total lines from that file at the end of script​

 

# Submit the code and output from running the script with "verbose" and one without "verbose"
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