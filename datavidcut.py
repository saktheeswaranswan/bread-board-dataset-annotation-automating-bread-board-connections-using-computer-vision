#https://iq.opengenus.org/convert-video-to-images-in-python/  #credits
import cv2
vidcap = cv2.VideoCapture('video_20230708_165136.mp4')
success, image = vidcap.read()
count = 1
while success:
  cv2.imwrite("/home/josva/Pictures/breadboarddataset/imagecut/image_%d.jpg" % count, image)    
  success, image = vidcap.read()
  print('Saved image ', count)
  count += 1
