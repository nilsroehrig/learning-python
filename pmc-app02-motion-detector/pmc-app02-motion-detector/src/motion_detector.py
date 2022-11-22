from datetime import datetime
import cv2
import pandas

video = cv2.VideoCapture(0)

first_frame = None
motion_detected = False
latest_motion_detection_start = None
timespans = []

while True:
    check, current_frame = video.read()
    current_frame_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    current_frame_gray = cv2.GaussianBlur(current_frame_gray, (21, 21), 0)

    if first_frame is None:
        first_frame = current_frame_gray
        continue

    delta_frame = cv2.subtract(first_frame, current_frame_gray)

    _, thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not motion_detected and len(contours) > 0:
        motion_detected = True
        latest_motion_detection_start = datetime.now()

    if motion_detected and len(contours) == 0:
        motion_detected = False
        timespans.append((latest_motion_detection_start, datetime.now()))

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Color", current_frame)

    if cv2.waitKey(1) == ord("q"):
        if motion_detected:
            timespans.append((latest_motion_detection_start, datetime.now()))
        break

timespan_dataframe = pandas.DataFrame()
timespan_dataframe["start"] = [start for start, _ in timespans]
timespan_dataframe["end"] = [end for _, end in timespans]

timespan_dataframe.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()
