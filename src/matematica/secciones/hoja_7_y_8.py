"""
Hojas 7 y 8: Para cada curso, página 7 = gráfico sub-eje + tabla procesos cognitivos;
              página 8 = tabla de opciones de respuesta seleccionadas.
Genera un PDFEditor con múltiples páginas (2 por curso).
"""
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

from src.libs.pdf.editor import PDFEditor
from src.libs.visualizaciones.grafico_subeje import graficar_efectividad_por_eje
from src.libs.visualizaciones.tabla_procesos import generar_tabla_procesos
from src.matematica.filtros import (
    filtrar_graficos_subeje,
    filtrar_tabla_procesos,
    filtrar_opcion_respuesta,
    obtener_nivel_escuela,
)

ALTURA_PAGINA_MM = 297


def hoja_7_y_8(una_escuela: dict, datos: dict, template_path: str, cursos: list):
    """
    Parámetros:
    - datos: dict con df_3_graficos_subeje, df_4_tabla_procesos, df_5_item_opcion,
             df_niveles, dict_pregunta_respuesta
    - cursos: lista de CURSO_NORMALIZADO
    """
    if not template_path:
        return None

    escuela_id = una_escuela['Escuela_ID']
    nivel_str = obtener_nivel_escuela(datos['df_niveles'], escuela_id) or 'Primario'
    datos_nivel = {'NIVEL_UNIFICADO': nivel_str}

    todas_las_paginas = []

    for curso in sorted(cursos):
        # ---- PÁGINA 7: gráfico sub-eje + tabla procesos ----
        ed1 = PDFEditor(template_path, una_escuela)
        ed1.add_text_to_page(
            curso, (30, 230), page_number=0,
            font_name='REM-Bold', font_size=9,
            color=(255, 255, 255), box=True,
            box_color=(30, 91, 168), box_padding=3, box_border_width=0,
        )

        # Gráfico sub-eje
        datos_subeje = filtrar_graficos_subeje(datos['df_3_graficos_subeje'], escuela_id, curso)
        if datos_subeje:
            try:
                img_graf = graficar_efectividad_por_eje(
                    datos_subeje, datos_nivel,
                    figsize=(10, 6), return_bytes=True,
                )
                ed1.insertar_imagen_bytes_segura(
                    img_graf, x_mm=31, y_mm=150, page_number=0,
                    ancho_mm=115, ajustar_si_excede=True, debug=False,
                )
            except Exception as e:
                print(f'Error gráfico sub-eje {escuela_id}/{curso}: {e}')

        # Tabla procesos cognitivos
        datos_proc = filtrar_tabla_procesos(datos['df_4_tabla_procesos'], escuela_id, curso)
        if datos_proc:
            try:
                img_proc = generar_tabla_procesos(datos_proc, return_bytes=True, altura_fila=0.5)
                img_obj = Image.open(BytesIO(img_proc))
                ancho_px, altura_px = img_obj.size
                dpi = img_obj.info.get('dpi', (72, 72))[1]
                altura_mm = (altura_px / dpi) * 25.4
                ancho_mm_orig = (ancho_px / dpi) * 25.4
                ancho_des = 120
                escala = ancho_des / ancho_mm_orig
                y_sup = 160
                y_aba = ALTURA_PAGINA_MM - y_sup - (altura_mm * escala)
                ed1.insertar_imagen_bytes_segura(
                    img_proc, x_mm=31, y_mm=y_aba, page_number=0,
                    ancho_mm=ancho_des, ajustar_si_excede=True, debug=False,
                )
            except Exception as e:
                print(f'Error tabla procesos {escuela_id}/{curso}: {e}')

        stream1 = ed1.save_to_stream()
        stream1.seek(0)
        for p in PdfReader(stream1).pages:
            todas_las_paginas.append(p)

        # ---- PÁGINA 8: tabla opciones de respuesta ----
        # La generación de esta tabla requiere crear_tabla_resultados (complejo).
        # Se inserta como página vacía del template por ahora si no hay datos.
        datos_opc = filtrar_opcion_respuesta(datos['df_5_item_opcion'], escuela_id, curso)
        if datos_opc and 'crear_tabla_respuestas' in datos:
            try:
                img_opc = datos['crear_tabla_respuestas'](
                    datos_opc,
                    datos.get('dict_pregunta_respuesta', {}),
                    curso,
                    nivel=nivel_str,
                    return_bytes=True,
                )
                ed2 = PDFEditor(template_path, una_escuela)
                ed2.insertar_imagen_bytes_segura(
                    img_opc, x_mm=10, y_mm=50, page_number=0,
                    ancho_mm=190, ajustar_si_excede=True, debug=False,
                )
                stream2 = ed2.save_to_stream()
                stream2.seek(0)
                for p in PdfReader(stream2).pages:
                    todas_las_paginas.append(p)
            except Exception as e:
                print(f'Error tabla opciones {escuela_id}/{curso}: {e}')
        else:
            # Página 8 vacía (solo template)
            ed2 = PDFEditor(template_path, '')
            stream2 = ed2.save_to_stream()
            stream2.seek(0)
            for p in PdfReader(stream2).pages:
                todas_las_paginas.append(p)

        print(f'Hojas 7 y 8 generadas: escuela {escuela_id}, curso {curso}')

    if not todas_las_paginas:
        return None

    writer = PdfWriter()
    for p in todas_las_paginas:
        writer.add_page(p)
    buf = BytesIO()
    writer.write(buf)
    buf.seek(0)

    pdf_final = PDFEditor(buf, una_escuela)
    return pdf_final
