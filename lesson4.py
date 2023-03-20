# -
# Attached to the assignment is a test file: lesson4_folderexample.txt Download lesson4_folderexample.txt 
# -
# External clients have added spaces throughout the folder names by: internal
# workflow conflict, user mistake, etc
# -
# We determined the only issue is that there are spaces, but need to confirm which
# folders
# -
# Write a script that removed all spaces, reports the fixed string, and reports on console which ones needed fixing and which were fine.
file = open("lesson4_folderexample.txt", "r")
fileLines = file.readlines()
fixedLines = []

for fileLine in fileLines:
    if " " in fileLine:
        print("Spaces found in " + fileLine)
        newFileLine = fileLine.replace(" ", "")
        fixedLines.append(newFileLine)

print("Fixed files directories:")
for i in fixedLines:
    print(i)