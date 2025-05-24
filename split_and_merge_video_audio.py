# conda activate iWM

# https://copyassignment.com/extract-audio-from-video-using-python/
# https://mlhive.com/2023/04/merge-audio-and-video-files-using-python

# pip install moviepy

# import moviepy.editor

# video = moviepy.editor.VideoFileClip("Dance.mp4")
# audio = video.audio # extract the audio
# audio.write_audiofile("audiodance.mp3")



from moviepy.editor import *

# Define the paths of the audio and video files
audio_path = "Guano.mp3"
video_path = "Dance.mp4"

# Create instances of VideoFileClip and AudioFileClip
video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# Merge the audio and video clips
video_clip_with_audio = video_clip.set_audio(audio_clip)

# Write the merged video file to a new file
video_clip_with_audio.write_videofile("Dance_with_Guano.mp4")