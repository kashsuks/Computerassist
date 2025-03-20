import speech_recognition as sr
import pyttsx3
import threading
import pyautogui
from configurationManager import ConfigurationManager

class VoiceControl:
    def __init__(self):
        self.speechRecognizer = sr.Recognizer()
        self.textToSpeechEngine = pyttsx3.init()
        self.isListening = False
        self.configuration = ConfigurationManager()

    def startListening(self):
        self.isListening = True
        threading.Thread(target=self.listenForCommands).start()

    def stopListening(self):
        self.isListening = False

    def listenForCommands(self):
        with sr.Microphone() as source:
            while self.isListening:
                try:
                    audioData = self.speechRecognizer.listen(source, timeout=5)
                    recognizedText = self.speechRecognizer.recognize_google(audioData)
                    self.processCommand(recognizedText.lower())
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

    def processCommand(self, command):
        if "click" in command:
            pyautogui.click()
            self.speakText("Clicking")
        elif "scroll up" in command:
            pyautogui.scroll(100)
            self.speakText("Scrolling up")
        elif "scroll down" in command:
            pyautogui.scroll(-100)
            self.speakText("Scrolling down")
        elif "double click" in command:
            pyautogui.doubleClick()
            self.speakText("Double clicking")
        elif "right click" in command:
            pyautogui.rightClick()
            self.speakText("Right clicking")

    def speakText(self, text):
        self.textToSpeechEngine.say(text)
        self.textToSpeechEngine.runAndWait()