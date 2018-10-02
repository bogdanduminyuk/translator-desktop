import json

from docx import Document
from docx.shared import Cm, Pt


def get_settings():
    return {
        "font-family": "Times New Roman",
        "font-size": 12,
        "line-spacing": 1.15,
        "margin": [1, 1, 1, 1],
    }


def stub_rows():
    return (
        ('№\nп/п', 'Слово', 'Перевод', 'Синонимы', 'Антонимы', 'Определения'),
        ('1', 'word', 'translation', 'synonyms', 'antonyms', 'definitions'),
        ('2', 'word', 'translation', 'synonyms', 'antonyms', 'definitions'),
        ('3', 'word', 'translation', 'synonyms', 'antonyms', 'definitions'),
        ('4', 'word', 'translation', 'synonyms', 'antonyms', 'definitions'),
        ('5', 'word', 'translation', 'synonyms', 'antonyms', 'definitions'),
    )


def get_records():
    def get_data():
        with open("data/output.txt", "r", encoding="utf-8") as file:
            return json.loads(file.read())

    def get_translations(data):
        return {
            word: value["translations"]["simple"]
            for word, value in data.items()
        }

    def parse_api(data):
        displayed_data = []
        synonyms, antonyms, definitions = "", "", ""

        for word in data.keys():
            lexical_entries = data[word]["api"][0]["lexicalEntries"]

            for lexical_category in lexical_entries:
                synonyms_list = lexical_category.get("synonyms", [])
                antonyms_list = lexical_category.get("antonyms", [])
                definitions_list = lexical_category.get("definitions", [])

                if synonyms_list:
                    synonyms += "Категория: " + lexical_category["lexicalCategory"] + "\n"
                    for synonym in synonyms_list:
                        synonyms += synonym + "\n"

                if antonyms_list:
                    antonyms += "Категория: " + lexical_category["lexicalCategory"] + "\n"
                    for antonym in antonyms_list:
                        antonyms += antonym + "\n"

                if definitions_list:
                    definitions += "Категория: " + lexical_category["lexicalCategory"] + "\n"
                    for definition in definitions_list:
                        definitions += definition + "\n"

            displayed_data.append((
                word, synonyms, antonyms, definitions
            ))

        return displayed_data

    data = get_data()
    translations = get_translations(data)
    parsed_api = parse_api(data)

    rows = []

    i = 1

    for word, synonyms, antonyms, definitions in parsed_api:
        rows.append(
            (str(i), word, translations[word], synonyms, antonyms, definitions)
        )
        i += 1

    return rows


def switch_orientation(doc):
    section = doc.sections[-1]
    new_width, new_height = section.page_height, section.page_width
    section.orientation = not section.orientation
    section.page_width = new_width
    section.page_height = new_height


def set_margins(doc, margin):
    section = doc.sections[-1]
    section.top_margin = Cm(margin[0])
    section.right_margin = Cm(margin[1])
    section.bottom_margin = Cm(margin[2])
    section.left_margin = Cm(margin[3])


def change_font(doc, family, size, interval):
    style = doc.styles['Normal']
    style.font.name = family
    style.font.size = Pt(size)
    style.paragraph_format.line_spacing = interval


if __name__ == "__main__":
    document = Document()
    settings = get_settings()

    # TODO: уточнить
    # switch_orientation(document)

    set_margins(document, settings["margin"])
    change_font(document, settings["font-family"], settings["font-size"], settings["line-spacing"])

    # records = stub_rows()
    records = get_records()

    table = document.add_table(rows=len(records), cols=6)
    table.style = 'Table Grid'

    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            cell.text = records[i][j]

    document.save('demo.docx')