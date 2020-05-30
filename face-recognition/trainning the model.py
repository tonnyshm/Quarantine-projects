import numpy as np
import os
import sys
import cv2
import facial_rec as fr

test_img = cv2.imread(r'C:\Users\HP\PycharmProjects\face-recognition\test1.jpg')

face_detected, gray_img = fr.facedetection(test_img)
# cv2.imshow(face_detected)
print("Face Detected:", face_detected)

# training model

faces, faceid = fr.labels_for_training_data(r'C:\Users\HP\PycharmProjects\face-recognition\images')
face_recognizer = fr.train_classifier(faces, faceid)
face_recognizer.save(r'C:\Users\HP\PycharmProjects\face-recognition\TrainingData.yml')

name = {0: 'tonny', 1: 'yonn'}

for face in face_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y + h, x:x + h]
    label, confidence = face_recognizer.predict(roi_gray)
    print("Confidence :", confidence)
    print("Label :", label)
    fr.draw_rect(test_img, face)
    predicted_name = name[label]
    fr.put_text(test_img, predicted_name, x, y)

resized_img = cv2.resize(test_img, (1000, 700))

cv2.imshow("Face Detection", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
