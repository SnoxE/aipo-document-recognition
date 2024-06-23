import cv2
from keras_facenet import FaceNet
import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt

def embedding_to_string(embedding):
    return '{' +  ','.join(str(x) for x in embedding) + '}'

def detect_faces(image_path: str):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not open or find the image.")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 9,  minSize=(100, 100))

    for (x,y,w,h) in faces:
      face_image = image[y:y+h, x:x+w]

    return face_image


def get_face_embedding(face_image):
    face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

    embedder = FaceNet() 
    return embedder.embeddings([face_image_rgb])[0]


def cosine_similarity(embedding1, embedding2):
    return np.dot(embedding1, embedding2) / (norm(embedding1) * norm(embedding2))


def is_match(embedding1, embedding2, threshold=0.7):
    return cosine_similarity(embedding1, embedding2) > threshold
