import cv2

pattern = cv2.imread('ref-point.jpg', cv2.IMREAD_GRAYSCALE)

cap = cv2.VideoCapture(0)

flip = False
center_rect_size = 150

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_frame, pattern, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    w, h = pattern.shape[::-1]
    if max_val > 0.60:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        frame_height, frame_width = frame.shape[:2]
        center_x = frame_width // 2
        center_y = frame_height // 2
        center_rect = (
            center_x - center_rect_size // 2,
            center_y - center_rect_size // 2,)

        cv2.rectangle(frame, (center_rect[0], center_rect[1]), (center_rect[0] + center_rect_size, center_rect[1] + center_rect_size), (0, 255, 255), 2)

        label_center_x = top_left[0] + w // 2
        label_center_y = top_left[1] + h // 2

        if (
            center_rect[0] <= label_center_x <= center_rect[0] + center_rect_size
            and center_rect[1] <= label_center_y <= center_rect[1] + center_rect_size):
            frame = cv2.flip(frame, -1)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()