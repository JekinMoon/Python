import cv2
import os

img_path = os.path.join(os.path.dirname(__file__), "images", "london.mp4")
cap = cv2.VideoCapture(img_path)
fps = cap.get(cv2.CAP_PROP_FPS)
print("fps:", fps)
if fps == 0:
    fps = 30
total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("FPS:", fps, "| Total frames:", total_frame)    

start_frame = 0
end_frame = total_frame - 1
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

speed = 1.0        
min_speed = 1.0
max_speed = 10.0
direction = 0.05

while True:
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        speed = 1.0
        direction = 0.05
        continue

    current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

    if current_frame > end_frame:
        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
        speed = 1.0
        direction = 0.05
        continue

    cv2.putText(frame, f"Frame: {current_frame} Speed: {speed:.2f}x", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("VideoFrame", frame)

    speed += direction

    if speed >= max_speed:
        speed = max_speed
        direction = -direction
    elif speed <= min_speed:
        speed = min_speed
        direction = -direction   
    
    if speed > 1:
        for _ in range(int(speed) - 1):
            cap.read()

    delay = max(int(1000 / (fps * speed)), 1)

    if cv2.waitKey(delay) >= 0:
        break

cap.release()
cv2.destroyAllWindows()