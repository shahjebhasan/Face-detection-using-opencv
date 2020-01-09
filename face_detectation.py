import cv2,time
import matplotlib.pyplot as plt
face_cascade=cv2.CascadeClassifier('C:/Users/DELL/Desktop/webskitters/Haarcascades/haarcascade_frontalface_default.xml')
def detect_face(img):
    face_img=img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,1.3,5)
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,0,255),2)      
    return face_img
video=cv2.VideoCapture(0)
a=1
while True:
    a+=1
    check,frame=video.read()
    frame=detect_face(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('Capture',gray)
    key=cv2.waitKey(30) & 0xff
    if key==ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()