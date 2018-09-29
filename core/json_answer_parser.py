import json


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
            "id": result["id"],
            "word": result["word"],
            "language": result["language"],
            "type": result["type"],
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

        :param group_list: list of synonyms or antonyms group (doesn't matter).
        :return: filtrated list without copies and empty lists.
        """
        copied = set()
        filtrated_list = []

        for group in group_list:
            temp_str = ""

            for item in group:
                if item not in copied:
                    temp_str += item + ";"
                    copied.add(item)

            filtrated_list.append(temp_str)

        return [item for item in filter(lambda x: x != "", filtrated_list)]

    synonyms_groups_list = []
    antonyms_groups_list = []

    for result in senses_list:
        for lexical_entry in result["lexicalEntries"]:
            for sense in lexical_entry["senses"]:
                synonyms_groups_list.append(
                    [synonym["text"] for synonym in sense.get("synonyms", [])]
                )
                antonyms_groups_list.append(
                    [antonym["text"] for antonym in sense.get("antonyms", [])]
                )

    return __filtrate_group_list__(synonyms_groups_list), __filtrate_group_list__(antonyms_groups_list)


def get_definitions(senses_list):
    """
    Analyzes senses list that can be got by calling `get_senses_list(source_data)`.

    :param senses_list: senses_list: filtrated list of results
    :return: list of lists of definitions
    """
    definitions_list = []

    for result in senses_list:
        for lexical_entry in result["lexicalEntries"]:
            definitions = []

            for sense in lexical_entry["senses"]:
                for definition in sense.get("definitions", []):
                    definitions.append(definition)

            definitions_list.append(definitions)

    return definitions_list


if __name__ == "__main__":
    pass
