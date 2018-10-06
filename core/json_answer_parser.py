import json
from core import settings


def get_senses_list(source_data):
    """
    Realizes first preparation of input data got from server API.

    :param source_data: data got by request to server's API
    :return: filtrated list of results with lexical categories and senses
    """
    result_list = []
    source_data = json.loads(source_data)

    for i, result in enumerate(source_data["results"]):
        item = {
            # "id": result["id"],
            # "word": result["word"],
            # "language": result["language"],
            # "type": result["type"],
            "lexicalEntries": [],
        }

        for lexicalEntry in result["lexicalEntries"]:
            senses = []

            for entry in lexicalEntry["entries"]:
                for sense in entry["senses"]:
                    senses.append(sense)

            item["lexicalEntries"].append({
                "lexicalCategory": lexicalEntry["lexicalCategory"],
                "senses": senses
            })

        result_list.append(item)

    return result_list


def get_synonyms_antonyms(senses_list):
    """
    Analyzes senses list that can be got by calling `get_senses_list(source_data)`.

    :param senses_list: filtrated list of results
    :return: tuple of group lists for synonyms and antonyms.
    """
    def __filtrate_group_list__(group_list):
        """
        Removes copies of synonyms and antonyms from different groups.
        Converts list of lists into list of strings. Now group will be
        represented ad string of values divided with delimiter.

        :param group_list: list of synonyms or antonyms group (doesn't matter).
        :return: filtrated list without copies and empty strings.
        """
        copied = set()
        filtrated_list = []

        for group in group_list:
            temp_str = ""

            for item in group:
                if item not in copied:
                    temp_str += item + settings.user["advanced"]["delimiter"]
                    copied.add(item)

            temp_str = temp_str[:-1]
            filtrated_list.append(temp_str)

        return [item for item in filter(lambda x: x != "", filtrated_list)]

    for result in senses_list:
        for lexical_entry in result["lexicalEntries"]:
            lexical_entry["synonyms"] = []
            lexical_entry["antonyms"] = []

            for sense in lexical_entry["senses"][:settings.user["advanced"]["database"]["save_category_senses_count"]]:
                lexical_entry["synonyms"].append(
                    [synonym["text"] for synonym in sense.get("synonyms", [])[:settings.user["advanced"]["database"]["save_items_count"]]]
                )
                lexical_entry["antonyms"].append(
                    [antonym["text"] for antonym in sense.get("antonyms", [])[:settings.user["advanced"]["database"]["save_items_count"]]]
                )

            lexical_entry["synonyms"] = __filtrate_group_list__(lexical_entry["synonyms"])
            lexical_entry["antonyms"] = __filtrate_group_list__(lexical_entry["antonyms"])
            lexical_entry.pop("senses", None)

    return senses_list


def get_definitions(senses_list):
    """
    Analyzes senses list that can be got by calling `get_senses_list(source_data)`.

    :param senses_list: senses_list: filtrated list of results
    :return: updated senses list
    """
    for result in senses_list:
        for lexical_entry in result["lexicalEntries"]:
            definitions = []

            for sense in lexical_entry["senses"]:
                for definition in sense.get("definitions", []):
                    definitions.append(definition)

            lexical_entry["definitions"] = definitions
            lexical_entry.pop("senses", None)

    return senses_list


if __name__ == "__main__":
    pass
