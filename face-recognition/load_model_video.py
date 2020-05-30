import numpy as np
import cv2
import os

import facial_rec as fr
print(fr)



face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read(r'C:\Users\HP\PycharmProjects\face-recognition\TrainingData.yml')    #Give path of where trainingData.yml is saved

cap=cv2.VideoCapture(0)   #If you want to recognise face from a video then replace 0 with video path
name = {0:"tonny",1:"unknown"}

while True:
    ret, test_img = cap.read()
    faces_detected, gray_img = fr.facedetection(test_img)
    print("face Detected: ", faces_detected)
    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)

    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + h, x:x + h]
        label, confidence = face_recognizer.predict(roi_gray)
        print("Confidence :", confidence)
        print("label :", label)
        fr.draw_rect(test_img, face)
        predicted_name = name[label]
        if confidence > 90:
            continue
        fr.put_text(test_img, predicted_name, x, y)
        if label == 0:
            print("tonny")

    resized_img = cv2.resize(test_img, (1000, 700))

    cv2.imshow("face detection ", resized_img)
    if cv2.waitKey(10) == ord('q'):
        break



