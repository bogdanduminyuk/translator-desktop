import json
import requests
from . import settings
# import settings


class Database:
    @staticmethod
    def get(word):
        response = requests.get(settings.db_urls["get"], params={"word": word})

        if response.ok:
            data = json.loads(response.text)[0]
            data["translation"] = json.loads(data["translation"])
            data["api"] = json.loads(data["api"])
            data.pop("id")
            return data

    @staticmethod
    def set(word, translation, api):
        data = {
            "word": word,
            "translation": json.dumps(translation, ensure_ascii=False),
            "api": json.dumps(api, ensure_ascii=False),
        }

        response = requests.post(settings.db_urls["set"], data=data)

        return response.ok

    @staticmethod
    def count():
        response = requests.get(settings.db_urls["count"])
        if response.ok:
            return json.loads(response.text)["count"]


if __name__ == "__main__":
    print("count: ", Database.count())
    print("get: ", Database.get("word"))
