import tkinter as tk
from eyeTracking import EyeTracker
from voiceControl import VoiceControl
from onScreenKeyboard import OnScreenKeyboard
from configurationManager import ConfigurationManager

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Accessible Control")
        self.eyeTracker = EyeTracker()
        self.voiceControl = VoiceControl()
        self.configuration = ConfigurationManager()
        self.createUI()

    def createUI(self):
        tk.Button(self.root, text="Start Eye Tracking", command=self.eyeTracker.startTracking).pack()
        tk.Button(self.root, text="Stop Eye Tracking", command=self.eyeTracker.stopTracking).pack()
        tk.Button(self.root, text="Start Voice Control", command=self.voiceControl.startListening).pack()
        tk.Button(self.root, text="Stop Voice Control", command=self.voiceControl.stopListening).pack()
        tk.Button(self.root, text="Open Keyboard", command=self.openKeyboard).pack()

    def openKeyboard(self):
        keyboardWindow = tk.Toplevel(self.root)
        OnScreenKeyboard(keyboardWindow)