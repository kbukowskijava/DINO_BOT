from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *

class DinoBot:
    def __init__(self, replaybtn):
        self.replaybtn = replaybtn

    def restartgame(self):
        #koordynaty 2560x422
        pyautogui.click(self.replaybtn)

def main():
    bot = DinoBot((2560, 422))
    bot.restartgame()

if __name__ == '__main__':
    main()