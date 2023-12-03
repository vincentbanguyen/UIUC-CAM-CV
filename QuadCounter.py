import cv2

video = cv2.VideoCapture("QuadCam.mp4") # object that reads the frames of our video


# background subtractor
object_detector = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=10)

while True: # anlayze frame by frame
    ret, frame = video.read()
    mask = object_detector.apply(frame)

    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 30:
            cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)

    if key == 27: # pressing esc will exit video capture
        break

video.release()