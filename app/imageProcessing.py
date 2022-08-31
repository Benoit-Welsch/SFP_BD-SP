import numpy as np
from PIL import Image, ImageOps
from helper import roundToString
from keras import load_model
import cv2

model = None


def createTileView(frames, col):
    row = len(frames) // col
    resolution = frames[0].shape
    tiles = Image.new("RGB", (resolution[1]*col, resolution[0]*row))

    for x in range(col):
        for y in range(row):
            RBGFrame = frames[y*col + x][:, :, ::-1]
            frame_PIL = Image.fromarray(RBGFrame)
            tiles.paste(frame_PIL, (resolution[1]*x, resolution[0]*y))

    return tiles


def preLoadModel():
    global model
    model = load_model('./model/keras_model.h5')
    model.compile(loss='binary_crossentropy',
                  optimizer='rmsprop',
                  metrics=['accuracy'])

    # Preload model
    preloadImage = np.random.rand(224, 224, 3) * 255
    # resize image to match model's expected sizing
    preloadImage = cv2.resize(preloadImage, (224, 224))
    # return the image with shaping that TF wants.
    preloadImage = preloadImage.reshape(1, 224, 224, 3)
    preShape = np.zeros([224, 224, 3], dtype=np.uint8)
    model.predict(preloadImage)


def isShiny(frames):
    global model
    normalizedFrame = []

    for frame in frames:
        # resize image to match model's expected sizing
        image_PIL = Image.fromarray(frame)
        image = ImageOps.fit(image_PIL, (224, 224), Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        normalizedFrame.append(normalized_image_array)

    predictions = model.predict(np.array(normalizedFrame))

    for pred in predictions:
        print(roundToString(pred[0]), roundToString(
            pred[1]), roundToString(pred[2]))
        if (pred[1] > pred[0] and pred[1] > pred[2]):
            return True
    return False
