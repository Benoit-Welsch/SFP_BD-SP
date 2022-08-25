import cv2
import numpy as np

from keras.models import load_model
from PIL import Image, ImageOps
import cv2

model = load_model('./model/keras_model.h5')
video = cv2.VideoCapture()
video.open("/dev/video1", cv2.CAP_DSHOW)


def saveFrame(frame, path):
    return cv2.imwrite(path, frame)


def captureFrame():
    success, frame = video.read()
    print(frame)
    if not success:
        raise Exception("Cannot read")
    return frame


def isShiny(frame, model):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    image_PIL = Image.fromarray(frame)
    image = ImageOps.fit(image_PIL, (224, 224), Image.ANTIALIAS)

    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    return prediction
