from pynput.keyboard import Key, Controller
import time


class StartUpGameLogic:

    def __init__(self):
        self.__keyboard = Controller()

    def StartUpGame(self):
        print("Starting StartUp Routine:")
        time.sleep(3)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)
        time.sleep(1)
        self.__keyboard.press("d")
        self.__keyboard.release("d")
        time.sleep(1)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)

        time.sleep(1)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)
        time.sleep(1)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)
        time.sleep(1)
        self.__keyboard.press(Key.enter)
        self.__keyboard.release(Key.enter)
        time.sleep(1)
        print("Game Started")

