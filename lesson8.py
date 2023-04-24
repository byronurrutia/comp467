# 1.Lesson Question Answer


# 2. Call a commandline tool, using subprocess and shlex . Write a script that calls the "ls"
# command with " l" argument on a folder. Print the file and file size of the largest file.
# command = 'ls -l /some/folder/with/stuff'
# process =
# subprocess.Popen
# shlex.split (
# stdout = subprocess.PIPE
# stderr = subprocess.STDOUT # Redirect STDERR to STDOUT, conjoining the two streams
# for line in iter process.stdout.readline ,

import subprocess
import shlex
import os

command = "ls -l /home/byronurrutia/projects/comp467/"
largest_file_size = 0
largest_file_name = ""
process = subprocess.Popen(
    shlex.split(command),
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    shell=True
)

for line in iter(process.stdout.readline, b""):
    parse_line = line.decode().strip()
    current_file_size = os.path.getsize(
        "/home/byronurrutia/projects/comp467/" + parse_line)
    print("file: %s; size: %s" % (parse_line, current_file_size))
    if current_file_size >= largest_file_size:
        largest_file_size = current_file_size
        largest_file_name = parse_line

print("largest file was %s with a size of %s bytes" %
      (largest_file_name, largest_file_size))
