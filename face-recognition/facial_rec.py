import numpy as np
import cv2
import os
import sys


def facedetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_haar.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=3)
    return faces, gray_img


def labels_for_training_data(directory):
    faces = []
    faceid = []

    for path, subdirname, filename in os.walk(directory):
        for filename in filename:
            if filename.startswith("."):
                print("Skipping System File")
                continue
            id = os.path.basename(path)
            img_path = os.path.join(path, filename)
            print("img_path", img_path)
            print("id", id)
            test_img = cv2.imread(img_path)
            if test_img is None:
                print("not Loaded Properly")
                continue

            faces_rect, gray_img = facedetection(test_img)
            if len(faces_rect) != 1:
                continue

            (x, y, w, h) = faces_rect[0]
            roi_gray = gray_img[y:y + w, x:x + h]
            faces.append(roi_gray)
            faceid.append(int(id))
    return faces, faceid


# TRAINING CLASSIFIER
def train_classifier(faces, faceid):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceid))
    return face_recognizer


# drawing a rectangle on the face
def draw_rect(test_img, face):
    (x, y, w, h) = face
    cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)


# putting text on images
def put_text(test_img, label_name, x, y):
    cv2.putText(test_img, label_name, (x, y), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 3)
