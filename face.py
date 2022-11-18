import cv2 
import mediapipe as mp

cap = cv2.VideoCapture(0)



# Adjust Resolution
def make_1080p(): 
    cap.set(3, 1920) 
    cap.set(4, 1080) 

def make_720p():
    cap.set(3, 1280) 
    cap.set(4, 720) 
def make_480p(): 
    cap.set(3, 640) 
    cap.set(4, 480) 
def change_res(width, height): 
    cap.set(3, width) 
    cap.set(4, height) 
    make_720p() 
    change_res(1280, 720) 

make_720p()


def rescale_frame(frame, percent=75): 
    width = int(frame.shape[1] * percent/ 100) 
    height = int(frame.shape[0] * percent/ 100) 
    dim = (width, height) 
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA) 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:

    _, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    results = hands.process(imgRGB)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)


    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

    cv2.imshow("muqemmel_fizik_projem", img)
    cv2.waitKey(1)