#Import the necessary packages
#Install cv2 with the help of command "pip install opencv-python"
import cv2,time
import matplotlib.pyplot as plt

#OpenCV comes with these pre-trained cascade files, we can download it visiting this "link http://alereimondo.no-ip.org/OpenCV/34/"
#after downloading provide the specific path on which the haarcascade_file is residing.
face_cascade=cv2.CascadeClassifier('C:/Users/DELL/Desktop/webskitters/Haarcascades/haarcascade_frontalface_default.xml')

def detect_face(img):
    # Our classifier returns the ROI of the detected face as a tuple
    face_img=img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,1.3,5)
    # It stores the top left coordinate and the bottom right coordiantes
    # face_rects returns x,y and w,h
    for (x,y,w,h) in face_rects:
        #provide the coordinates to map the rectangle around your face
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,0,255),2)      
    return face_img

#Method to create VideoCapture object. It will Trigger the camera.
#(0) specifies use built - in camera.
video=cv2.VideoCapture(0)

a=1
while True:
    a+=1
    check,frame=video.read()
    #frame:Numpy array,it represents the first image that video captures
    #check:Bool type,returns true if python is able to read the VideoCapture object
    frame=detect_face(frame)
    #converts the image into GrayScale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #imshow method is used to capture the first image/frame of the video
    cv2.imshow('Capture',gray)
    key=cv2.waitKey(30) & 0xff
    
    #window will get destroyed when we press q
    if key==ord('q'):
        break
        
print(a)

video.release()
cv2.destroyAllWindows()
