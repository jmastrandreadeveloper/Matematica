"""
Hoja 4: Tabla de participación (Participantes vs Matrícula por curso).
"""
from io import BytesIO
from PIL import Image

from src.libs.pdf.editor import PDFEditor
from src.libs.visualizaciones.tabla_participacion import generar_tabla_participacion
from src.matematica.filtros import preparar_tabla_participacion

ALTURA_PAGINA_MM = 297


def hoja_4(una_escuela: dict, datos: dict, template_path: str, cursos: list):
    """
    Parámetros:
    - una_escuela: dict con datos de la escuela
    - datos: dict con DataFrames cargados (df_0_alcance, df_matricula)
    - template_path: ruta al PDF template
    - cursos: lista de CURSO_NORMALIZADO de esta escuela
    """
    if not template_path:
        return None

    escuela_id = una_escuela['Escuela_ID']
    datos_tabla = preparar_tabla_participacion(
        datos['df_0_alcance'],
        datos['df_matricula'],
        escuela_id,
        cursos,
    )
    if not datos_tabla:
        return None

    img_bytes = generar_tabla_participacion(datos_tabla, return_bytes=True, altura_fila=0.3)
    if img_bytes is None:
        return None

    pdf = PDFEditor(template_path, una_escuela)

    img_tabla = Image.open(BytesIO(img_bytes))
    ancho_px, altura_px = img_tabla.size
    dpi = img_tabla.info.get('dpi', (72, 72))[1]
    altura_imagen_mm = (altura_px / dpi) * 25.4
    ancho_original_mm = (ancho_px / dpi) * 25.4

    ancho_deseado_mm = 143
    factor_escala = ancho_deseado_mm / ancho_original_mm
    altura_escalada_mm = altura_imagen_mm * factor_escala

    y_desde_superior = 81
    y_desde_abajo = ALTURA_PAGINA_MM - y_desde_superior - altura_escalada_mm

    pdf.insertar_imagen_bytes_segura(
        img_bytes, x_mm=33, y_mm=y_desde_abajo, page_number=0,
        ancho_mm=ancho_deseado_mm, ajustar_si_excede=True, debug=False,
    )

    print(f'Hoja 4 generada para escuela {escuela_id}')
    return pdf
