import time
import os
import pygame

DesiredFile = "TextToSpeech.txt"

# Initialization
pygame.music.init()

pygame.music.mixer.load()

def main():
    with open(DesiredFile, "r") as file:
      file.readlines().strip("\n")
      for word in file:
        if word == "a":
          playSong(a)
        elif word == "b":
          playSong(b)
          # continue to Z and other letters and symbols ...
    
def playSong(SongName):
  pygame.music.mixer.play(SongName)
  while pygame.music.mixer.getBussy():
    pass # Wait for completely from start played song to end of song

if __name__ == (__main__):
    main()
