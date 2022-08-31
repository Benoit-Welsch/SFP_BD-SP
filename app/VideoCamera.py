from ast import Num
from threading import Thread
import cv2

cam = None


class VideoGet:
    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        self.stopped = True

    def captureFrame(self, numberOfFrame=30):
        frames = []
        for _ in range(numberOfFrame):
            frames.append(self.frame)
        return frames


class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None, number=0):
        self.frame = frame
        self.stopped = False
        self.number = number

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow("Video" + str(self.number), self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True


cam = VideoGet(0)


def threadBoth(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoGet(source).start()
    video_shower = []
    for i in range(3):
        video_shower.append(VideoShow(video_getter.frame, i).start())

    while True:
        if video_getter.stopped or all(th.stopped for th in video_shower):
            video_getter.stop()
            for th in video_shower:
                th.stop()
            break

        frame = video_getter.frame
        for th in video_shower:
            th.frame = frame
