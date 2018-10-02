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

    records = stub_rows()

    table = document.add_table(rows=len(records), cols=6)
    table.style = 'Table Grid'

    for i, row in enumerate(table.rows):
        for j, cell in enumerate(row.cells):
            cell.text = records[i][j]

    document.save('demo.docx')