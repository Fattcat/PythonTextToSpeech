import time
import os
import pygame

# Definícia súboru s textom
DesiredFile = "TextToSpeech.txt"

# Inicializácia pygame mixéra
pygame.mixer.init()

# Definovanie cesty k súborom piesní (príklady)
audio_files = {
    "a": "song_a.mp3",
    "b": "song_b.mp3",
    "c": "song_c.mp3",
    "d": "song_d.mp3",
    "e": "song_e.mp3",
    "f": "song_f.mp3",
    "g": "song_g.mp3",
    "h": "song_h.mp3",
    "i": "song_i.mp3",
    "j": "song_j.mp3",
    # Pridajte ďalšie písmená a ich odpovedajúce piesne
}

def main():
    # Otvárame súbor na čítanie
    if not os.path.exists(DesiredFile):
        print(f"Error: File '{DesiredFile}' not found.")
        return
    
    with open(DesiredFile, "r") as file:
        for line in file:
            word = line.strip("\n")  # Odstránenie koncového znaku nového riadku
            if word in audio_files:
                playSong(audio_files[word])
            else:
                print(f"No audio found for: {word}")

def playSong(song_path):
    # Kontrola, či súbor existuje
    if not os.path.exists(song_path):
        print(f"Error: Song file '{song_path}' not found.")
        return

    # Prehrávanie piesne
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    # Čakáme, kým pieseň dohrá
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)  # Malé oneskorenie na zníženie CPU záťaže

if __name__ == "__main__":
    main()
