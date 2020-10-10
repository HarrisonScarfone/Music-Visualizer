import pygame
import numpy

from numpy.fft import fft
from math import log10

class FFT_Handler:

    def __init__(self, sound):
        
        self.sound = sound
        self.audio_as_sound_array = pygame.sndarray.array(self.sound)
        self.audio_as_np_array = numpy.array(self.audio_as_sound_array)

        self.left_channel = self.audio_as_np_array[:,0]
        self.right_channel = self.audio_as_np_array[:,1]

        self.playback_frequency, self.file_format, self.is_stereo = pygame.mixer.get_init()
        self.playback_frequency = 1./self.playback_frequency

        self.sample_rate = 0.001
        self.sample_num = int(self.playback_frequency * self.sample_rate)


    def get_bin_heights(self, arr, start, stop, bins=75):

        start_position = int(start / self.playback_frequency)
        stop_position = int(stop / self.playback_frequency)
        # sample_interval = stop - start
        num_of_samples = stop_position - start_position        

        spectrum = fft(arr[start_position:stop_position])
        power = numpy.abs(spectrum)[:num_of_samples // 2] * 1 / num_of_samples

        # seem like the frequency isn't needed? i can just draw it relative?        
        # frequency = numpy.linspace(0, 10 / sample_interval, num_of_samples)[:num_of_samples // 2]

        bin_power = []
        step = (len(power) // bins) + 1
        i, curr_power = 0, 0
        while i < len(power):
            if i % step == 0:
                bin_power.append(curr_power)
                curr_power = 0
            else:
                curr_power += power[i]
            i += 1
        bin_power.append(curr_power)

        return bin_power
        

    def get_left_channel(self, start, stop):
        return self.get_bin_heights(self.left_channel, start, stop)
    
    def get_right_channel(self, start, stop):
        return self.get_bin_heights(self.right_channel, start, stop)
    
    def get_normalized_additive_channel_bins(self, start, stop):
        left = self.get_left_channel(start, stop)
        right = self.get_right_channel(start, stop)
        avg = []
        for i, (l, r) in enumerate(zip(left, right)):
            # seems like any bar over needs some help
            # any bar over 25 really needs it lmfao
            # due to not logarithmically grouping power?
            # scale down the bass settings lol
            if i > 25:
                avg.append((l+r) * 1.3)
            elif i > 10:
                avg.append((l+r))
            else:
                avg.append((l+r)//2 * 0.6)

        return avg / numpy.amax(numpy.absolute(avg)) * 300

    def play_sound(self):
        self.sound.play()
