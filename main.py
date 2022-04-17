import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle for bird
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit('down')     # KEY_UP: To duck down from birds
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit('up')       # KEY_UP: To jump from obstacles(CACTUS)
                return
    return

if __name__ == "__main__":
    print("Hey...Dino game about to start in 3 seconds")
    time.sleep(2)
    #hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # Setting the rectangle[(VALUES)(I = X, J = Y)] to detect the bird and cactus
'''''''''''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0

        # Draw the rectangle for bird
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171

        image.show()
        break
'''''''''