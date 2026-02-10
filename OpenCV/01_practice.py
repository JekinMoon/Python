import cv2
import os

img_path = os.path.join(os.path.dirname(__file__), "images", "robot.jpg")
img = cv2.imread(img_path)  

cv2.imshow("Image Window", img)

key = cv2.waitKey(0)
print(f"Pressed key code: {key}")

cv2.destroyAllWindows()


img_default = cv2.imread(img_path, cv2.IMREAD_COLOR)

img_grayscale = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

cv2.imshow("Default Image", img_default)
cv2.imshow("Grayscale Image", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

