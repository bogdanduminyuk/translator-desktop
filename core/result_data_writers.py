import json

from docx import Document
from docx.shared import Cm, Pt

from core import settings
from .abstracts import ResultDataWriter


class TxtDataWriter(ResultDataWriter):
    def __init__(self, path):
        self.path = path

    def write(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False))


class DocDataWriter(ResultDataWriter):
    def __init__(self, filename, columns_settings):
        self.filename = filename
        self.settings = settings.user["docx-writer"]
        self.columns_settings = columns_settings

    def write(self, data):
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

        def compose_header(cols_settings):
            header_row = ["№\nп/п", "Слово", "Перевод"]
            header_composer = [
                ("syn", "Синонимы"),
                ("ant", "Антонимы"),
                ("def", "Определения")
            ]

            for key, item in header_composer:
                if cols_settings.get(key, False):
                    header_row.append(item)

            return header_row

        def insert_lexical_category(cell, category, key, constraint=None):
            if cell.paragraphs[0].text != "":
                cell.add_paragraph()

            to_be_bold = cell.paragraphs[len(cell.paragraphs) - 1].add_run(category["lexicalCategory"])
            to_be_bold.font.bold = True

            for item in category.get(key, [])[:constraint]:
                cell.add_paragraph("- " + item + ";")

        def insert_header(doc_table, table_header):
            doc_table.add_row()
            for i, cell in enumerate(doc_table.rows[0].cells):
                cell.text = table_header[i]

        document = Document()
        switch_orientation(document)
        set_margins(document, self.settings["margin"])
        change_font(document, self.settings["font-family"], self.settings["font-size"], self.settings["line-spacing"])

        header = compose_header(self.columns_settings)
        table = document.add_table(rows=len(data.keys()), cols=len(header))
        table.style = 'Table Grid'
        insert_header(table, header)

        i = 0

        for word, word_data in data.items():
            i += 1
            row = table.rows[i]
            table_builder = (
                # FIXME: fix idx here! calculate it because if 'syn' does not exist
                # FIXME: it throws tuple IndexError
                (3, "syn", "synonyms", settings.user["output"]["synonyms_count"]),
                (4, "ant", "antonyms", settings.user["output"]["antonyms_count"]),
                (5, "def", "definitions", None),
            )

            row.cells[0].text = str(i)
            row.cells[1].text = word

            for lexical_category in word_data["translation"]["lexicalCategories"]:
                insert_lexical_category(row.cells[2], lexical_category, "translation")

            for lexical_category in word_data["api"]["lexicalEntries"]:
                for idx, settings_key, cat_key, settings_constraint in table_builder:
                    if self.columns_settings.get(settings_key, False):
                        insert_lexical_category(row.cells[idx], lexical_category, cat_key, settings_constraint)

        document.save(self.filename)

        return True
