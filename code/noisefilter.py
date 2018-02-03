import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test_images/doc2.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
cv2.imwrite('doc2_noisefree.jpg',dst)
plt.show()
