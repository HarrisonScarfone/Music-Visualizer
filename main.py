import pygame
import pygame.image
import sys
import time

import numpy
from numpy.fft import fft
import time

from bars import Visualization
from fft_data import FFT_Handler

import random
 
def main():
     
    pygame.init()
    pygame.display.set_caption("Test")
     
    DISPLAY = pygame.display.set_mode((800,800))
     
    WHITE = (255,255,255)

    DISPLAY.fill(WHITE)

    sound = pygame.mixer.Sound('a.wav')
    
    fft_handler = FFT_Handler(sound)


    visualization = Visualization()
    visualization.make_update_sprites(DISPLAY)

    clock = pygame.time.Clock()
    clock.tick()
    last_time = 0
    curr_time = 100

    fft_handler.play_sound()


    while True:

        try:
            vals = fft_handler.get_normalized_additive_channel_bins(last_time / 1000, curr_time / 1000)
            visualization.make_update_sprites(DISPLAY, vals)

            pygame.transform.flip(DISPLAY, True, False)
            pygame.display.flip()
        except:
            pass

        t = clock.tick()
        last_time += t
        curr_time += t


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__=="__main__":
    main()
