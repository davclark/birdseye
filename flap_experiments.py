import py5
import cv2 as cv

WIDTH, HEIGHT = 1280, 720

def setup():
    py5.size(WIDTH, HEIGHT)
    py5.rect_mode(py5.CENTER)

    global webcam
    # Hopefully we can just hard-code this - for now, my built-in webcam is device 0, and a USB webcam is device 1
    # But we might be able to build in something to enumerate and select cameras if needed
    # cv.CAP_ANY doesn't seem to work for my USB webcam on Linux, so I'm hard-coding a robust Windows soludion that uses
    # DirectShow
    webcam = cv.VideoCapture(0, cv.CAP_DSHOW,
                             params=(cv.CAP_PROP_FRAME_WIDTH, WIDTH,
                                     cv.CAP_PROP_FRAME_HEIGHT, HEIGHT,
                                     # This doesn't seem to do anything
                                     # we get data in BGR either way
                                     # cv.CAP_PROP_CONVERT_RGB, True
                                     ))

def draw():
    _, cv_image = webcam.read()

    # Detecting bright spots can use something like:
    # https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
    # https://stackoverflow.com/questions/51846933/finding-bright-spots-in-a-image-using-opencv?rq=1

    # Py5 / processing doesn't support arbitrary order - so we need to re-order our numpy array from BGR to RGB
    # 2::-1 counts down from 2 to the "end" (which is the beginning of the array since we're going backwords)
    # We only reverse the last (third) dimension, but a similar approach could handle left-right or up-down reversal
    # Height is the first dimension and width is the second
    frame_image = py5.create_image_from_numpy(cv_image[:,:,2::-1], 'RGB')
    py5.image(frame_image, 0, 0)
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

py5.run_sketch()
