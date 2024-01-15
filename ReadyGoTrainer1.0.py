import keyboard
import time
import random
import pygame

def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

while True:
    print("READY...")
    play_sound("audio\\ready.wav")
    wait_until_go = random.uniform(0,1.5)
    time.sleep(wait_until_go)
    print("GO!!!")
    play_sound("audio\\go.wav")

    wait_until_reset = random.uniform(2,3)
    time.sleep(wait_until_reset)

    print('\n')


    if keyboard.is_pressed('esc'):
        print("Exiting the Ready Go Trainer")
        break