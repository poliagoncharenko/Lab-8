import cv2
image = cv2.imread('variant-10.jpg', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(image, 150,255,cv2.THRESH_BINARY)

cv2.imshow('image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()