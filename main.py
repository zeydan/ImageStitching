import cv2
import glob

imagefiles = glob.glob('store1/*')
imagefiles.sort()

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    images.append(img)

stitcher = cv2.Stitcher_create()
_, result = stitcher.stitch(images)

cv2.imshow('Result', result)
cv2.imwrite('Store1.jpg', result)
cv2.waitKey(0)