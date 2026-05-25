from src.libs.pdf.editor import PDFEditor


def hojas_1_2_3(una_escuela: dict, template_path: str):
    pdf = PDFEditor(template_path, '')
    pdf.add_named_destination('1-2-3', page_number=0)
    print(f'Hojas 1-2-3 generadas para escuela {una_escuela["Escuela_ID"]}')
    return pdf
