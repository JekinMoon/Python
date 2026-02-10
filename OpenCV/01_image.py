import cv2
import os

# 이미지 읽기
# img_path = os.path.join(os.path.dirname(__file__), "images", "5959.jpg")
# img = cv2.imread(img_path)

# 이미지 창에 표시
# cv2.imshow("Image Window", img)

# 키보드 입력 대기(0은 무한 대기)
# key = cv2.waitKey(0)
# print(f"Pressed key code: {key}")

# 모든 창 닫기 
# cv2.destroyAllWindows()


# 채널 3개 (R, G, B)
# img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 채널 없음(그레이스케일)
# img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# cv2.imshow("Default Image", img_default)
# cv2.imshow("Grayscale Image", img_grayscale)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_path = os.path.join(os.path.dirname(__file__), "images", "logo.png")

# 채널 3개 (R, G, B)
img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 채널 4 (Alpha 값 포함 - 배경 투명일 경우)
img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

cv2.imshow("Default Image", img_default)    
cv2.imshow("Unchanged Image", img_unchanged)
print("Logo Shape (Unchanged):", img_unchanged.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()


