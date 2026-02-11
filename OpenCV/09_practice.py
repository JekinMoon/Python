import cv2

image = cv2.imread("OpenCV/images/5959.jpg")

if image is None:
    print("이미지를 불러올 수 없습니다.")
else:
    h,w,_ = image.shape

    # 1. 1/2 축소
    small_img = cv2.resize(image, (w//2, h//2))

    # 2. 좌우 반전
    flip_img = cv2.flip(small_img, 1)

    # 3. 우하단 배치
    result = image.copy()
    sh, sw, _ = flip_img.shape

    # 시작점부터 이미지 높이만큼만 영역 지정
    result[h//2 : h//2 + sh, w//2 : w//2 + sw] = flip_img

    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    