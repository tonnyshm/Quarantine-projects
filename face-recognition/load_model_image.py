import numpy as np
import cv2
import os

import facial_rec as fr

print(fr)

test_img = cv2.imread(r'C:\Users\HP\PycharmProjects\face-recognition\test1.jpg')      # Give path to the image which you want to test

faces_detected, gray_img = fr.facedetection(test_img)
print("face Detected: ", faces_detected)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(
    r'C:\Users\HP\PycharmProjects\face-recognition\TrainingData.yml')         # Give path of where trainingData.yml is saved

name = {0: "tonny",  1: "yonnyy"}        # Change names accordingly.  If you want to recognize only one person then write:- name={0:"name"} thats all. Dont write for id number 1.

for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y + h, x:x + h]
    label, confidence = face_recognizer.predict(roi_gray)
    print("Confidence :", confidence)
    print("label :", label)
    fr.draw_rect(test_img, face)
    predicted_name = name[label]
    fr.put_text(test_img, predicted_name, x, y)

resized_img = cv2.resize(test_img, (900, 900))

cv2.imshow("face detection ", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows
