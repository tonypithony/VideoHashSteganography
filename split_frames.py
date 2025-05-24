# conda activate DCTWM 
# conda activate iWM

# https://iq.opengenus.org/convert-video-to-images-in-python/

import cv2


name = 'kikicut_wm_25fps.mp4'

vidcap = cv2.VideoCapture(name)

success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite(f"{name[:-4]}/{count}.png", image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1
  # if count == 34346:
  #   break
