import cv2

cap = cv2.VideoCapture('video.webm') 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Deo doc duoc frame")
        break

    pixel_color = frame[262, 276]
    if all(pixel_color == [255, 255, 255]):
        print(1, end="")  
    else:
        print(0, end="")  

cap.release()
