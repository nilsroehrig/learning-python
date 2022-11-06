import time

import cv2

video = cv2.VideoCapture(0)

frames = 1

start = time.time()

while True:
    frames = frames + 1
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

end = time.time()
video.release()
cv2.destroyAllWindows()

print("FPS: ", frames / (end - start))



