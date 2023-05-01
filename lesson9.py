# Write a python script that when you import a video file, it will do two commands
# from: https://ostechnix.com/20 ffmpeg commands beginners/beginners/ Links to an external site.(you can use any
# other commands as well, as long as both use ffmpeg

# Copy/paste code and a single frame example (could be screenshot) of output
import subprocess
import shlex

subprocess.run(shlex.split("ffmpeg -i video.mp4"))
subprocess.run(shlex.split("ffmpeg -i video.mp4 -vn audio.mp3"))