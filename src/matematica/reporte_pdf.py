"""
Generador de reportes PDF por escuela para Matemática.
Orquesta la carga de datos, generación de secciones y guardado del PDF final.
"""
import os
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter

import src.paths as paths
from src.libs.io.utils import cargar_csv
from src.matematica.filtros import (
    obtener_escuelas,
    obtener_cursos_escuela,
    obtener_nivel_escuela,
    filtrar_datos_institucionales,
)
from src.matematica.secciones.caratula import caratula
from src.matematica.secciones.hojas_1_2_3 import hojas_1_2_3
from src.matematica.secciones.hoja_4 import hoja_4
from src.matematica.secciones.hoja_5 import hoja_5
from src.matematica.secciones.hoja_6 import hoja_6
from src.matematica.secciones.hoja_7_y_8 import hoja_7_y_8
from src.matematica.secciones.hoja_9_nominal import hoja_9_nominal


def cargar_datos(cfg) -> dict:
    """
    Carga todos los CSVs necesarios para el reporte.
    Retorna un dict con todos los DataFrames y dicts de config.
    """
    raw = cfg.RAW_MATEMATICA
    raw_nom = cfg.RAW_NOMINAL

    datos = {
        'df_0_alcance':         cargar_csv(os.path.join(raw, 'df_0_Alcance.csv')),
        'df_1_histogramas':     cargar_csv(os.path.join(raw, 'df_1_Histogramas.csv')),
        'df_2_efectividad':     cargar_csv(os.path.join(raw, 'df_2_Efectividad.csv')),
        'df_3_graficos_subeje': cargar_csv(os.path.join(raw, 'df_3_Graficos_subeje.csv')),
        'df_4_tabla_procesos':  cargar_csv(os.path.join(raw, 'df_4_Tabla_procesos.csv')),
        'df_5_item_opcion':     cargar_csv(os.path.join(raw, 'df_5_Item_opcion_elegida.csv')),
        'df_6_nominal':         cargar_csv(os.path.join(raw, 'df_6_Nominal_prueba_NIVEL_UNIFICADO_CON_FRACCIONES.csv')),
        'df_niveles':           cargar_csv(os.path.join(raw, 'df_niveles_unificados.csv')),
        'df_cursos':            cargar_csv(os.path.join(raw, 'df_Escuela_ID_CURSO_NORMALIZADO_list.csv')),
        'df_institucional':     cargar_csv(os.path.join(raw, 'df_datos_institucionales_Escuela_ID.csv')),
        'df_matricula':         cargar_csv(os.path.join(raw, 'df_nominal_cantidad_de_alumnos_por_escuela_y_curso.csv')),
        'df_nominal_inst':      cargar_csv(os.path.join(raw_nom, 'df_nominal_datos_institucionales.csv')),
        # Configuración desde config.py
        'dict_cantidad_preguntas':    cfg.DICT_CANTIDAD_PREGUNTAS,
        'dict_ejes_con_procesos':     cfg.DICT_EJES_CON_PROCESOS,
        'dict_pregunta_respuesta':    cfg.DICT_PREGUNTA_RESPUESTA,
    }
    return datos


def _generar_seccion(fn, *args, nombre='sección'):
    """Llama a una función de sección, capturando errores."""
    try:
        return fn(*args)
    except Exception as e:
        print(f'  Error al generar {nombre}: {e}')
        import traceback
        traceback.print_exc()
        return None


def _paginas_de(pdf_editor):
    """Extrae las páginas de un PDFEditor como lista."""
    if pdf_editor is None:
        return []
    try:
        stream = pdf_editor.save_to_stream()
        stream.seek(0)
        return list(PdfReader(stream).pages)
    except Exception as e:
        print(f'  Error al extraer páginas: {e}')
        return []


def generar_reporte_escuela(escuela_id, datos: dict, cfg, año_mes: str) -> bool:
    """Genera y guarda el PDF completo de una escuela."""
    print('=' * 70)
    print(f'Escuela {escuela_id}')

    inst = filtrar_datos_institucionales(datos['df_nominal_inst'], escuela_id)
    if inst is None:
        inst = filtrar_datos_institucionales(datos['df_institucional'], escuela_id)
    if inst is None:
        print(f'  Sin datos institucionales → saltando')
        return False

    nivel = obtener_nivel_escuela(datos['df_niveles'], escuela_id) or inst.get('Nivel_Unificado', 'Secundario')
    inst['Nivel_Unificado'] = nivel
    cursos = obtener_cursos_escuela(datos['df_cursos'], escuela_id)

    templates = cfg.TEMPLATES_PRIMARIO if nivel == 'Primario' else cfg.TEMPLATES_SECUNDARIO

    todas_las_paginas = []

    secciones = [
        (caratula,      (inst, templates['caratula']),                          'Carátula'),
        (hojas_1_2_3,   (inst, templates['hojas_1_2_3']),                       'Hojas 1-2-3'),
        (hoja_4,        (inst, datos, templates['hoja_4'], cursos),             'Hoja 4'),
        (hoja_5,        (inst, datos, templates['hoja_5'], cursos),             'Hoja 5'),
        (hoja_6,        (inst, datos, templates['hoja_6']),                     'Hoja 6'),
        (hoja_7_y_8,    (inst, datos, templates['hoja_7_y_8'], cursos),         'Hojas 7 y 8'),
        (hoja_9_nominal,(inst, datos, templates['hoja_9_nominal'], cursos),     'Hoja 9'),
    ]

    for fn, args, nombre in secciones:
        pdf_ed = _generar_seccion(fn, *args, nombre=nombre)
        paginas = _paginas_de(pdf_ed)
        if paginas:
            todas_las_paginas.extend(paginas)
            print(f'  {nombre}: {len(paginas)} página(s)')
        else:
            print(f'  {nombre}: sin páginas')

    if not todas_las_paginas:
        print(f'  Sin páginas generadas → saltando')
        return False

    writer = PdfWriter()
    for p in todas_las_paginas:
        writer.add_page(p)
    buf = BytesIO()
    writer.write(buf)
    buf.seek(0)

    nombre_archivo = f'{escuela_id}_{inst.get("Número", "000")}_Matemática_{año_mes}.pdf'
    ruta_salida = paths.proc_matematica_pdf(año_mes, nivel, nombre_archivo)
    with open(ruta_salida, 'wb') as f:
        f.write(buf.getvalue())

    tamaño_mb = os.path.getsize(ruta_salida) / (1024 * 1024)
    print(f'  Guardado: {ruta_salida} ({tamaño_mb:.2f} MB)')
    return True


def generar_reportes_pdf(cfg, año_mes: str) -> None:
    """Punto de entrada: genera PDFs para todas las escuelas."""
    print('Cargando datos...')
    datos = cargar_datos(cfg)
    escuelas = obtener_escuelas(datos['df_institucional'])
    print(f'{len(escuelas)} escuelas encontradas')

    exitosos, fallidos = 0, 0
    for escuela_id in escuelas:
        if generar_reporte_escuela(escuela_id, datos, cfg, año_mes):
            exitosos += 1
        else:
            fallidos += 1

    print('=' * 70)
    print(f'Completado: {exitosos} exitosos, {fallidos} fallidos de {len(escuelas)} escuelas')
