from src.libs.pdf.editor import PDFEditor


def caratula(una_escuela: dict, template_path: str):
    pdf = PDFEditor(template_path, '')
    pdf.add_named_destination('caratula', page_number=0)
    pdf.add_text_to_page(
        f'Escuela N° : {una_escuela["Número"]}',
        (30, 80), 0, 'REM-Regular', 25,
        color=(0, 15, 159), align='left',
    )
    pdf.add_text_to_page(
        una_escuela['Escuela'][:31],
        (30, 70), 0, 'REM-Black', 25,
        color=(0, 15, 159), align='left',
    )
    print(f'Carátula generada para escuela {una_escuela["Escuela_ID"]}')
    return pdf
