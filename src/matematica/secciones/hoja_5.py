"""
Hoja 5: Histogramas de cantidad de respuestas correctas por curso.
Layout dinámico según cantidad de cursos (1–7 imágenes).
"""
from src.libs.pdf.editor import PDFEditor
from src.libs.visualizaciones.histograma import generar_imagen_histograma
from src.matematica.filtros import filtrar_por_escuela_y_curso, obtener_nivel_escuela

ANCHO_HOJA = 210
ALTO_HOJA = 297


def _insertar_imagen_con_etiqueta(pdf, imagen_bytes, curso, x_mm, y_mm, ancho_mm, texto_pos):
    pdf.insertar_imagen_bytes(imagen_bytes, x_mm=x_mm, y_mm=y_mm, page_number=0, ancho_mm=ancho_mm)
    pdf.add_text_to_page(
        curso, texto_pos, page_number=0,
        font_name='REM-Bold', font_size=9,
        color=(255, 255, 255), box=True,
        box_color=(30, 91, 168), box_padding=3, box_border_width=0,
    )


def _generar_imagenes(df_histogramas, df_niveles, cursos, escuela_id, dict_cantidad_preguntas):
    """Genera dict {curso_label: bytes} con los histogramas de cada curso."""
    nivel = obtener_nivel_escuela(df_niveles, escuela_id)
    datos_nivel = {'NIVEL_UNIFICADO': nivel or 'Primario'}
    etiqueta = 'Grado' if nivel == 'Primario' else 'Año'
    imagenes = {}
    for curso in cursos:
        df_curso = filtrar_por_escuela_y_curso(df_histogramas, escuela_id, curso)
        if df_curso.empty:
            continue
        datos_hist = df_curso.iloc[0].to_dict()
        try:
            img = generar_imagen_histograma(
                datos_hist, datos_nivel, dict_cantidad_preguntas,
                figsize=(5, 6), return_bytes=True,
            )
            imagenes[f'{curso} {etiqueta}'] = img
            print(f'Histograma generado: Escuela {escuela_id}, Curso {curso}')
        except Exception as e:
            print(f'Error histograma {escuela_id}/{curso}: {e}')
    return imagenes


def hoja_5(una_escuela: dict, datos: dict, template_path: str, cursos: list):
    """
    Parámetros:
    - datos: dict con df_1_histogramas, df_niveles, dict_cantidad_preguntas
    - cursos: lista de CURSO_NORMALIZADO
    """
    escuela_id = una_escuela['Escuela_ID']
    imagenes_dict = _generar_imagenes(
        datos['df_1_histogramas'],
        datos['df_niveles'],
        cursos,
        escuela_id,
        datos['dict_cantidad_preguntas'],
    )

    if not imagenes_dict:
        return None

    pdf = PDFEditor(template_path, '')
    num = len(imagenes_dict)
    imgs = list(imagenes_dict.values())
    curs = list(imagenes_dict.keys())

    ancho_img = ANCHO_HOJA / 2
    x_izq, x_der = 0, ANCHO_HOJA / 2
    x_centro = (ANCHO_HOJA - ancho_img) / 2

    if num == 1:
        ancho = 180
        x = (ANCHO_HOJA - ancho) / 2
        espacio_enc = 65
        y = espacio_enc + (ALTO_HOJA - espacio_enc - 10 - 120) / 2
        pdf.insertar_imagen_bytes(imgs[0], x_mm=x, y_mm=y, page_number=0, ancho_mm=ancho)
        pdf.add_text_to_page(curs[0], (33, 200), page_number=0, font_name='REM-Bold', font_size=9,
                              color=(255, 255, 255), box=True, box_color=(30, 91, 168), box_padding=3, box_border_width=0)
    elif num == 2:
        alto_img = 100
        espacio_enc = 115
        y = espacio_enc + (ALTO_HOJA - espacio_enc - 10 - alto_img) / 2
        pdf.insertar_imagen_bytes(imgs[0], x_mm=x_izq, y_mm=y, page_number=0, ancho_mm=ancho_img)
        pdf.insertar_imagen_bytes(imgs[1], x_mm=x_der, y_mm=y, page_number=0, ancho_mm=ancho_img)
        pdf.add_text_to_page(curs[0], (33, 200), page_number=0, font_name='REM-Bold', font_size=9,
                              color=(255, 255, 255), box=True, box_color=(30, 91, 168), box_padding=3, box_border_width=0)
        pdf.add_text_to_page(curs[1], (125, 200), page_number=0, font_name='REM-Bold', font_size=9,
                              color=(255, 255, 255), box=True, box_color=(30, 91, 168), box_padding=3, box_border_width=0)
    elif num <= 4:
        # 2 filas de 2 (o 2+1 para num=3)
        alto_img = 75 if num == 3 else 70
        espacio_entre = 9
        espacio_enc = -10
        altura_total = alto_img * 2 + espacio_entre
        espacio_disp = ALTO_HOJA - espacio_enc - 10
        inicio_v = espacio_enc + (espacio_disp - altura_total) / 2
        y_arriba = inicio_v + altura_total - alto_img
        y_abajo = inicio_v

        pdf.insertar_imagen_bytes(imgs[0], x_mm=x_izq, y_mm=y_arriba, page_number=0, ancho_mm=ancho_img)
        if num >= 2:
            pdf.insertar_imagen_bytes(imgs[1], x_mm=x_der, y_mm=y_arriba, page_number=0, ancho_mm=ancho_img)
        if num == 3:
            pdf.insertar_imagen_bytes(imgs[2], x_mm=x_centro, y_mm=y_abajo, page_number=0, ancho_mm=ancho_img)
        elif num == 4:
            pdf.insertar_imagen_bytes(imgs[2], x_mm=x_izq, y_mm=y_abajo, page_number=0, ancho_mm=ancho_img)
            pdf.insertar_imagen_bytes(imgs[3], x_mm=x_der, y_mm=y_abajo, page_number=0, ancho_mm=ancho_img)
        for i, (c, pos_x, pos_y) in enumerate(zip(
            curs[:num],
            [33, 125, 95 if num == 3 else 33, 125][:num],
            [200, 200, 110, 110][:num],
        )):
            pdf.add_text_to_page(c, (pos_x, pos_y), page_number=0, font_name='REM-Bold', font_size=9,
                                  color=(255, 255, 255), box=True, box_color=(30, 91, 168), box_padding=3, box_border_width=0)
    else:
        # 5, 6, 7 → grilla de 3 filas
        alto_img = 55 if num == 6 else 40
        espacio_enc = 90 if num == 6 else 105
        espacio_entre = 15 if num == 6 else 10
        y_fila1 = ALTO_HOJA - espacio_enc - alto_img
        y_fila2 = y_fila1 - alto_img - espacio_entre
        y_fila3 = y_fila2 - alto_img - espacio_entre
        y_fila4 = y_fila3 - alto_img - espacio_entre

        posiciones = [
            (x_izq, y_fila1), (x_der, y_fila1),
            (x_izq, y_fila2), (x_der, y_fila2),
            (x_izq, y_fila3), (x_der, y_fila3),
            (x_centro, y_fila4),
        ]
        for i, img in enumerate(imgs[:num]):
            px, py = posiciones[i]
            pdf.insertar_imagen_bytes(img, x_mm=px, y_mm=py, page_number=0, ancho_mm=ancho_img)

        etiquetas_x = [33, 125, 33, 125, 33, 125, 95]
        etiquetas_y = [200, 200, 124, 124, 52, 52, 40]
        for i, c in enumerate(curs[:num]):
            pdf.add_text_to_page(c, (etiquetas_x[i], etiquetas_y[i]), page_number=0,
                                  font_name='REM-Bold', font_size=9,
                                  color=(255, 255, 255), box=True, box_color=(30, 91, 168),
                                  box_padding=3, box_border_width=0)

    print(f'Hoja 5 generada para escuela {escuela_id} ({num} histogramas)')
    return pdf
