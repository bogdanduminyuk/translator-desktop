import dpath


def get_senses_list(source_data):
    """
    Realizes first preparation of input data got from server API.

    :param source_data: data got by request to server's API
    :return: filtrated list of results with lexical categories and senses
    """
    result_list = []

    for i, result in enumerate(source_data["results"]):
        item = {
            "id": result["id"],
            "word": result["word"],
            "language": result["language"],
            "type": result["type"],
            "lexicalEntries": [],
        }

        for lexicalEntry in dpath.util.get(source_data, "results/{i}/lexicalEntries".format(i=i)):
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
            copy_group = []

            for item in group:
                if item not in copied:
                    copy_group.append(item)
                    copied.add(item)

            filtrated_list.append(copy_group)

        return [item for item in filter(lambda x: x != [], filtrated_list)]

    synonyms_groups_list = []
    antonyms_groups_list = []

    for result in senses_list:
        for lexical_entry in result["lexicalEntries"]:
            for sense in lexical_entry["senses"]:
                synonyms_group = []
                antonyms_group = []

                for synonym in sense.get("synonyms", []):
                    synonyms_group.append(synonym["text"])

                for antonym in sense.get("antonyms", []):
                    antonyms_group.append(antonym["text"])

                for sub_sense in sense.get("subsenses", []):
                    for sub_synonym in sub_sense.get("synonyms", []):
                        synonyms_group.append(sub_synonym["text"])

                    for sub_antonym in sub_sense.get("antonyms", []):
                        antonyms_group.append(sub_antonym["text"])

                synonyms_groups_list.append(synonyms_group)
                antonyms_groups_list.append(antonyms_group)

    return __filtrate_group_list__(synonyms_groups_list), __filtrate_group_list__(antonyms_groups_list)


def get_definitions(senses_list):
    pass


if __name__ == "__main__":
    pass
