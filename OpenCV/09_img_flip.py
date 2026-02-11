import cv2

image = cv2.imread("OpenCV/images/5959.jpg")

# 좌우 반전
img_flip = cv2.flip(image, 1) # 0보다 크다 : y축 반전

cv2.imshow('flip', img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

