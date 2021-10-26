# Add sound to mouse click
# Developer: Mohammad Ali Bazzazi (me)

print("""
_______________     __________   _______   _______    _________   _______    #
|              \   |          |        /         /   |         |        /   
|               |  |          |       /         /    |         |       /     |
|              /   |          |      /         /     |         |      /      |
|_____________|    |__________|     /         /      |_________|     /       |
|              \   |          |    /         /       |         |    /        |
|               |  |          |   /         /        |         |   /         |
|              /   |          |  /         /         |         |  /          |
|_____________/    |          | /_______  /_______   |         | /______     |
""")
print("*********************************************************************************")
print("*"+" "*79+"*")
print("*  Copyright of Mohammad Ali Bazzazi, 2021 ©                                    *")
print("*"+" "*79+"*")
print("*  https://www.youtube.com/channel/UCeLKoNs3c72Vc-OG3uNQxGw?sub_confirmation=1  *")
print("*"+" "*79+"*")
print("*********************************************************************************")

################## START ##################

# import library
from pynput.mouse import Listener
from playsound import playsound
import random

# put your musics in the project directory
# Enter name of your musics in list below
musics = ["music_1.mp3", "music_2.mp3", "music_3.mp3"]

# run function below when any mouse button clicked
def on_click(x, y, button, pressed):
    if pressed:
        print("DETECTED!\n")
        playsound(random.choice(musics))
        print("Waiting for any mouse click...")


with Listener(on_click=on_click) as listener:
    print("Waiting for any mouse click...")
    listener.join()

################## END ##################
