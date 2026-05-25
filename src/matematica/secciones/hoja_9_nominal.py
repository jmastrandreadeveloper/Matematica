"""
Hoja 9: Listado nominal de alumnos por curso (PDF con tabla de alumnos).
Genera un PDFEditor con múltiples páginas (una o más por curso).
"""
import numpy as np
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

from src.libs.pdf.editor import PDFEditor
from src.matematica.filtros import extraer_alumnos_por_escuela_curso, obtener_nivel_escuela

FILAS_POR_PAGINA = 10


def _generar_pdf_nominal_curso(df_tabla, escuela_id, curso, nivel, plantilla_path=None):
    """Genera BytesIO con PDF de la tabla nominal de un curso."""
    import pandas as pd

    cols_excluir = {'Escuela_ID', 'CURSO_NORMALIZADO', 'NIVEL_UNIFICADO'}
    columnas = [c for c in df_tabla.columns if c not in cols_excluir]

    nivel_texto = 'GRADO' if nivel == 'Primario' else 'AÑO'
    titulo = f'{curso} {nivel_texto}'

    total_alumnos = len(df_tabla)
    num_paginas = int(np.ceil(total_alumnos / FILAS_POR_PAGINA)) or 1

    # Obtener tamaño de página
    if plantilla_path:
        try:
            with open(plantilla_path, 'rb') as f:
                reader = PdfReader(f)
                page = reader.pages[0]
                page_width = float(page.mediabox.width)
                page_height = float(page.mediabox.height)
        except Exception:
            page_width, page_height = A4[0], A4[1]
    else:
        page_width, page_height = A4[0], A4[1]

    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(page_width, page_height))

    for pagina in range(num_paginas):
        inicio = pagina * FILAS_POR_PAGINA
        fin = min((pagina + 1) * FILAS_POR_PAGINA, total_alumnos)
        df_pagina = df_tabla.iloc[inicio:fin].copy()

        titulo_y = page_height - 250
        c.setFont('Helvetica-Bold', 14)
        c.setFillColorRGB(0, 0.4, 0.8)
        c.drawString(80, titulo_y, titulo)

        data = [columnas]
        for _, row in df_pagina.iterrows():
            fila = [str(row[col]) if pd.notna(row[col]) else '' for col in columnas]
            data.append(fila)
        for _ in range(FILAS_POR_PAGINA - len(df_pagina)):
            data.append([''] * len(columnas))

        tabla_ancho = page_width * 0.90
        col_widths = [tabla_ancho / len(columnas)] * len(columnas)
        row_height = 20

        tabla = Table(data, colWidths=col_widths, rowHeights=row_height)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 7),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BOX', (0, 0), (-1, -1), 1.5, colors.black),
        ]))

        tabla_x = page_width * 0.02
        tabla_y = page_height * (1 - 0.26 - 0.60)
        tabla.wrapOn(c, tabla_ancho, page_height)
        tabla.drawOn(c, tabla_x, tabla_y)

        if pagina < num_paginas - 1:
            c.showPage()

    c.save()
    buf.seek(0)
    return buf


def hoja_9_nominal(una_escuela: dict, datos: dict, template_path: str, cursos: list):
    """
    Parámetros:
    - datos: dict con df_6_nominal, df_niveles, dict_ejes_con_procesos
    - cursos: lista de CURSO_NORMALIZADO
    """
    escuela_id = una_escuela['Escuela_ID']
    nivel = obtener_nivel_escuela(datos['df_niveles'], escuela_id) or 'Primario'
    etiqueta = 'Grado' if nivel == 'Primario' else 'Año'

    pdfs_por_curso = {}
    for curso in sorted(cursos):
        df_tabla = extraer_alumnos_por_escuela_curso(
            datos['df_6_nominal'],
            escuela_id,
            curso,
            datos['dict_ejes_con_procesos'],
        )
        if df_tabla.empty:
            continue
        try:
            pdf_buf = _generar_pdf_nominal_curso(df_tabla, escuela_id, curso, nivel, template_path)
            pdfs_por_curso[f'{curso} {etiqueta}'] = pdf_buf
            print(f'Hoja 9 nominal generada: escuela {escuela_id}, curso {curso}')
        except Exception as e:
            print(f'Error hoja 9 nominal {escuela_id}/{curso}: {e}')

    if not pdfs_por_curso:
        return None

    # Fusionar todos los PDFs de cursos
    writer = PdfWriter()
    paginas_por_curso = {}
    for label, buf in pdfs_por_curso.items():
        buf.seek(0)
        reader = PdfReader(buf)
        paginas_por_curso[label] = len(reader.pages)
        for p in reader.pages:
            writer.add_page(p)

    buf_final = BytesIO()
    writer.write(buf_final)
    buf_final.seek(0)

    pdf_final = PDFEditor.fusionar_pdfs_desde_bytes(
        [buf_final], escuela_data=una_escuela, nombre_operacion='Hoja 9 Nominales'
    )

    # Agregar destinos de navegación
    pagina_actual = 0
    for label, num_pags in paginas_por_curso.items():
        pdf_final.add_named_destination(f'Listado_nominal_{label}', page_number=pagina_actual)
        pagina_actual += num_pags

    return pdf_final
