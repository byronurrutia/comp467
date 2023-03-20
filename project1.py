import csv

baselight = open("Baselight_export.txt", "r")
xytech = open("Xytech.txt", "r")

xytechLines = xytech.readlines()
baselightLines = baselight.readlines()
workOrder = ""
producer = ""
operator = ""
job = ""
notes = ""
count = 0
fileLocations = []
locations = []
frames = []
frameLocations = []
isNotes = False

for xytechLine in xytechLines:
    if "Xytech Workorder 1107" in xytechLine:
        workOrder = xytechLine.replace("\n", "")
    elif "Producer" in xytechLine:
        producer = xytechLine.replace("Producer: ", "", 1)
        producer = producer.replace("\n", "")
        #print(producer)
    elif "Operator" in xytechLine:
        operator = xytechLine.replace("Operator: ", "", 1)
        operator = operator.replace("\n", "")
        #print(operator)
    elif "Job" in xytechLine:
        job = xytechLine.replace("Job: ", "", 1)
        job = job.replace("\n", "")
        #print(job)
    elif "/production/starwars/" in xytechLine:
        locations.append(xytechLine.strip())
        fileLocation = xytechLine
        fileLocation = fileLocation.replace(fileLocation[:30], "")
        fileLocations.append(fileLocation.strip())
    elif isNotes:
        notes = xytechLine
    elif "Notes" in xytechLine:
        isNotes = True

for baselightLine in baselightLines:
    strippedLine = baselightLine.replace("/images1/starwars/", "", 1)
    strippedLine = strippedLine.replace(" <err>", "", 1)
    strippedLine = strippedLine.replace(" <null>", "", 1)
    isFound = False
    index = 0
    for fileLocation in fileLocations:
        if fileLocation in strippedLine:
            strippedLine = strippedLine.replace(fileLocation, "", 1)
            frameLocations.append(locations[index])
            index = 0
            isFound = True
        elif isFound == False: 
            index = index + 1
    strippedLine = strippedLine.split()
    start = 0
    current = 0
    currentFrame = []
    for number in strippedLine:
        intNumber = int(number)
        if start == 0:
            start = intNumber
            current = intNumber
        elif intNumber == current + 1:
            current = intNumber
        elif intNumber > current + 1:
            if start == current:
                currentFrame.append(str(start))
            elif current > start:
                currentFrame.append(str(start) + "-" + str(current))
            start = intNumber
            current = intNumber
    if start == current:
                currentFrame.append(str(start))
    elif current > start:
        currentFrame.append(str(start) + "-" + str(current))
    frames.append(currentFrame)

frames.pop()

with open('frame_corrections.csv', mode="w") as csvfile:
    line1 = [workOrder, producer, operator, job, notes]
    print(workOrder + "/" + producer + "/" + operator + "/" + job + "/" + notes + "\n")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(line1)
    csvwriter.writerow([])
    for frameLocation in frameLocations:
        matchFrame = frames[count]
        for i in matchFrame:
            line2 = [frameLocation, i]
            print(frameLocation+ " / " + i)
            csvwriter.writerow(line2)
        count = count + 1