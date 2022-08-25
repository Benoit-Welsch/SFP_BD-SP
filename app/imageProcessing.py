from datetime import datetime
from imutils.video import VideoStream
from time import sleep
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
from helper import debug
import cv2


model = load_model('./model/keras_model.h5')
vs = VideoStream(src=0).start()
sleep(2.0)


def isShiny():
    debug('RIGHT - Start detection')
    i = 0
    while (i <= 30):
        frame = vs.read()
        date_time = datetime.now().strftime("%m-%d-%Y_%H-%M-%S")
        prediction = detect(frame)
        cv2.imwrite("./.temp/frame-" + date_time +
                    "_" + str(i) + ".png", frame)
        if (prediction[0][1] > prediction[0][0]):
            return True
        i += 1
    return False


def detect(frame):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # resize the image to a 224x224 with the same strategy as in TM2:
    # resizing the image to be at least 224x224 and then cropping from the center
    image_PIL = Image.fromarray(frame)
    image = ImageOps.fit(image_PIL, (224, 224), Image.Resampling.LANCZOS)

    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    return prediction
