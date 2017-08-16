import cv2
print(cv2.__version__)
filename = raw_input('filename = ')
vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  print 'Read a new frame: ', success
  cv2.imwrite("filename%d.tif" % count, image)     # save frame as tif file
  count += 1