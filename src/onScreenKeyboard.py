import tkinter as tk
import pyautogui
from configurationManager import ConfigurationManager

class OnScreenKeyboard:
    def __init__(self, root):
        self.root = root
        self.configuration = ConfigurationManager()
        self.createKeyboard()

    def createKeyboard(self):
        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', ' '
        ]
        row, col = 1, 0
        for key in keys:
            tk.Button(self.root, text=key, command=lambda k=key: self.pressKey(k)).grid(row=row, column=col)
            col += 1
            if col > 9:
                col = 0
                row += 1

    def pressKey(self, key):
        pyautogui.typewrite(key)