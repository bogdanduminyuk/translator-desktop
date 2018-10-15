import json
import os


APP_DIR = os.path.join(os.environ["LOCALAPPDATA"], "translator")

if not os.path.exists(APP_DIR):
    os.mkdir(APP_DIR)


class UserSettings:
    file = os.path.join(APP_DIR, "user.json")
    storage = {}

    @staticmethod
    def set_default():
        UserSettings.storage = {
            "general": {
                "application_id": "fadf5485",
                "application_key": "48fbdacce1908543d0229902ed1917e9"
            },

            "advanced": {
                "request_timeout": 5,
                "request_interval": 1,
                "delimiter": ";",
                "database": {
                    "save_category_senses_count": 20,
                    "save_items_count": 7
                }
            },

            "output": {
                "synonyms_count": 5,
                "antonyms_count": 5
            },

            "docx-writer": {
                "font-family": "Times New Roman",
                "font-size": "12",
                "line-spacing": "1.15",
                "margin": [1, 1, 1, 1]
            }
        }

    @staticmethod
    def get():
        if not os.path.exists(UserSettings.file):
            UserSettings.set_default()
        else:
            with open(UserSettings.file, "r", encoding="utf-8") as f:
                UserSettings.storage = json.load(f)

        return UserSettings.storage

    @staticmethod
    def write():
        with open(UserSettings.file, "w", encoding="utf-8") as f:
            json.dump(UserSettings.storage, f, indent=4)
