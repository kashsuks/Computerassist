import json

class ConfigurationManager:
    def __init__(self, config_file="config/userSettings.json"):
        self.config_file = config_file
        try:
            with open(self.config_file, "r") as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            self.settings = {}

    def getSetting(self, key, default=None):
        return self.settings.get(key, default)

    def setSetting(self, key, value):
        self.settings[key] = value
        with open(self.config_file, "w") as f:
            json.dump(self.settings, f, indent=4)