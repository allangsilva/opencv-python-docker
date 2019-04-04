import cv2
import sys

cascPath = "/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Captura Frame por Frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
    #flags = cv.CV_HAAR_SCALE_IMAGE)
    
    # Desenhando ao redor das faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    #Exibe o numero de ocorrencias na tela 
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(len(faces)),(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

    # Exibe o resultado (quadro na face)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver pronto libere a captura
video_capture.release()
cv2.destroyAllWindows()