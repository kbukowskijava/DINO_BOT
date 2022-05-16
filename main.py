from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time


class DinoBot:
    def __init__(self, replaybtn, dino):
        self.replaybtn = replaybtn
        self.dino = dino

    def restartgame(self):
        # koordynaty 2560x422
        pyautogui.click(self.replaybtn)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')

    def grabimage(self):
        box = (self.dino[0] + 35, self.dino[1], self.dino[0] + 75, self.dino[1] + 30)
        image = ImageGrab.grab(box, False, True)
        image.save("RGBFileSave.jpg")
        greyImage = ImageOps.grayscale(image)
        greyImage.save("LFileSave.jpg")
        # 30x40 px = 1200px
        imageArray = array(greyImage.getcolors())
        return imageArray.sum()

    def start(self):
        self.restartgame()
        while True:
            if self.grabimage() != 1447:
                self.jump()

def main():
    # koordynaty dino 2325, 426
    bot = DinoBot((2560, 422), (2325, 426))
    bot.start()


if __name__ == '__main__':
    main()
