# ---------------------------------Customization----------------------------------------


# interval to scroll
minInterval = 2
maxInterval = 30

# chance to like
likeChance = 50


# ---------------------------------Requirements----------------------------------------


import random
import time
from pynput import keyboard





# ---------------------------------SCRIPT----------------------------------------



keyboard_controller = keyboard.Controller()

nombrelike = 0

while True:
    compteurtime = random.randint(minInterval, maxInterval)
    for i in range(compteurtime):
        time.sleep(1)
        compteurlike = random.randint(0, likeChance)
        if compteurlike == likeChance-1:
            keyboard_controller.press("l")
            time.sleep(0.2)
            keyboard_controller.release("l")
            
    keyboard_controller.press(keyboard.Key.down)
    time.sleep(0.2)
    keyboard_controller.release(keyboard.Key.down)