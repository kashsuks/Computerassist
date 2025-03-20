import cv2
import dlib
import pyautogui
import threading
from configurationManager import ConfigurationManager

class EyeTracker:
    def __init__(self):
        self.configuration = ConfigurationManager()
        self.facePredictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.faceDetector = dlib.get_frontal_face_detector()
        self.videoCapture = cv2.VideoCapture(0)
        self.isTracking = False
        self.trackingSensitivity = self.configuration.getSetting("eyeSensitivity", 2.0)

    def startTracking(self):
        self.isTracking = True
        threading.Thread(target=self.trackEyes).start()

    def stopTracking(self):
        self.isTracking = False

    def trackEyes(self):
        while self.isTracking:
            ret, frame = self.videoCapture.read()
            if not ret:
                break

            grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detectedFaces = self.faceDetector(grayFrame)

            for face in detectedFaces:
                landmarks = self.facePredictor(grayFrame, face)
                leftEyeCenter = self.getEyeCenter(landmarks, 36, 39)
                rightEyeCenter = self.getEyeCenter(landmarks, 42, 45)

                if leftEyeCenter and rightEyeCenter:
                    averageX = (leftEyeCenter[0] + rightEyeCenter[0]) / 2
                    averageY = (leftEyeCenter[1] + rightEyeCenter[1]) / 2

                    screenX = int(averageX * self.trackingSensitivity)
                    screenY = int(averageY * self.trackingSensitivity)

                    pyautogui.moveTo(screenX, screenY)

            cv2.imshow("Eye Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.videoCapture.release()
        cv2.destroyAllWindows()

    def getEyeCenter(self, landmarks, start, end):
        points = []
        for n in range(start, end + 1):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            points.append((x, y))

        if points:
            averageX = sum(p[0] for p in points) / len(points)
            averageY = sum(p[1] for p in points) / len(points)
            return (int(averageX), int(averageY))
        return None

    def setSensitivity(self, sensitivity):
        self.trackingSensitivity = sensitivity
        self.configuration.setSetting("eyeSensitivity", sensitivity)