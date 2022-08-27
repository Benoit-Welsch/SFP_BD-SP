from datetime import datetime
from imutils.video import VideoStream
from time import sleep
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
from helper import debug, roundToString
import cv2

# Wait for cam
vs = VideoStream(src=0).start()
sleep(2.0)
# Load model

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
model.predict(preloadImage)


def isShiny():
    debug('KERAS - Start detection')
    frames = []
    numberOfFrame = 60
    date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Take 30 screenshot with 0.3s on sleep (30fps = 1 frame every 33ms -> 0.033s)
    for _ in range(numberOfFrame):
        frame = vs.read()
        frames.append(frame)
        sleep(0.03)

    # Create a combine view of all images -> Tiles
    col = 6
    row = int(numberOfFrame/col)
    resolution = frames[0].shape
    tiles = Image.new("RGB", (resolution[1]*col, resolution[0]*row))

    for x in range(col):
        for y in range(row):
            RBGFrame = frames[y*col + x][:, :, ::-1]
            frame_PIL = Image.fromarray(RBGFrame)
            tiles.paste(frame_PIL, (resolution[1]*x, resolution[0]*y))

    tiles.save("./.temp/frames_" + date_time + ".png")

    test_images = []

    for frame in frames:
        # resize image to match model's expected sizing
        image_PIL = Image.fromarray(frame)
        image = ImageOps.fit(image_PIL, (224, 224), Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        test_images.append(normalized_image_array)

    predictions = model.predict(np.array(test_images))

    for pred in predictions:
        print(roundToString(pred[0]), roundToString(
            pred[1]), roundToString(pred[2]))
        if (pred[1] > pred[0] and pred[1] > pred[2]):
            return True
    return False
