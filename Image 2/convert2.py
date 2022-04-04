import cv2
image= cv2.imread("2.jpeg")
grey_filter= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output1.png",grey_filter)
#invert= cv2.bitwise_not(grey_filter)

#cv2.imwrite("output11.png",invert)
#blur= cv2.GaussianBlur(invert, (25,25),0)
#cv2.imwrite("output111.png",blur)
#invertedblur= cv2.bitwise_not(blur)

#cv2.imwrite("output1111.png",invertedblur)
#sketch_filter=cv2.divide(grey_filter,invertedblur,scale=300.0)
#cv2.imwrite("output11111.png",sketch_filter)