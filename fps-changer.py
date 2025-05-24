# conda activate iWM

# https://stackoverflow.com/questions/44179498/change-videos-frame-rate-fps-in-python

# pip install moviepy

from moviepy.editor import *

clip = VideoFileClip("2.mp4")
clip.write_videofile("new-fps.mp4", fps=600)
#clip.reader.close()