#!/usr/bin/env python3.7
import cv2
import pygame

'''Play the video at 60 fps irrespective of video'''

cap = cv2.VideoCapture('sample_media/bird flying led sample.mp4')
success, img = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)
shape = img.shape[1::-1]

wn = pygame.display.set_mode(shape)
clock = pygame.time.Clock()

while success:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            success = False
    vid_surface = pygame.image.frombuffer(img.tobytes(), shape, "BGR")
    wn.blit(vid_surface, (0, 0))
    pygame.display.update()

    success, img = cap.read()
    clock.tick(fps)

pygame.quit()
