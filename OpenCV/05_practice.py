import cv2

# 1. 이미지 읽기(흑백으로 로드)
img = cv2.imread("OpenCV/images/mario.png", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(img, (400, 400))

# 2. 흑백 반전 (각 픽셀 값을 255에서 뺌)
inverted_image = 255 - image

# 3. 결과 출력
cv2.imshow("Original", image)
cv2.imshow("Inverted", inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

