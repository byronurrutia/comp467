# Solve:
# 1.Download my amazing VP
# video, https://mycsun.box.com/s/v55rwqlu5ufuc8l510r8nni0dzq5qki7
# 2. Run script with new
# argparse command process <video file>
# 3. From (2) Call the populated database from proj2, find all ranges only that fall in
# the length of video from (1)
# 4. Using ffmpeg or 3rd party tool of your choice, to extract timecode from video and
# write your own timecode method to convert marks to timecode
# 5. New argparse output parameter for XLS with flag from (2) should export same
# CSV export, but in XLS with new column from files found from (3) and export their
# timecode ranges as well
# 6. Create Thumbnail (96x74) from each entry in (2), but middle most frame or closest
# to. Add to XLS file to it's corresponding range in new column


# Optional (Extra Credit)
# 1. Render out each shot and upload them using API to frame.io or Shotgrid

# Deliverables
# 1. Copy/Paste code
# 2. Excel file with new columns noted on Solve (5) and (6)

import argparse
import pymongo
import csv
import subprocess
import shlex
import math
import xlsxwriter

parser = argparse.ArgumentParser(
    description="import and count text file lines")
parser.add_argument("-p", "--process", type=str,
                    help="name of the video file to process", nargs="+")
parser.add_argument("-e", "--export", action="store_true",
                    help="export data to xls and csv")
args = parser.parse_args()

myclient = pymongo.MongoClient(
    "mongodb+srv://testuser:<Password>@seniorproject-west.ralsx.mongodb.net/test")
mydb = myclient["mydatabase"]
col2 = mydb["mycollection2"]

subprocess.run(shlex.split("ffmpeg -i " + args.process))
subprocess.run(shlex.split(
    "ffmpeg -i" + args.process + "-filter:v 'crop=96: 74: 920: 503' cropped_output.mp4"))


class TimeCodeUnits:
    def __init__(self, hh, mm, ss, ff):
        self.hours = hh
        self.minutes = mm
        self.seconds = ss
        self.frame = ff


def framesToTimecode(frame):
    ss = math.floor(frame / 60)
    mm = math.floor(ss / 60)
    hh = math.floor(mm / 60)
    ff = math.floor(frame % 60)

    if (len(str(hh)) == 1):
        hh = "0" + str(hh)
    else:
        hh = str(hh)

    if (len(str(mm)) == 1):
        mm = "0" + str(mm)
    else:
        mm = str(mm)

    if (len(str(ss)) == 1):
        ss = "0" + str(ss)
    else:
        ss = str(ss)

    if (len(str(ff)) == 1):
        ff = "0" + str(ff)
    else:
        ff = str(ff)
    return TimeCodeUnits(hh, mm, ss, ff)


def isGreaterTimecode(frameTimecode, videoTimecode):
    if int(frameTimecode.hours) > int(videoTimecode.hours):
        return True
    else:
        if int(frameTimecode.minutes) > int(videoTimecode.minutes):
            return True
        else:
            if int(frameTimecode.seconds) > int(videoTimecode.seconds):
                return True
            else:
                return False


def middleRangeTimecode(firstFrame, secondFrame):
    middleFrame = math.floor((secondFrame - firstFrame) / 2)
    return framesToTimecode(firstFrame + middleFrame)


def printTimecode(timecode):
    print(timecode.hours + ":" + timecode.minutes + ":" +
          timecode.seconds + ":" + timecode.frame)


videoTimecode = TimeCodeUnits("00", "01", "40", "38")
locations = []
frames = []
timecodes = []
middleTimecode = []

for x in col2.find():
    string = x["frame_ranges"]
    firstRange = ""
    secondRange = ""
    isSecondRange = False
    if "-" in string:
        for char in string:
            if char != "-" and isSecondRange == False:
                firstRange = firstRange + char
            if char == "-":
                isSecondRange = True
                continue
            if char != "-" and isSecondRange == True:
                secondRange = secondRange + char
    else:
        firstRange = string

    if (isGreaterTimecode(framesToTimecode(int(firstRange)), videoTimecode) == True):
        continue
    else:
        locations.append(x["location"])
        frames.append(x["frame_ranges"])
        firstTimecode = framesToTimecode(int(firstRange))
        if secondRange != "":
            secondTimecode = framesToTimecode(int(secondRange))
            timecodes.append(firstTimecode.hours + ":" + firstTimecode.minutes + ":" +
                             firstTimecode.seconds + ":" + firstTimecode.frame + " / " + secondTimecode.hours + ":" + secondTimecode.minutes + ":" + secondTimecode.seconds + ":" + secondTimecode.frame)
            middleTimecode.append(middleRangeTimecode(
                int(firstRange), int(secondRange)))
        elif secondRange == "":
            middleTimecode.append(firstTimecode)
            timecodes.append(firstTimecode.hours + ":" + firstTimecode.minutes + ":" +
                             firstTimecode.seconds + ":" + firstTimecode.frame)

if args.output:
    workbook = xlsxwriter.Workbook('project3/project3.xlsx')
    worksheet = workbook.add_worksheet()
    index = 2
    worksheet.write("A1", "Locations")
    worksheet.write("B1", "Frames")
    worksheet.write("C1", "Timecodes")
    worksheet.write("D1", "Thumbnail")
    for location in locations:
        worksheet.write("A"+str(index), location)
        worksheet.write("B"+str(index), frames[index - 2])
        worksheet.write("C"+str(index), timecodes[index - 2])
        subprocess.run(shlex.split("ffmpeg -i cropped_output.mp4 -ss " +
                                   middleTimecode[index - 2].hours + ":" + middleTimecode[index - 2].minutes + ":" + middleTimecode[index - 2].seconds + " -frames:v 1 output" + str(index - 1) + ".jpg"))
        worksheet.insert_image(
            "D"+str(index), "output" + str(index - 1) + ".jpg")
        index = index + 1
    workbook.close()

    fields = ["location", "frames", "timecode"]

    rows = []
    index = 0
    for location in locations:
        rows.append([location, frames[index], timecodes[index]])

    with open("project3.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
