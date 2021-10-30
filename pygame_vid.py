#!/usr/bin/env python3.7
import cv2
import pygame
import numpy as np

'''Play the thresholded video'''

def thresholded_component(img, lower, upper, component_idx):
    '''Take one component / layer / color and return a map of values between upper and lower'''
    component = img[:,:,component_idx]
    _, lower_thresh = cv2.threshold(component, lower, 1, cv2.THRESH_BINARY)
    _, upper_thresh = cv2.threshold(component, upper, 1, cv2.THRESH_BINARY_INV)
    return lower_thresh * upper_thresh


# Constants to access YCrCb colorspace
Y = 0
Cr = 1
Cb = 2


def draw():
    success, img = cap.read()

    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    blurred_ycc = cv2.GaussianBlur(ycrcb, (11, 11), 0)
    y_thresh = thresholded_component(blurred_ycc, 200, 255, Y)
    cr_thresh = thresholded_component(blurred_ycc, 110, 150, Cr)
    # cb_thresh = thresholded_component(blurred_ycc, 170, 200, Cb)

    combined = y_thresh * (1 - cr_thresh) * 255

    rgb = np.repeat(combined[:,:,np.newaxis], 3, axis=2)

    # vid_surface = pygame.image.frombuffer(img.tobytes(), shape, "BGR")
    vid_surface = pygame.image.frombuffer(rgb, shape, "BGR")
    wn.blit(vid_surface, (0, 0))
    pygame.display.update()

    clock.tick(fps)

    return success


if __name__ == '__main__':
    # This is like setup() in processing
    cap = cv2.VideoCapture('sample_media/bird flying led sample.mp4')
    success, img = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    shape = img.shape[1::-1]

    wn = pygame.display.set_mode(shape)
    clock = pygame.time.Clock()

    # This loop will keep calling our draw function until we quit (e.g., close the windoww), or
    # if capture fails (for now if we reach the end of the video)
    while success:
        success = draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                success = False

    pygame.quit()
