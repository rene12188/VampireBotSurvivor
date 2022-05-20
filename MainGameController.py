import win32gui
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import time

from StartUpGameLogic import StartUpGameLogic


class MainGameController:
    def __init__(self):
        self.__StartUp = StartUpGameLogic()

    def StartRun(self):
        print("Starting Game:")
        self.__StartUp.StartUpGame()
        pass


    def __mainGameLoop(self):

        #while true:



        pass

    def __grabImage(self):
        hwnd = win32gui.FindWindow(None, r'Vampire Survivors')
        win32gui.SetForegroundWindow(hwnd)
        dimensions = win32gui.GetWindowRect(hwnd)

        image = ImageGrab.grab(dimensions)
        image.show()