import py5
import cv2 as cv

WIDTH, HEIGHT = 1280, 720

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.rect_mode(py5.CENTER)

    global webcam
    webcam = cv.VideoCapture(1, cv.CAP_DSHOW,
                             params=(cv.CAP_PROP_FRAME_WIDTH, WIDTH,
                                     cv.CAP_PROP_FRAME_HEIGHT, HEIGHT,
                                     # This doesn't seem to do anything
                                     # I think we get data in BGR
                                     cv.CAP_PROP_CONVERT_RGB, True))

def draw():
    _, cv_image = webcam.read()
    # This doesn't seem to support arbitrary order - so we need to re-order our numpy array
    frame_image = py5.create_image_from_numpy(cv_image, 'RGB')
    py5.image(frame_image, 0, 0)
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
