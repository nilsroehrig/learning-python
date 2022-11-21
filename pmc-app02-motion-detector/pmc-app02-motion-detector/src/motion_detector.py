import cv2

video = cv2.VideoCapture(0)

first_frame = None

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

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(current_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # cv2.imshow("Capture", current_frame_gray)
    # cv2.imshow("Delta Frame", delta_frame)
    # cv2.imshow("Thresholded Delta Frame", thresh_frame)
    # cv2.imshow("Countours", contours)

    cv2.imshow("Color", current_frame)

    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
