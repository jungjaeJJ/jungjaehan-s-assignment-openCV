import numpy as np
import cv2
# Read from the first camera device
cap = cv2.VideoCapture(0)

topLeft = (50, 50)
bold = 0

# Callback function for the trackbar
def on_bold_trackbar(value):
    #print("Trackbar value:", value)
    global bold
    bold = value

cv2.namedWindow("Camera")
cv2.createTrackbar("bold", "Camera", bold, 10, on_bold_trackbar)

# 성공적으로 video device 가 열렸으면 while 문 반복
while(cap.isOpened()):
    # 한 프레임을 읽어옴
    ret, frame = cap.read()
    if ret is False:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Text 
    cv2.putText(frame, "TEXT",
        topLeft, cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 25, 25), 4 + bold)

    
    # Make a Circle
    cv2.circle(frame, (200,100), 100, (245,243,31) , 1, cv2.LINE_AA)

    # Draw with the mouse

    radius = 3  # Define the radius outside of the mouse_event function

    def mouse_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # Check for left mouse button click
            cv2.circle(param, (x, y), radius, (255, 0, 0), 2)

    frame = np.full((500, 500, 3), 255, dtype=np.uint8)
    cv2.setMouseCallback("Camera", mouse_event, frame)


    #Display
    cv2.imshow("Camera",frame)

    # 1 ms 동안 대기하며 키 입력을 받고 'q' 입력 시 종료
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
