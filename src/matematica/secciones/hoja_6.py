"""
Hoja 6: Tabla de porcentaje de efectividad por curso.
"""
from io import BytesIO
from PIL import Image

from src.libs.pdf.editor import PDFEditor
from src.libs.visualizaciones.tabla_efectividad import generar_tabla_efectividad
from src.matematica.filtros import preparar_tabla_efectividad

ALTURA_PAGINA_MM = 297


def hoja_6(una_escuela: dict, datos: dict, template_path: str):
    """
    Parámetros:
    - datos: dict con df_2_efectividad
    """
    if not template_path:
        return None

    escuela_id = una_escuela['Escuela_ID']
    datos_tabla = preparar_tabla_efectividad(datos['df_2_efectividad'], escuela_id)
    if not datos_tabla:
        return None

    img_bytes = generar_tabla_efectividad(datos_tabla, return_bytes=True, altura_fila=0.3)
    if img_bytes is None:
        return None

    pdf = PDFEditor(template_path, una_escuela)

    img_tabla = Image.open(BytesIO(img_bytes))
    ancho_px, altura_px = img_tabla.size
    dpi = img_tabla.info.get('dpi', (72, 72))[1]
    altura_imagen_mm = (altura_px / dpi) * 25.4
    ancho_original_mm = (ancho_px / dpi) * 25.4
    ancho_deseado_mm = 80
    factor_escala = ancho_deseado_mm / ancho_original_mm
    altura_escalada_mm = altura_imagen_mm * factor_escala

    y_desde_superior = 105
    y_desde_abajo = ALTURA_PAGINA_MM - y_desde_superior - altura_escalada_mm

    pdf.insertar_imagen_bytes_segura(
        img_bytes, x_mm=65, y_mm=y_desde_abajo, page_number=0,
        ancho_mm=ancho_deseado_mm, ajustar_si_excede=True, debug=False,
    )

    print(f'Hoja 6 generada para escuela {escuela_id}')
    return pdf
