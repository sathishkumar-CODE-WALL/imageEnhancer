import cv2

#Load the image in black and white (0 - b/w, 1 - color).
img = cv2.imread('demo_image.jpg', 0)

#Get the height and width of the image.
h, w = img.shape[:2]

#Invert the image to be white on black for compatibility with findContours function.
imgray = 255 - img
#Binarize the image and call it thresh.
ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

#Find all the contours in thresh. In your case the 3 and the additional strike
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#Calculate bounding rectangles for each contour.
rects = [cv2.boundingRect(cnt) for cnt in contours]

#Calculate the combined bounding rectangle points.
top_x = min([x for (x, y, w, h) in rects])
top_y = min([y for (x, y, w, h) in rects])
bottom_x = max([x+w for (x, y, w, h) in rects])
bottom_y = max([y+h for (x, y, w, h) in rects])

#Draw the rectangle on the image
out = cv2.rectangle(img, (top_x, top_y), (bottom_x, bottom_y), (0, 255, 0), 2)
#Save it as out.jpg
cv2.imwrite('out.jpg', img)