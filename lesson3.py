# Create a folder on your computer called "week3"

# Create a script that, when run,checks every second indefinitely for a new file in that folder

# If file found,report back to the user:
#   1.File found
#   2. What type of file it is
#   3.When it was put there


# You as the user can introduce whatever file you want to invoke the notification portion of the script ( i.e put a text file, image, etc)


# Copy/paste code and console output
import time
import os
import datetime

path = "/home/byronurrutia/projects/comp467/"
startDir = os.listdir(path)

starttime = time.time()
while True:
    print("...")
    currDir = os.listdir(path)
    now = datetime.datetime.now()
    # https://www.geeksforgeeks.org/python-list-files-in-a-directory/
    newList = [i for i in currDir if i not in startDir]
    if len(newList) > 0:
        count = 0
        for item in newList:
            listSize = len(newList)
            # https://www.geeksforgeeks.org/how-to-get-file-extension-in-python/
            split_tup = os.path.splitext(newList[count])
            print(newList[count]
                +" created at "
                +str(datetime.datetime.now())
                +" as "+str(split_tup[1]))
            count = count + 1
    startDir = os.listdir(path)
    # https://stackoverflow.com/questions/474528/how-to-repeatedly-execute-a-function-every-x-seconds
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))