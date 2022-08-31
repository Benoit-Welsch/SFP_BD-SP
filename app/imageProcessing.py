import numpy as np
from PIL import Image, ImageOps
from keras.models import load_model

model = None


def createTileView(frames, col):
    row = len(frames) // col
    resolution = frames[0].shape
    tiles = Image.new("RGB", (resolution[1]*col, resolution[0]*row))

    for x in range(col):
        for y in range(row):
            currentFrame = frames[y*col + x]
            # Transform BGR in to RGB
            RBGFrame = currentFrame[:, :, ::-1]
            # Format transformation
            frame_PIL = Image.fromarray(RBGFrame)
            # Add frame to image
            tiles.paste(frame_PIL, (resolution[1]*x, resolution[0]*y))

    return tiles


def loadModel():
    global model
    model = load_model('./model/keras_model.h5', compile=False)

    # Preload model on empty image
    preShape = np.zeros([1, 224, 224, 3], dtype=np.uint8)
    model.predict(preShape)
    return model


def isShiny(frames):
    global model
    if (model == None):
        loadModel()

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
        if (pred[1] > pred[0] and pred[1] > pred[2]):
            return True
    return False, predictions
