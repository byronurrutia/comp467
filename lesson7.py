# Lesson Question 1 Answer
# magneto or swagneto

# Project 1 and 2 dealt with frames, let's turn some
# Into timecode.
# Write a script that takes a frame and turns it into
# Working timecode at 24 fps.
# Use frame examples: 35, 1569, 14000

import math
exampleFrames = [35, 1569, 1400]
framerate = 24

for frame in exampleFrames:
    ss = math.floor(frame / framerate)
    mm = math.floor(ss / 60)
    hh = math.floor(mm / 60)
    ff = math.floor(frame % framerate)

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

    print("Timecode for " + str(frame) + " frames:")
    print(hh + ":" + mm + ":" + ss + ":" + ff)
