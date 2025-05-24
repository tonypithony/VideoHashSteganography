import os
# from glob import glob


# filenames = glob("videoempty/*.mp4") 

# i = 1
# for filename in filenames:
#         try:
#             os.rename(filename, str(i) + ".mp4")
#             i += 1 
#         except FileExistsError:
#             pass


# for video in filenames:
# 	os.system(f"ffmpeg -i {video} videoempty/{video[11:-4]}.avi")
# 	os.remove(video)


video = 'kikicut.avi'

os.system(f"ffmpeg -i {video} {video[:-4]}.mp4")