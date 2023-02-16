# ---------------------------------Customization----------------------------------------


# interval to scroll
minInterval = 2
maxInterval = 30

# chance to like
ActiveAutoLike = True
likeChance = 20


# ---------------------------------Requirements----------------------------------------


import random
import time
from pynput import keyboard





# ---------------------------------SCRIPT----------------------------------------



keyboard_controller = keyboard.Controller()

nombrelike = 0

while True:
    compteurtime = random.randint(minInterval, maxInterval)
    print(compteurtime)
    for i in range(compteurtime):
        print(f"Elapsed time: {i+1} seconds out of {compteurtime}")
        time.sleep(1)
        compteurlike = random.randint(0, likeChance)
        if ActiveAutoLike == True:
            if compteurlike == likeChance-1: # Correction: use 1 instead of 50 to make the condition true
                nombrelike = nombrelike + 1
                print(f'Number of likes given: {nombrelike}')
                keyboard_controller.press("l")
                time.sleep(0.2)
                keyboard_controller.release("l")
            
    keyboard_controller.press(keyboard.Key.down)
    time.sleep(0.2)
    keyboard_controller.release(keyboard.Key.down)
