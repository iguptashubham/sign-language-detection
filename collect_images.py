import os
import time
import cv2
import uuid

data_dir = "./Data_images"
classes = 3
generate = 20

if not os.path.exists(data_dir):
    os.mkdir(data_dir)

cap = cv2.VideoCapture(0)
for i in range(1,classes+1):
    if not os.path.exists(os.path.join(data_dir, str(i))):
        os.makedirs(os.path.join(data_dir,str(i)), exist_ok=True)

    while True:
        ret, frame = cap.read()
        frame = cv2.putText(frame, "Press 'q' to Start-",
                            (50, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            2, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(25) & 0xff==ord('q'):
            break

    counter = 0
    while counter < generate:
        ret, frame = cap.read()
        frame = cv2.putText(frame,f'{counter}',
                            (50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            2,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow('Capturing Images',frame)
        cv2.imwrite(os.path.join(data_dir, str(i),f"{uuid.uuid1()}.jpg"),frame)
        cv2.waitKey(25)
        time.sleep(1)
        counter = counter +1

cap.release()
cv2.destroyAllWindows()