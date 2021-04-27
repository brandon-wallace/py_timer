#!/usr/bin/env python3
'''
A Python timer that counts down to zero.

Requirements: Python 3.4+
'''

import time
from pathlib import Path, PosixPath
from playsound import playsound


buzzer = Path('audio/game-show-buzzer-sound-effect.mp3')

def countdown(min):
    '''Countdown to zero'''

    sec = 60
    running = True
    print(f'STARTING COUNTDOWN FROM {min:02d}m:00s')

    while running:
        if sec == 60:
            min -= 1
        sec -= 1
        time.sleep(1)
        print(f'TIME REMAINING: {min:02d}m:{sec:02d}s', end='\r')
        if sec == 0:
            if min == 0:
                running = False
                playsound(str(buzzer))
            sec = 60


try:
    minutes = int(input('Enter start time in minutes: '))
except ValueError:
    print('Error: Please provide a number as input.')
    exit()

# Hide the terminal cursor.
print("\x1b[?25l")
countdown(minutes)
# Show the terminal cursor.
print("\x1b[?25h")
print('TIME\'S UP!')
