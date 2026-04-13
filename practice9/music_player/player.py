import pygame
import os
class MusicPlayer:
    def __init__(self, playlist):
        self.playlist=playlist
        self.current=0

    def play(self):
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current=(self.current+1)%len(self.playlist)
        self.play()

    def previous_track(self):
        self.current=(self.current-1)%len(self.playlist)
        self.play()

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.current])
    