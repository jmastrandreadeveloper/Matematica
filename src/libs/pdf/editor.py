#from fpdf           import FPDF , HTMLMixin
from datetime       import date
#import os

# import config as cf
# import ClasePDF as cPDF
# import funcionesUtiles as fU

from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
import io
from PyPDF2 import PdfReader

from pathlib import Path

import io
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

from PyPDF2 import PdfMerger
from io import BytesIO

from io import BytesIO
from PyPDF2 import PdfWriter

import io
import tempfile
from PIL import Image
#import plotly.graph_objects as go
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader

import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import mm
from PIL import Image
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PdfReader, PdfWriter, PageObject
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, TextStringObject, DictionaryObject, NumberObject, ArrayObject, ByteStringObject
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject, TextStringObject, DictionaryObject, NumberObject, ArrayObject, ByteStringObject
from PyPDF2 import PdfMerger

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
import io

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PyPDF2 import PdfReader, PdfWriter
from reportlab.platypus import PageBreak

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak
from reportlab.lib.units import mm

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.units import mm

from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4, landscape

import os
import sys

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_CENTER
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2._page import PageObject
import io

from reportlab.lib.enums import TA_CENTER

from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from PyPDF2 import PdfReader
from PyPDF2.generic import DictionaryObject, ArrayObject, TextStringObject, NameObject, NumberObject
import io

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'  ))
sys.path.append(project_root)
# print('project_root : ', project_root)




#from config import fuentesREM  # Asegúrate de que config.py esté correctamente ubicado y accesible

# Ruta base donde se encuentran las fuentes
#carpeta_A_Fuentes = 'D:\PROYECTOS PYTHON\ProyectoBase_v2' + '\Fuentes'

# Diccionario con los nombres de las fuentes y sus archivos correspondientes
fuentesREM = {
    'REM-Black'             : project_root + '/FUENTES/REM/REM-Black.ttf',#'REM-Black.ttf',
    'REM-BlackItalic'       : project_root + '/FUENTES/REM/REM-BlackItalic.ttf',
    'REM-Bold'              : project_root + '/FUENTES/REM/REM-Bold.ttf',
    'REM-BoldItalic'        : project_root + '/FUENTES/REM/REM-BoldItalic.ttf',
    'REM-ExtraBold'         : project_root + '/FUENTES/REM/REM-ExtraBold.ttf',
    'REM-ExtraBoldItalic'   : project_root + '/FUENTES/REM/REM-ExtraBoldItalic.ttf',
    'REM-ExtraLight': project_root + '/FUENTES/REM/REM-ExtraLight.ttf',
    'REM-ExtraLightItalic': project_root + '/FUENTES/REM/REM-ExtraLightItalic.ttf',
    'REM-Italic': project_root + '/FUENTES/REM/REM-Italic.ttf',
    #'REM-Italic-VariableFont_wght': 'REM-Italic-VariableFont_wght.ttf',
    'REM-Light': project_root + '/FUENTES/REM/REM-Light.ttf',
    'REM-LightItalic': project_root + '/FUENTES/REM/REM-LightItalic.ttf',
    'REM-Medium': project_root + '/FUENTES/REM/REM-Medium.ttf',
    'REM-MediumItalic': project_root + '/FUENTES/REM/REM-MediumItalic.ttf',
    'REM-Regular': project_root + '/FUENTES/REM/REM-Regular.ttf',
    'REM-SemiBold': project_root + '/FUENTES/REM/REM-SemiBold.ttf',
    'REM-SemiBoldItalic': project_root + '/FUENTES/REM/REM-SemiBoldItalic.ttf',
    'REM-Thin': project_root + '/FUENTES/REM/REM-Thin.ttf',
    'REM-ThinItalic': project_root + '/FUENTES/REM/REM-ThinItalic.ttf'
    #'REM-VariableFont_wght': 'REM-VariableFont_wght.ttf',
}

# Register all fonts in fuentesREM
for key, value in fuentesREM.items():
    try:
        pdfmetrics.registerFont(TTFont(key, value))
        print(f"Font '{key}' registered successfully.")
    except Exception as e:
        print(f"Error registering font '{key}': {e}")


def mm_to_points(mm):
        return mm * 2.83465

class PDFEditor:
    # def __init__(self, pdf_path, escuela_data):
    #     self.pdf_path = pdf_path
    #     self.unaEscuela = escuela_data  # Objeto con la información de la escuela
    #     self.reader = PdfReader(pdf_path)
    #     self.writer = PdfWriter()
    #     self.fuentesREM = fuentesREM  # Diccionario de fuentes y sus rutas
    #     self.fonts = {}
    #     self.modified_pages = {}  # Dictionary to store modified pages
    #     #self.setup_fonts(self.fuentesREM.keys())  # Registra todas las fuentes al inicio

    def __init__(self, pdf_source, escuela_data):
        """
        Clase para editar y combinar PDFs.
        
        Args:
            pdf_source (str | io.BytesIO | PdfReader): Ruta del PDF, BytesIO o PdfReader.
            escuela_data (dict): Datos de la escuela.
        """
        self.unaEscuela = escuela_data  # Objeto con la información de la escuela
        self.writer = PdfWriter()
        self.modified_pages = {}  # Diccionario para almacenar páginas modificadas
        self.fonts = {}
        self.fuentesREM = fuentesREM  # Diccionario de fuentes y sus rutas

        # Convertir la fuente de datos en un PdfReader válido
        self.reader = self._initialize_reader(pdf_source)
        
        # Nuevo: almacenar enlaces pendientes
        self.pending_links = []  # ← Agregar esta línea
        self.named_destinations = {}  # ← Diccionario de destinos nombrados (alias)
        
    def add_pending_link(self, page_number, rect_mm, destination_page_offset, link_id=None, debug_draw=False, debug_color=(255, 0, 0)):
        """
        Registra un enlace para ser agregado después de la unión de PDFs.
        
        Parámetros:
        - page_number: página relativa dentro de este PDF (0, 1, 2...)
        - rect_mm: tupla (x, y, ancho, alto) en milímetros del área clicable
        - destination_page_offset: offset de página destino relativo al inicio del PDF final
        - link_id: identificador opcional para el enlace
        - debug_draw: si es True, dibuja un rectángulo para visualizar el área del enlace
        - debug_color: color RGB del rectángulo de debug (default: rojo)
        """
        self.pending_links.append({
            'page_number': page_number,
            'rect_mm': rect_mm,
            'destination_offset': destination_page_offset,
            'link_id': link_id
        })
        print(f"📌 Enlace pendiente registrado: Página {page_number} → Offset {destination_page_offset}")
        
        # Dibujar área de debug si está activado
        if debug_draw:
            self._draw_link_debug_area(page_number, rect_mm, debug_color)


    def _draw_link_debug_area(self, page_number, rect_mm, color=(255, 0, 0)):
        """
        Dibuja un rectángulo semi-transparente para visualizar el área de un enlace.
        
        Parámetros:
        - page_number: número de página
        - rect_mm: tupla (x, y, ancho, alto) en milímetros
        - color: color RGB del rectángulo (default: rojo)
        """
        from reportlab.pdfgen import canvas
        import io
        from PyPDF2 import PdfReader
        
        x_mm, y_mm, width_mm, height_mm = rect_mm
        
        # Convertir a puntos
        x = self.mm_to_points(x_mm)
        y = self.mm_to_points(y_mm)
        width = self.mm_to_points(width_mm)
        height = self.mm_to_points(height_mm)
        
        # Crear overlay con el rectángulo
        packet = io.BytesIO()
        
        # Obtener página para saber su tamaño
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]
        
        page_width = float(base_page.mediabox.width)
        page_height = float(base_page.mediabox.height)
        
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
        
        # Normalizar color
        r, g, b = color
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0
        
        # Dibujar rectángulo con borde grueso
        can.setStrokeColorRGB(r_norm, g_norm, b_norm)
        can.setLineWidth(2)
        can.setFillColorRGB(r_norm, g_norm, b_norm)
        can.setFillAlpha(0.1)  # Semi-transparente
        
        # Dibujar el rectángulo
        can.rect(x, y, width, height, fill=1, stroke=1)
        
        # Agregar etiqueta con el link_id si existe
        can.setFillColorRGB(1, 1, 1)  # Texto blanco
        can.setFont("Helvetica-Bold", 8)
        can.drawString(x + 2, y + height - 10, "🔗 LINK")
        
        can.save()
        packet.seek(0)
        
        # Fusionar con la página
        overlay_pdf = PdfReader(packet)
        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page
        
        print(f"  🎨 Área de debug dibujada en página {page_number}")


    def add_named_destination(self, alias, page_number, x_mm=0, y_mm=297):
        """
        Registra un destino nombrado (alias) para una página.
        
        Parámetros:
        - alias: nombre del destino (ej: "caratula", "curso_1", "resultados")
        - page_number: número de página dentro de este PDF (0, 1, 2...)
        - x_mm: coordenada X en mm (default: 0 = izquierda)
        - y_mm: coordenada Y en mm (default: 297 = arriba para A4)
        
        Ejemplo:
            pdf.add_named_destination('caratula', page_number=0)
            pdf.add_named_destination('curso_1', page_number=0, y_mm=200)
        """
        self.named_destinations[alias] = {
            'page': page_number,
            'x_mm': x_mm,
            'y_mm': y_mm
        }
        print(f"📍 Destino nombrado registrado: '{alias}' → Página {page_number}")


    def add_pending_link_to_alias(self, page_number, rect_mm, destination_alias, link_id=None, debug_draw=False, debug_color=(255, 0, 0)):
        """
        Registra un enlace a un destino nombrado (alias).
        
        Parámetros:
        - page_number: página donde está el enlace (0, 1, 2...)
        - rect_mm: área clicable (x, y, ancho, alto) en milímetros
        - destination_alias: alias del destino (ej: "caratula", "curso_1")
        - link_id: identificador opcional
        - debug_draw: si es True, dibuja el área del enlace
        - debug_color: color del área de debug RGB (default: rojo)
        
        Ejemplo:
            pdf.add_pending_link_to_alias(
                page_number=0,
                rect_mm=(25, 200, 50, 8),
                destination_alias='caratula',
                debug_draw=True
            )
        """
        self.pending_links.append({
            'page_number': page_number,
            'rect_mm': rect_mm,
            'destination_alias': destination_alias,
            'destination_offset': None,  # No se usa cuando hay alias
            'link_id': link_id
        })
        print(f"📌 Enlace a alias registrado: Página {page_number} → '{destination_alias}'")
        
        # Dibujar área de debug si está activado
        if debug_draw:
            self._draw_link_debug_area(page_number, rect_mm, debug_color)
            
    
    def add_external_link(self, page_number, rect_mm, url, link_id=None, debug_draw=False, debug_color=(0, 0, 255)):
        """
        Agrega un enlace externo (URL) a una página del PDF.
        
        Parámetros:
        -----------
        page_number : int
            Número de página donde agregar el enlace (0-indexed)
        
        rect_mm : tuple
            Tupla (x, y, ancho, alto) en milímetros del área clicable
            Ejemplo: (33, 200, 16, 10) = x=33mm, y=200mm, ancho=16mm, alto=10mm
        
        url : str
            URL completa del enlace externo
            Ejemplo: 'https://www.ejemplo.com', 'mailto:correo@ejemplo.com'
        
        link_id : str, opcional
            Identificador opcional para el enlace (para debugging)
            Default: None
        
        debug_draw : bool, opcional
            Si es True, dibuja un rectángulo para visualizar el área del enlace
            Default: False
        
        debug_color : tuple, opcional
            Color RGB del rectángulo de debug (0-255 para cada componente)
            Default: (0, 0, 255) = azul
        
        Retorna:
        --------
        self
            Retorna la instancia de PDFEditor para permitir encadenamiento de métodos
        
        Ejemplo de uso:
        ---------------
        >>> # Agregar enlace a un sitio web
        >>> pdf_editor.add_external_link(
        ...     page_number=0,
        ...     rect_mm=(50, 100, 40, 10),
        ...     url='https://www.google.com',
        ...     link_id='link_google',
        ...     debug_draw=False,
        ...     debug_color=(0, 255, 0)
        ... )
        
        >>> # Agregar enlace a email
        >>> pdf_editor.add_external_link(
        ...     page_number=0,
        ...     rect_mm=(50, 80, 40, 10),
        ...     url='mailto:contacto@escuela.edu.ar',
        ...     debug_draw=True
        ... )
        
        >>> # Sin debug
        >>> pdf_editor.add_external_link(
        ...     page_number=0,
        ...     rect_mm=(50, 60, 40, 10),
        ...     url='https://www.example.com/reporte.pdf'
        ... )
        
        Notas:
        ------
        - Los enlaces externos se aplican inmediatamente a la página
        - Soporta URLs web (http/https), emails (mailto:), archivos (file://)
        - El área clicable es invisible por defecto (usa debug_draw=True para verla)
        - Las coordenadas son en milímetros desde la esquina inferior izquierda
        """
        
        
        # Validar URL
        if not url or not isinstance(url, str):
            raise ValueError("URL debe ser un string válido")
        
        # Validar que la URL tenga un esquema válido
        valid_schemes = ['http://', 'https://', 'mailto:', 'file://', 'ftp://']
        if not any(url.lower().startswith(scheme) for scheme in valid_schemes):
            # Si no tiene esquema, asumir https://
            url = f'https://{url}'
            print(f"  ⚠️  URL sin esquema detectada, agregando https://: {url}")
        
        x_mm, y_mm, width_mm, height_mm = rect_mm
        
        # Convertir milímetros a puntos
        x = self.mm_to_points(x_mm)
        y = self.mm_to_points(y_mm)
        width = self.mm_to_points(width_mm)
        height = self.mm_to_points(height_mm)
        
        # Obtener la página
        if page_number in self.modified_pages:
            page = self.modified_pages[page_number]
        else:
            page = self.reader.pages[page_number]
            self.modified_pages[page_number] = page
        
        # Obtener dimensiones de la página
        page_width = float(page.mediabox.width)
        page_height = float(page.mediabox.height)
        
        # Crear anotación de enlace externo (URI)
        link_annotation = DictionaryObject()
        link_annotation.update({
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Link"),
            NameObject("/Rect"): ArrayObject([
                NumberObject(x),
                NumberObject(y),
                NumberObject(x + width),
                NumberObject(y + height)
            ]),
            NameObject("/Border"): ArrayObject([
                NumberObject(0),
                NumberObject(0),
                NumberObject(0)
            ]),  # Sin borde visible
            NameObject("/A"): DictionaryObject({
                NameObject("/Type"): NameObject("/Action"),
                NameObject("/S"): NameObject("/URI"),
                NameObject("/URI"): TextStringObject(url)
            })
        })
        
        # Agregar la anotación a la página
        if "/Annots" in page:
            page[NameObject("/Annots")].append(link_annotation)
        else:
            page[NameObject("/Annots")] = ArrayObject([link_annotation])
        
        # Log
        link_display = link_id if link_id else url
        print(f"🔗 Enlace externo agregado en página {page_number}: {link_display}")
        print(f"   URL: {url}")
        print(f"   Área: x={x_mm}mm, y={y_mm}mm, ancho={width_mm}mm, alto={height_mm}mm")
        
        # Dibujar área de debug si está activado
        if debug_draw:
            self._draw_link_debug_area_external(page_number, rect_mm, debug_color, url)
        
        return self
    
    
    def _draw_link_debug_area_external(self, page_number, rect_mm, color=(0, 0, 255), url=""):
        """
        Dibuja un rectángulo semi-transparente para visualizar el área de un enlace externo.
        
        Parámetros:
        -----------
        page_number : int
            Número de página
        
        rect_mm : tuple
            Tupla (x, y, ancho, alto) en milímetros
        
        color : tuple, opcional
            Color RGB del rectángulo (0-255)
            Default: (0, 0, 255) = azul
        
        url : str, opcional
            URL para mostrar en el debug
        """
        from reportlab.pdfgen import canvas
        import io
        from PyPDF2 import PdfReader
        
        x_mm, y_mm, width_mm, height_mm = rect_mm
        
        # Convertir a puntos
        x = self.mm_to_points(x_mm)
        y = self.mm_to_points(y_mm)
        width = self.mm_to_points(width_mm)
        height = self.mm_to_points(height_mm)
        
        # Crear overlay con el rectángulo
        packet = io.BytesIO()
        
        # Obtener página para saber su tamaño
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]
        
        page_width = float(base_page.mediabox.width)
        page_height = float(base_page.mediabox.height)
        
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
        
        # Normalizar color
        r, g, b = color
        r_norm = r / 255.0
        g_norm = g / 255.0
        b_norm = b / 255.0
        
        # Dibujar rectángulo con borde grueso
        can.setStrokeColorRGB(r_norm, g_norm, b_norm)
        can.setLineWidth(2)
        can.setFillColorRGB(r_norm, g_norm, b_norm)
        can.setFillAlpha(0.1)  # Semi-transparente
        
        # Dibujar el rectángulo
        can.rect(x, y, width, height, fill=1, stroke=1)
        
        # Agregar icono y etiqueta
        can.setFillColorRGB(1, 1, 1)  # Texto blanco
        can.setFont("Helvetica-Bold", 8)
        can.drawString(x + 2, y + height - 10, "🌐 LINK")
        
        # Agregar URL truncada si es muy larga
        if url:
            can.setFont("Helvetica", 6)
            url_display = url[:30] + "..." if len(url) > 30 else url
            can.drawString(x + 2, y + 2, url_display)
        
        can.save()
        packet.seek(0)
        
        # Fusionar con la página
        overlay_pdf = PdfReader(packet)
        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page
        
        print(f"  🎨 Área de debug dibujada en página {page_number} (color: RGB{color})")


    # ============================================================================
    # EJEMPLO DE USO COMPLETO
    # ============================================================================

    """
    # Ejemplo 1: Agregar enlace a sitio web con debug
    pdf_editor.add_external_link(
        page_number=0,
        rect_mm=(50, 200, 60, 10),
        url='https://www.educacion.gob.ar',
        link_id='link_ministerio',
        debug_draw=False,
        debug_color=(0, 255, 0)  # Verde
    )

    # Ejemplo 2: Agregar enlace a email
    pdf_editor.add_external_link(
        page_number=0,
        rect_mm=(50, 180, 60, 10),
        url='mailto:contacto@escuela.edu.ar',
        link_id='link_email',
        debug_draw=False,
        debug_color=(255, 0, 0)  # Rojo
    )

    # Ejemplo 3: Agregar múltiples enlaces sin debug
    enlaces = [
        {'url': 'https://www.google.com', 'rect': (10, 100, 40, 10)},
        {'url': 'https://www.wikipedia.org', 'rect': (10, 80, 40, 10)},
        {'url': 'https://www.github.com', 'rect': (10, 60, 40, 10)},
    ]

    for idx, enlace in enumerate(enlaces):
        pdf_editor.add_external_link(
            page_number=0,
            rect_mm=enlace['rect'],
            url=enlace['url'],
            link_id=f'link_{idx}'
        )

    # Ejemplo 4: URL sin esquema (se agrega automáticamente)
    pdf_editor.add_external_link(
        page_number=0,
        rect_mm=(50, 120, 60, 10),
        url='www.ejemplo.com',  # Se convertirá a https://www.ejemplo.com
        debug_draw=True
    )

    # Ejemplo 5: Encadenamiento de métodos
    pdf_editor.add_external_link(
        page_number=0,
        rect_mm=(10, 50, 40, 10),
        url='https://example.com'
    ).add_external_link(
        page_number=0,
        rect_mm=(60, 50, 40, 10),
        url='https://another.com'
    )
    """


    @classmethod
    def aplicar_enlaces_con_alias(cls, pdf_editor_final, lista_pdf_editors):
        """
        Aplica enlaces usando destinos nombrados (alias).
        Puede mezclar enlaces con alias y enlaces con offset.
        
        Parámetros:
        - pdf_editor_final: PDFEditor del PDF ya unido
        - lista_pdf_editors: lista de PDFEditor originales (en orden de unión)
        
        Ejemplo:
            pdf_final = PDF.PDFEditor(pdf_unido_bytes, una_escuela)
            PDF.PDFEditor.aplicar_enlaces_con_alias(pdf_final, lista_pdf_editors)
        """
        from PyPDF2.generic import DictionaryObject, ArrayObject, NumberObject, NameObject
        
        print("\n🔗 Aplicando enlaces (con alias y offsets)...")
        
        # Paso 1: Construir mapa de alias → página absoluta
        alias_map = {}
        page_offset = 0
        
        for idx, pdf in enumerate(lista_pdf_editors):
            num_pages = len(pdf.reader.pages)
            
            # Registrar destinos nombrados de este PDF
            if hasattr(pdf, 'named_destinations'):
                for alias, dest_info in pdf.named_destinations.items():
                    page_absolute = page_offset + dest_info['page']
                    alias_map[alias] = {
                        'page': page_absolute,
                        'x_mm': dest_info['x_mm'],
                        'y_mm': dest_info['y_mm']
                    }
                    print(f"  📍 '{alias}' → Página {page_absolute}")
            
            page_offset += num_pages
        
        print(f"  Total de destinos nombrados: {len(alias_map)}")
        
        # Paso 2: Aplicar enlaces
        page_offset = 0
        total_enlaces = 0
        total_pages = len(pdf_editor_final.reader.pages)
        
        for idx, pdf in enumerate(lista_pdf_editors):
            num_pages = len(pdf.reader.pages)
            
            if not hasattr(pdf, 'pending_links') or not pdf.pending_links:
                page_offset += num_pages
                continue
            
            print(f"  📌 PDF {idx} tiene {len(pdf.pending_links)} enlaces")
            
            for link in pdf.pending_links:
                page_absolute = page_offset + link['page_number']
                
                # Determinar destino
                if link.get('destination_alias'):
                    # Usar alias
                    alias = link['destination_alias']
                    if alias not in alias_map:
                        print(f"  ⚠️ Alias '{alias}' no encontrado")
                        continue
                    
                    dest_info = alias_map[alias]
                    destination_absolute = dest_info['page']
                    dest_x = pdf_editor_final.mm_to_points(dest_info['x_mm'])
                    dest_y = pdf_editor_final.mm_to_points(dest_info['y_mm'])
                elif link.get('destination_offset') is not None:
                    # Usar offset (compatibilidad)
                    destination_absolute = page_offset + link['destination_offset']
                    dest_x = 0
                    dest_y = pdf_editor_final.mm_to_points(297)
                else:
                    print(f"  ⚠️ Enlace sin destino válido")
                    continue
                
                # Validar páginas
                if page_absolute >= total_pages or destination_absolute >= total_pages:
                    print(f"  ⚠️ Páginas inválidas: {page_absolute} → {destination_absolute}")
                    continue
                
                # Obtener página
                page = pdf_editor_final.reader.pages[page_absolute]
                
                # Convertir coordenadas del enlace
                x_mm, y_mm, width_mm, height_mm = link['rect_mm']
                x = pdf_editor_final.mm_to_points(x_mm)
                y = pdf_editor_final.mm_to_points(y_mm)
                width = pdf_editor_final.mm_to_points(width_mm)
                height = pdf_editor_final.mm_to_points(height_mm)
                
                # Crear rectángulo
                link_rect = ArrayObject([
                    NumberObject(x),
                    NumberObject(y),
                    NumberObject(x + width),
                    NumberObject(y + height)
                ])
                
                # Obtener página destino
                dest_page = pdf_editor_final.reader.pages[destination_absolute]
                
                # Crear acción GoTo
                go_to_action = DictionaryObject()
                go_to_action.update({
                    NameObject("/S"): NameObject("/GoTo"),
                    NameObject("/D"): ArrayObject([
                        dest_page.indirect_reference,
                        NameObject("/XYZ"),
                        NumberObject(dest_x),
                        NumberObject(dest_y),
                        NumberObject(0)
                    ])
                })
                
                # Crear anotación
                link_annotation = DictionaryObject()
                link_annotation.update({
                    NameObject("/Type"): NameObject("/Annot"),
                    NameObject("/Subtype"): NameObject("/Link"),
                    NameObject("/Rect"): link_rect,
                    NameObject("/Border"): ArrayObject([NumberObject(0), NumberObject(0), NumberObject(0)]),
                    NameObject("/A"): go_to_action
                })
                
                # Agregar anotación
                if "/Annots" in page:
                    page["/Annots"].append(link_annotation)
                else:
                    page[NameObject("/Annots")] = ArrayObject([link_annotation])
                
                # Marcar como modificada
                pdf_editor_final.modified_pages[page_absolute] = page
                
                # Mensaje
                if link.get('destination_alias'):
                    dest_str = f"→ '{link['destination_alias']}' (Pág.{destination_absolute})"
                else:
                    dest_str = f"→ Pág.{destination_absolute}"
                
                total_enlaces += 1
                print(f"  ✅ Pág.{page_absolute} {dest_str}")
            
            page_offset += num_pages
        
        print(f"✅ Total de enlaces aplicados: {total_enlaces}\n")


    @classmethod
    def aplicar_enlaces_pendientes(cls, pdf_editor_final, lista_pdf_editors):
        """
        Aplica todos los enlaces pendientes después de unir los PDFs.
        
        Parámetros:
        - pdf_editor_final: PDFEditor del PDF ya unido
        - lista_pdf_editors: lista de PDFEditor originales (en orden de unión)
        """
        from PyPDF2.generic import DictionaryObject, ArrayObject, NumberObject, NameObject
        
        print("\n🔗 Aplicando enlaces pendientes...")
        
        # Calcular los offsets de página para cada PDF
        page_offset = 0
        pdf_offsets = []
        
        for pdf in lista_pdf_editors:
            pdf_offsets.append(page_offset)
            # Contar páginas del reader original
            num_pages = len(pdf.reader.pages)
            page_offset += num_pages
            print(f"  PDF offset: {pdf_offsets[-1]}, páginas: {num_pages}")
        
        # Verificar total de páginas en el PDF final
        total_pages_final = len(pdf_editor_final.reader.pages)
        print(f"  Total páginas en PDF final: {total_pages_final}")
        
        # Aplicar enlaces de cada PDF
        total_enlaces = 0
        for idx, pdf in enumerate(lista_pdf_editors):
            offset = pdf_offsets[idx]
            
            # Verificar si hay enlaces pendientes
            if not hasattr(pdf, 'pending_links') or not pdf.pending_links:
                continue
            
            for link in pdf.pending_links:
                # Calcular página absoluta en el PDF final
                page_absolute = offset + link['page_number']
                destination_absolute = offset + link['destination_offset']
                
                # Validar que las páginas existen
                if page_absolute >= total_pages_final:
                    print(f"  ⚠️ Página origen {page_absolute} no existe (total: {total_pages_final})")
                    continue
                
                if destination_absolute >= total_pages_final:
                    print(f"  ⚠️ Página destino {destination_absolute} no existe (total: {total_pages_final})")
                    continue
                
                # Obtener la página
                page = pdf_editor_final.reader.pages[page_absolute]
                
                # Convertir coordenadas de mm a puntos
                x_mm, y_mm, width_mm, height_mm = link['rect_mm']
                x = pdf_editor_final.mm_to_points(x_mm)
                y = pdf_editor_final.mm_to_points(y_mm)
                width = pdf_editor_final.mm_to_points(width_mm)
                height = pdf_editor_final.mm_to_points(height_mm)
                
                # Crear el rectángulo del enlace
                link_rect = ArrayObject([
                    NumberObject(x),
                    NumberObject(y),
                    NumberObject(x + width),
                    NumberObject(y + height)
                ])
                
                # Crear la acción de ir a página
                go_to_action = DictionaryObject()
                go_to_action.update({
                    NameObject("/S"): NameObject("/GoTo"),
                    NameObject("/D"): ArrayObject([
                        pdf_editor_final.reader.pages[destination_absolute].indirect_reference,
                        NameObject("/Fit")
                    ])
                })
                
                # Crear la anotación de enlace
                link_annotation = DictionaryObject()
                link_annotation.update({
                    NameObject("/Type"): NameObject("/Annot"),
                    NameObject("/Subtype"): NameObject("/Link"),
                    NameObject("/Rect"): link_rect,
                    NameObject("/Border"): ArrayObject([NumberObject(0), NumberObject(0), NumberObject(0)]),
                    NameObject("/A"): go_to_action
                })
                
                # Agregar la anotación a la página
                if "/Annots" in page:
                    page["/Annots"].append(link_annotation)
                else:
                    page[NameObject("/Annots")] = ArrayObject([link_annotation])
                
                # ✅ CRÍTICO: Marcar la página como modificada
                pdf_editor_final.modified_pages[page_absolute] = page
                
                total_enlaces += 1
                print(f"  ✅ Enlace aplicado: Pág.{page_absolute} → Pág.{destination_absolute} ({link.get('link_id', 'sin ID')})")
        
        print(f"✅ Total de enlaces aplicados: {total_enlaces}\n")
    
    @classmethod
    def leer_pdfs_en_directorio(cls, directorio, escuela_data):
        """
        Lee todos los archivos PDF en un directorio y los convierte en instancias de PDFEditor.

        Args:
            directorio (str): Ruta del directorio donde están los PDFs.
            escuela_data (dict): Datos de la escuela a pasar a PDFEditor.

        Returns:
            list: Lista de instancias de PDFEditor.
        """
        if not os.path.isdir(directorio):
            raise FileNotFoundError(f"❌ Error: El directorio '{directorio}' no existe.")

        pdf_editors = []
        for archivo in sorted(Path(directorio).glob("*.pdf")):
            try:
                pdf_editor = cls(str(archivo), escuela_data)  # Crea instancias de la clase PDFEditor
                pdf_editors.append(pdf_editor)
            except Exception as e:
                print(f"⚠️ Advertencia: No se pudo procesar '{archivo.name}': {e}")

        if not pdf_editors:
            print("⚠️ No se encontraron archivos PDF en el directorio.")

        return pdf_editors

    @classmethod
    def contar_paginas_pdf_editors(cls, pdf_editors):
        """
        Cuenta cuántas páginas tiene cada instancia de PDFEditor en la lista.

        Args:
            pdf_editors (list): Lista de objetos PDFEditor.

        Returns:
            dict: Diccionario con la cantidad de páginas de cada PDF.
        """
        if not pdf_editors:
            print("⚠️ La lista de PDFEditor está vacía.")
            return {}

        resultados = {}
        for pdf in pdf_editors:
            num_paginas = len(pdf.reader.pages)
            resultados[os.path.basename(pdf.pdf_path)] = num_paginas
            print(f"📄 {os.path.basename(pdf.pdf_path)}: {num_paginas} páginas.")

        return resultados

    @classmethod
    def contar_paginas_pdfs_en_directorio(cls, directorio, escuela_data):
        """
        Lee PDFs desde un directorio y cuenta las páginas de cada uno.

        Args:
            directorio (str): Ruta del directorio donde están los PDFs.
            escuela_data (dict): Datos de la escuela a pasar a PDFEditor.

        Returns:
            dict: Diccionario con la cantidad de páginas de cada PDF.
        """
        pdf_editors = cls.leer_pdfs_en_directorio(directorio, escuela_data)
        return cls.contar_paginas_pdf_editors(pdf_editors) if pdf_editors else {}
    
    def _initialize_reader(self, pdf_source):
        """Convierte pdf_source en un PdfReader válido."""
        if isinstance(pdf_source, str):  # Si es una ruta de archivo
            return PdfReader(pdf_source, strict=False)
        elif isinstance(pdf_source, io.BytesIO):  # Si es un BytesIO
            pdf_source.seek(0)  # Asegurar que el puntero está al inicio
            return PdfReader(pdf_source, strict=False)
        elif isinstance(pdf_source, PdfReader):  # Si ya es un PdfReader
            return pdf_source
        else:
            raise TypeError(f"❌ Error: Tipo de PDF no soportado ({type(pdf_source).__name__}).")

    
    # ============================================================================
    # OPCIÓN 3: Extraer TODAS las páginas a una lista plana primero
    # ============================================================================

    @classmethod
    def final_union_PDFs_flat(cls, pdf_editors):
        """
        Une PDFs extrayendo TODAS las páginas a una lista plana primero,
        luego las ensambla en un solo paso.
        
        Esto evita problemas de "uniones de uniones".
        """
        if not pdf_editors:
            raise ValueError("❌ Error: La lista de PDFEditor está vacía.")

        # Paso 1: Extraer TODAS las páginas a una lista
        todas_las_paginas = []
        total_paginas = 0
        
        print("\n📄 Extrayendo páginas de todos los PDFs:")
        
        for index, pdf in enumerate(pdf_editors):
            # Convertir a bytes
            if isinstance(pdf, PDFEditor):
                pdf_bytes = pdf.save_to_stream()
            elif isinstance(pdf, io.BytesIO):
                pdf_bytes = pdf
                pdf_bytes.seek(0)
            else:
                raise TypeError(f"❌ Tipo no soportado: {type(pdf)}")
            
            # Leer páginas
            try:
                pdf_reader = PdfReader(pdf_bytes, strict=False)
                num_pages = len(pdf_reader.pages)
                total_paginas += num_pages
                print(f"✅ PDF {index + 1}: {num_pages} páginas extraídas.")
                
                # Agregar cada página a la lista
                for page in pdf_reader.pages:
                    todas_las_paginas.append(page)
                    
            except Exception as e:
                print(f"❌ Error al leer PDF {index + 1}: {e}")
                continue
        
        # Paso 2: Ensamblar TODAS las páginas en un solo PDF
        print(f"\n📄 Ensamblando {len(todas_las_paginas)} páginas en el PDF final...")
        
        pdf_writer = PdfWriter()
        for i, page in enumerate(todas_las_paginas):
            try:
                pdf_writer.add_page(page)
            except Exception as e:
                print(f"⚠️ Error al agregar página {i+1}: {e}")
        
        # Guardar
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)

        print(f"✅ PDF final creado con {len(todas_las_paginas)} páginas")
        return pdf_output


    # ============================================================================
    # RECOMENDACIÓN: Probar en este orden
    # ============================================================================
    """
    1. Primero probar: final_union_PDFs_merger (OPCIÓN 2)
    → PdfMerger es más robusto para uniones complejas

    2. Si no funciona: final_union_PDFs_flat (OPCIÓN 3)
    → Aplanado completo garantiza eliminación de anidación

    3. Si aún falla: final_union_PDFs con flatten=True (OPCIÓN 1)
    → Versión mejorada del original

    IMPORTANTE: También verifica que NO estés haciendo uniones anidadas
    en tu código principal. Ejemplo:

    ❌ MAL:
    pdf_parte1 = final_union_PDFs([A, B, C])
    pdf_parte2 = final_union_PDFs([D, E, F])
    pdf_final = final_union_PDFs([pdf_parte1, pdf_parte2])  # Anidado!

    ✅ BIEN:
    pdf_final = final_union_PDFs([A, B, C, D, E, F])  # Todo de una vez
    """
    
    @staticmethod
    def fusionar_pdfs_desde_bytes(lista_pdf_bytes, escuela_data=None, nombre_operacion="PDFs", verbose=True):
        """
        Versión ULTRA-ROBUSTA: Trata cada entrada como un documento aislado
        evitando conflictos de recursos (imágenes solapadas).
        """
        from PyPDF2 import PdfReader, PdfWriter
        from io import BytesIO
        
        if not lista_pdf_bytes:
            raise ValueError("❌ Lista vacía")

        writer_final = PdfWriter()
        
        if verbose:
            print(f'\n🚀 Iniciando fusión robusta: {nombre_operacion}')

        for idx, pdf_data in enumerate(lista_pdf_bytes):
            # 1. Aseguramos que sea BytesIO
            if isinstance(pdf_data, BytesIO):
                stream = pdf_data
            else:
                # Si nos pasaron un PDFEditor, extraemos su stream 'limpio'
                stream = pdf_data.save_to_stream()
            
            stream.seek(0)
            
            # 2. Leemos el PDF de forma aislada
            # El parámetro strict=False ayuda a ignorar errores menores de sintaxis PDF
            reader = PdfReader(stream, strict=False)
            
            # 3. Importamos las páginas al writer final
            # add_page() en las versiones nuevas de PyPDF2 maneja mejor los recursos
            for page in reader.pages:
                writer_final.add_page(page)
                
            if verbose:
                print(f'  ✓ Documento {idx+1} integrado ({len(reader.pages)} pág/s)')

        # 4. Generamos el resultado final
        output = BytesIO()
        writer_final.write(output)
        output.seek(0)

        # 5. Retornamos la instancia de la clase para seguir trabajando
        return PDFEditor(output, escuela_data if escuela_data else {})


    # ============================================================================
    # DIAGNÓSTICO: Función para detectar PDFs ya unidos
    # ============================================================================

    def diagnosticar_pdf(pdf_bytes):
        """
        Analiza un PDF para detectar si es resultado de una unión previa.
        """
        from PyPDF2 import PdfReader
        
        pdf_bytes.seek(0)
        reader = PdfReader(pdf_bytes, strict=False)
        
        print("\n🔍 Diagnóstico del PDF:")
        print(f"  Páginas: {len(reader.pages)}")
        print(f"  Metadata: {reader.metadata}")
        
        # Verificar cada página
        for i, page in enumerate(reader.pages):
            try:
                # Intentar extraer contenido
                text = page.extract_text()
                annotations = page.get('/Annots', [])
                
                print(f"  Página {i+1}:")
                print(f"    - Texto extraíble: {'Sí' if text else 'No'}")
                print(f"    - Anotaciones: {len(annotations) if annotations else 0}")
                
            except Exception as e:
                print(f"  Página {i+1}: ⚠️ Error al analizar - {e}")
        
        pdf_bytes.seek(0)
    
    
    @classmethod
    def final_union_PDFs(cls, pdf_editors):
        """
        Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.

        Args:
            pdf_editors (list): Lista de instancias de PDFEditor.

        Returns:
            io.BytesIO: PDF combinado en memoria.
        """
        if not pdf_editors:
            raise ValueError("❌ Error: La lista de PDFEditor está vacía.")

        pdf_writer = PdfWriter()
        total_paginas = 0

        print("\n📄 Reporte de PDFs a unir:")
        for index, pdf in enumerate(pdf_editors):
            pdf_bytes = pdf.save_to_stream() 
            pdf_reader = PdfReader(pdf_bytes, strict=False)  # Leer el PDF convertido

            num_pages = len(pdf_reader.pages)
            total_paginas += num_pages
            print(f"✅ PDF {index + 1}: {num_pages} páginas.")

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)  # Agregar todas las páginas

        # Guardar el PDF combinado en memoria
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)  # Reiniciar el puntero al inicio

        print(f"\n📑 Total de páginas en el PDF final: {total_paginas}")
        return pdf_output
    
    @classmethod
    def final_union_PDFs_2(cls, pdf_editors):
        """
        Une múltiples PDFs en memoria, evitando agregar páginas vacías o corruptas.
        
        Args:
            pdf_editors (list): Lista de instancias de PDFEditor.
        
        Returns:
            io.BytesIO: PDF combinado en memoria.
        """
        if not pdf_editors:
            raise ValueError("❌ Error: La lista de PDFEditor está vacía.")

        pdf_writer = PdfWriter()
        total_paginas = 0
        paginas_agregadas = 0

        print("\n📄 Reporte de PDFs a unir:")
        for index, pdf in enumerate(pdf_editors):
            pdf_bytes = pdf.to_bytesio()
            pdf_reader = PdfReader(pdf_bytes, strict=False)
            num_pages = len(pdf_reader.pages)
            total_paginas += num_pages
            print(f"✅ PDF {index + 1}: {num_pages} páginas.")

            for i, page in enumerate(pdf_reader.pages):
                try:
                    text = page.extract_text()
                    if text and text.strip():  # Página con texto
                        pdf_writer.add_page(page)
                        paginas_agregadas += 1
                    else:
                        print(f"⚠️ Página {i+1} del PDF {index+1} está vacía o no tiene texto legible.")
                except Exception as e:
                    print(f"❌ Error al procesar página {i+1} del PDF {index+1}: {e}")

        # Guardar en memoria
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)

        print(f"\n📑 Total de páginas originales: {total_paginas}")
        print(f"📌 Total de páginas agregadas al PDF final: {paginas_agregadas}")
        return pdf_output
    
    
    @staticmethod
    def final_union_PDFs_4(lista_de_rutas, ignorar_errores=False):
        """
        Une múltiples archivos PDF y devuelve el contenido combinado como un objeto en memoria.

        Args:
            lista_de_rutas (list): Lista de rutas de archivos PDF.
            ignorar_errores (bool): Si True, ignora errores en archivos corruptos o no válidos.

        Returns:
            io.BytesIO: Archivo PDF combinado en memoria.
        """
        merger = PdfMerger()
        archivos_agregados = 0

        for ruta in lista_de_rutas:
            if not os.path.isfile(ruta):
                print(f"⚠️ Archivo no encontrado: {ruta}")
                if not ignorar_errores:
                    raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
                continue

            if not ruta.lower().endswith('.pdf'):
                print(f"⚠️ No es un archivo PDF: {ruta}")
                if not ignorar_errores:
                    raise ValueError(f"Archivo no es un PDF: {ruta}")
                continue

            try:
                merger.append(ruta)
                archivos_agregados += 1
            except Exception as e:
                print(f"⚠️ Error al agregar {ruta}: {e}")
                if not ignorar_errores:
                    raise e

        if archivos_agregados == 0:
            raise ValueError("No se agregó ningún PDF. Verifica las rutas o los archivos.")

        # Guardar resultado en memoria
        output_stream = io.BytesIO()
        merger.write(output_stream)
        merger.close()
        output_stream.seek(0)
        print(f"✅ PDF combinado en memoria. Total archivos: {archivos_agregados}")
        return output_stream
    
    
    
    
    @classmethod
    def final_union_PDFs_3(cls, pdf_editors):
        """
        Une múltiples PDFs en memoria, filtrando páginas vacías o con errores de codificación.
        """
        if not pdf_editors:
            raise ValueError("❌ La lista de PDFEditor está vacía.")

        writer = PdfWriter()
        total_origen = 0
        total_agregadas = 0

        print("\n📄 Analizando y uniendo PDFs:")
        for idx, editor in enumerate(pdf_editors):
            pdf_io = editor.to_bytesio()
            pdf_io.seek(0)

            try:
                reader = PdfReader(pdf_io, strict=False)
            except Exception as e:
                print(f"❌ Error al leer PDF {idx+1}: {e}")
                continue

            print(f"🔹 PDF {idx+1}: {len(reader.pages)} páginas detectadas.")
            total_origen += len(reader.pages)

            for i, page in enumerate(reader.pages):
                try:
                    texto = page.extract_text()
                    if texto and texto.strip():  # tiene texto visible
                        writer.add_page(page)
                        total_agregadas += 1
                    else:
                        # página vacía o sin texto visible
                        print(f"⚠️ Página {i+1} del PDF {idx+1} omitida (vacía o ilegible).")
                except Exception as e:
                    print(f"❌ Error al procesar página {i+1} del PDF {idx+1}: {e}")

        # Guardar el PDF combinado
        output_io = io.BytesIO()
        writer.write(output_io)
        output_io.seek(0)

        print(f"\n📑 Total de páginas originales: {total_origen}")
        print(f"✅ Páginas agregadas al PDF final: {total_agregadas}")
        return output_io
    
    
    @classmethod
    def unir_pdfs_memoria(cls, pdf_list):
        """
        Une una lista de PDFs que están en memoria y devuelve un objeto BytesIO con el PDF combinado.

        Args:
            pdf_list (list): Lista de objetos PDFEditor o BytesIO.

        Returns:
            BytesIO: PDF combinado en memoria.
        """
        if not isinstance(pdf_list, list):
            raise TypeError("❌ Error: Se esperaba una lista de PDFs en memoria.")

        pdf_writer = PdfWriter()
        total_pages = 0

        print("\n📄 Reporte de PDFs a unir:")

        for index, pdf in enumerate(pdf_list):
            # Convertir a BytesIO si es un PDFEditor
            if isinstance(pdf, PDFEditor):
                pdf = pdf.to_bytesio()

            if not isinstance(pdf, io.BytesIO):
                raise TypeError(f"❌ Error: El elemento en la posición {index} no es un BytesIO válido.")

            pdf.seek(0)
            pdf_reader = PdfReader(pdf, strict=False)

            num_pages = len(pdf_reader.pages)
            total_pages += num_pages
            print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

            for page_num in range(num_pages):
                pdf_writer.add_page(pdf_reader.pages[page_num])

        # Guardar el PDF combinado en memoria
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)

        print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
        return pdf_output
    
    @classmethod
    def verificar_pdfs_en_memoria(self, pdf_editors):
        """
        Verifica la cantidad de páginas en cada PDF almacenado en memoria.

        Args:
            pdf_editors (list): Lista de instancias de PDFEditor.

        Returns:
            dict: Un diccionario con información sobre cada PDF en memoria.
        """
        report = {}

        for index, editor in enumerate(pdf_editors):
            if not isinstance(editor, PDFEditor):
                print(f"❌ Error: El elemento en la posición {index} no es un PDFEditor.")
                continue

            pdf_bytes = editor.to_bytesio()
            size_in_bytes = pdf_bytes.getbuffer().nbytes

            # Reiniciar el puntero antes de leerlo
            pdf_bytes.seek(0)
            pdf_reader_memoria = PdfReader(pdf_bytes, strict=False)
            num_pages = len(pdf_reader_memoria.pages)

            print(f"📄 PDF {index + 1}: {num_pages} páginas, {size_in_bytes} bytes.")

            report[f"PDF_{index + 1}"] = {
                "num_paginas": num_pages,
                "tamaño_bytes": size_in_bytes
            }

        return report
    
    
    # def to_bytesio(self):
    #     """Convierte el PDF actual en un objeto BytesIO."""
    #     pdf_bytes = io.BytesIO()
    #     self.writer.write(pdf_bytes)
    #     pdf_bytes.seek(0)
    #     return pdf_bytes
    def to_bytesio(self):
        """
        Convierte el PDF actual en un objeto BytesIO.
        ✅ CORREGIDO: Incluye páginas modificadas de self.modified_pages
        """
        pdf_bytes = io.BytesIO()
        pdf_writer = PdfWriter()

        # ✅ CORREGIDO: Incluir páginas modificadas
        for i in range(len(self.reader.pages)):
            if i in self.modified_pages:
                pdf_writer.add_page(self.modified_pages[i])  # ← Página modificada
            else:
                pdf_writer.add_page(self.reader.pages[i])    # ← Página original

        pdf_writer.write(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes

    @staticmethod
    def convert_to_pdfeditor(pdf, escuela_data):
        """Convierte cualquier objeto PDF a PDFEditor."""
        if isinstance(pdf, PDFEditor):
            return pdf
        elif isinstance(pdf, (io.BytesIO, PdfReader, str)):
            return PDFEditor(pdf, escuela_data)
        else:
            raise TypeError(f"❌ Error: No se puede convertir {type(pdf).__name__} a PDFEditor.")
        
    def convert_to_bytesio(self, pdf):
        """
        Convierte un objeto PDFEditor, PdfReader o BytesIO en un objeto BytesIO válido.

        Args:
            pdf (PDFEditor | PdfReader | BytesIO): Objeto de entrada.

        Returns:
            BytesIO: Representación del PDF en memoria.
        """
        if isinstance(pdf, io.BytesIO):
            return pdf  # Ya es un objeto BytesIO, no necesita conversión

        elif isinstance(pdf, PDFEditor):
            return self.pdf_editor_to_bytes(pdf)  # Convierte PDFEditor a BytesIO

        elif isinstance(pdf, PdfReader):
            pdf_writer = PdfWriter()
            for page in pdf.pages:
                pdf_writer.add_page(page)

            pdf_output = io.BytesIO()
            pdf_writer.write(pdf_output)
            pdf_output.seek(0)
            return pdf_output  # Devuelve el contenido como BytesIO

        else:
            raise TypeError(f"❌ Error: Tipo de archivo no compatible ({type(pdf)})")
        
    
    def pdf_editor_to_bytes(self, pdf_editor):
        """
        Convierte un objeto PDFEditor en un objeto BytesIO.

        Args:
            pdf_editor (PDFEditor): Instancia de PDFEditor.

        Returns:
            BytesIO: Representación del PDF en memoria.
        """
        if not isinstance(pdf_editor, PDFEditor):
            raise TypeError(f"❌ Error: Se esperaba un objeto PDFEditor, pero se recibió {type(pdf_editor)}.")

        pdf_output = io.BytesIO()
        
        # Guardar el contenido del PDFEditor en el PdfWriter
        for page_num in range(len(pdf_editor.reader.pages)):
            pdf_editor.writer.add_page(pdf_editor.reader.pages[page_num])

        pdf_editor.writer.write(pdf_output)  # Escribir en memoria
        pdf_output.seek(0)  # Reiniciar puntero

        return pdf_output
    
    
    def merge_pdfs_in_memory_NONO(self, pdf_list, additional_pdfs=None):
        """
        Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
        Asegura que se extraigan todas las páginas correctamente de cada PDF.

        Args:
            pdf_list (list): Lista de objetos PDFEditor, BytesIO o PdfReader.
            additional_pdfs (list, optional): PDFs adicionales.

        Returns:
            BytesIO: PDF combinado en memoria.
        """
        if not isinstance(pdf_list, list):  # Asegurar que sea una lista
            pdf_list = [pdf_list]

        pdf_writer = PdfWriter()
        total_pages = 0  # Contador total de páginas

        print("\n📄 Reporte de PDFs a unir:")

        # Procesar la lista de PDFs principal
        for index, pdf in enumerate(pdf_list):
            pdf_bytes = self.convert_to_bytesio(pdf)  # Convertir cada entrada a BytesIO

            if isinstance(pdf_bytes, io.BytesIO):
                pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
                pdf_reader = PdfReader(pdf_bytes, strict=False)

                num_pages = len(pdf_reader.pages)
                total_pages += num_pages
                print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

                # Agregar todas las páginas al PdfWriter
                for page_num in range(num_pages):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
            else:
                print(f"❌ Error: El PDF {index + 1} no devolvió un objeto BytesIO válido.")

        # Procesar PDFs adicionales si existen
        if additional_pdfs:
            for index, pdf in enumerate(additional_pdfs):
                pdf_bytes = self.convert_to_bytesio(pdf)

                if isinstance(pdf_bytes, io.BytesIO):
                    pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
                    pdf_reader = PdfReader(pdf_bytes, strict=False)

                    num_pages = len(pdf_reader.pages)
                    total_pages += num_pages
                    print(f"✅ PDF adicional {index + 1} tiene {num_pages} páginas.")

                    for page_num in range(num_pages):
                        pdf_writer.add_page(pdf_reader.pages[page_num])
                else:
                    print(f"❌ Error: El PDF adicional {index + 1} no devolvió un objeto BytesIO válido.")

        # Guardar el PDF combinado en memoria
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)  # Reiniciar el puntero al inicio

        print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
        return pdf_output
    
    @staticmethod
    def contar_paginas_pdf_editors(pdf_editors):
        """
        Cuenta cuántas páginas tiene cada objeto PDFEditor en una lista.

        Args:
            pdf_editors (list): Lista de instancias de PDFEditor.

        Returns:
            dict: Diccionario con la cantidad de páginas de cada PDFEditor.
        """
        if not isinstance(pdf_editors, list):
            raise TypeError("❌ Error: Se esperaba una lista de objetos PDFEditor.")

        paginas_por_pdf = {}

        for index, pdf_editor in enumerate(pdf_editors):
            if not isinstance(pdf_editor, PDFEditor):
                raise TypeError(f"❌ Error: El elemento en la posición {index} no es un objeto PDFEditor.")
            
            num_paginas = len(pdf_editor.reader.pages)
            paginas_por_pdf[f"PDF_{index+1}"] = num_paginas
            print(f"📄 PDF {index+1} tiene {num_paginas} páginas.")

        return paginas_por_pdf
    
    
    def merge_pdfs_in_memory(self, pdf_list, additional_pdfs=None):
        """
        Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
        Todos los PDFs se convierten primero a PDFEditor.

        Args:
            pdf_list (list): Lista de PDFs en PDFEditor, BytesIO, PdfReader o rutas de archivo.
            additional_pdfs (list, optional): PDFs adicionales.

        Returns:
            BytesIO: PDF combinado en memoria.
        """
        if not isinstance(pdf_list, list):  # Asegurar que sea una lista
            pdf_list = [pdf_list]

        pdf_writer = PdfWriter()
        total_pages = 0  # Contador total de páginas

        # Convertir todos los PDFs a PDFEditor
        pdf_editor_list = [self.convert_to_pdfeditor(pdf, self.unaEscuela) for pdf in pdf_list]

        # Agregar páginas de los PDFs principales
        #print("\n📄 Reporte de PDFs a unir:")
        for index, pdf_editor in enumerate(pdf_editor_list):
            num_pages = len(pdf_editor.reader.pages)
            total_pages += num_pages
            #print(f"✅ PDF {index + 1} tiene {num_pages} páginas. y es del tipo : {type(pdf_editor)}")

            for page_num in range(num_pages):
                pdf_writer.add_page(pdf_editor.reader.pages[page_num])  # Agregar todas las páginas

        # Agregar PDFs adicionales si existen
        if additional_pdfs:
            additional_editor_list = [self.convert_to_pdfeditor(pdf, self.unaEscuela) for pdf in additional_pdfs]

            for index, pdf_editor in enumerate(additional_editor_list):
                num_pages = len(pdf_editor.reader.pages)
                total_pages += num_pages
                #print(f"✅ PDF adicional {index + 1} tiene {num_pages} páginas.")

                for page_num in range(num_pages):
                    pdf_writer.add_page(pdf_editor.reader.pages[page_num])  # Agregar todas las páginas

        # Guardar el PDF combinado en memoria
        pdf_output = io.BytesIO()
        pdf_writer.write(pdf_output)
        pdf_output.seek(0)  # Reiniciar el puntero al inicio

        #print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
        return pdf_output



    def mm_to_points(self, mm):
        return (mm / 25.4) * 72
    
    def poner_tabla_en_la_hoja(self,tabla):
        self.tabla = tabla
        return
    
    import io
    from PyPDF2 import PdfReader, PdfWriter

    
    @staticmethod
    def eliminar_pdfs_en_directorio(directorio):
        """
        Elimina todos los archivos PDF en el directorio especificado.

        Args:
            directorio (str): Ruta del directorio donde se eliminarán los PDFs.

        Returns:
            dict: Un diccionario con el estado de los archivos eliminados.
        """
        if not os.path.exists(directorio):
            print(f"❌ Error: El directorio '{directorio}' no existe.")
            return {"status": "error", "mensaje": "Directorio no encontrado"}

        archivos_pdf = [f for f in os.listdir(directorio) if f.lower().endswith(".pdf")]

        if not archivos_pdf:
            print("ℹ️ No hay archivos PDF en el directorio.")
            return {"status": "ok", "mensaje": "No se encontraron archivos PDF"}

        archivos_eliminados = []

        for archivo in archivos_pdf:
            ruta_completa = os.path.join(directorio, archivo)
            try:
                os.remove(ruta_completa)
                print(f"🗑️ Archivo eliminado: {archivo}")
                archivos_eliminados.append(archivo)
            except Exception as e:
                print(f"⚠️ No se pudo eliminar {archivo}: {e}")

        return {"status": "ok", "archivos_eliminados": archivos_eliminados}
    
    def pdf_editor_to_bytes(self, pdf_editor):
        """Convierte un PDFEditor en un objeto BytesIO."""
        pdf_writer = PdfWriter()

        num_pages = len(pdf_editor.reader.pages)
        print(f"✅ PDF procesado ({num_pages} páginas).")

        for i in range(num_pages):
            if i in pdf_editor.modified_pages:
                pdf_writer.add_page(pdf_editor.modified_pages[i])  # Página modificada
            else:
                pdf_writer.add_page(pdf_editor.reader.pages[i])  # Página original

        pdf_bytes = io.BytesIO()
        pdf_writer.write(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes

    # # este funciona bien pero no se si es el mejor
    # def merge_pdfs_in_memory(self, pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
    #     Muestra un reporte con la cantidad de páginas en cada PDF y el total final.

    #     Args:
    #         pdf_list (PDFEditor | list): Un solo objeto PDFEditor o una lista de PDFEditor/BytesIO.
    #         additional_pdfs (list, optional): Lista de BytesIO o PdfReader con PDFs adicionales.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     if not isinstance(pdf_list, list):  # Asegurar que sea una lista
    #         pdf_list = [pdf_list]

    #     pdf_writer = PdfWriter()
    #     total_pages = 0  # Contador total de páginas

    #     # Convertir PDFEditor a BytesIO si es necesario
    #     pdf_bytes_list = []
    #     for index, pdf in enumerate(pdf_list):
    #         if isinstance(pdf, PDFEditor):
    #             pdf_bytes = self.pdf_editor_to_bytes(pdf)  # Llamada corregida usando self
    #             pdf_bytes_list.append(pdf_bytes)
    #         elif isinstance(pdf, io.BytesIO):
    #             pdf_bytes_list.append(pdf)
    #         else:
    #             raise TypeError(f"❌ Error: El elemento en la posición {index} no es un objeto BytesIO válido.")

    #     # Agregar páginas de los PDFs principales
    #     print("\n📄 Reporte de PDFs a unir:")
    #     for index, pdf_bytes in enumerate(pdf_bytes_list):
    #         pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
    #         pdf_reader = PdfReader(pdf_bytes, strict=False)  # Leer el PDF
            
    #         num_pages = len(pdf_reader.pages)
    #         total_pages += num_pages
    #         print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

    #         for page_num in range(num_pages):
    #             pdf_writer.add_page(pdf_reader.pages[page_num])  # Agregar todas las páginas

    #     # Agregar PDFs adicionales si existen
    #     if additional_pdfs:
    #         for index, pdf_source in enumerate(additional_pdfs):
    #             if isinstance(pdf_source, io.BytesIO):
    #                 pdf_source.seek(0)  # Asegurar que el puntero está al inicio
    #                 additional_reader = PdfReader(pdf_source, strict=False)
    #                 pdf_type = "BytesIO"
    #             elif isinstance(pdf_source, PdfReader):
    #                 additional_reader = pdf_source
    #                 pdf_type = "PdfReader"
    #             else:
    #                 raise ValueError(f"❌ Error: El PDF adicional en la posición {index} no es válido.")

    #             num_pages = len(additional_reader.pages)
    #             total_pages += num_pages
    #             print(f"✅ PDF adicional {index + 1} ({pdf_type}) tiene {num_pages} páginas.")

    #             for page_num in range(num_pages):
    #                 pdf_writer.add_page(additional_reader.pages[page_num])  # Agregar todas las páginas

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
    #     return pdf_output
    
    
    # def merge_pdfs_in_memory_2(self, pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
    #     Muestra un reporte con la cantidad de páginas en cada PDF y el total final.

    #     Args:
    #         pdf_list (PDFEditor | list): Un solo objeto PDFEditor o una lista de PDFEditor/BytesIO.
    #         additional_pdfs (list, optional): Lista de BytesIO o PdfReader con PDFs adicionales.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     if not isinstance(pdf_list, list):  # Asegurar que sea una lista
    #         pdf_list = [pdf_list]

    #     # Validar que todos los elementos de pdf_list sean del tipo esperado
    #     invalid_elements = [index for index, pdf in enumerate(pdf_list) if not isinstance(pdf, (PDFEditor, io.BytesIO))]
        
    #     if invalid_elements:
    #         raise TypeError(f"❌ Error: Los siguientes índices contienen elementos no válidos: {invalid_elements}")

    #     pdf_writer = PdfWriter()
    #     total_pages = 0  # Contador total de páginas

    #     # Convertir PDFEditor a BytesIO si es necesario
    #     pdf_bytes_list = []
    #     for index, pdf in enumerate(pdf_list):
    #         if isinstance(pdf, PDFEditor):
    #             pdf_bytes = self.pdf_editor_to_bytes(pdf)  # Convertir a BytesIO
    #         else:
    #             pdf_bytes = pdf  # Ya es BytesIO
    #         pdf_bytes_list.append(pdf_bytes)

    #     # Agregar páginas de los PDFs principales
    #     print("\n📄 Reporte de PDFs a unir:")
    #     for index, pdf_bytes in enumerate(pdf_bytes_list):
    #         pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
    #         pdf_reader = PdfReader(pdf_bytes, strict=False)  # Leer el PDF
            
    #         num_pages = len(pdf_reader.pages)
    #         total_pages += num_pages
    #         print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

    #         for page_num in range(num_pages):
    #             pdf_writer.add_page(pdf_reader.pages[page_num])  # Agregar todas las páginas

    #     # Agregar PDFs adicionales si existen
    #     if additional_pdfs:
    #         for index, pdf_source in enumerate(additional_pdfs):
    #             if isinstance(pdf_source, io.BytesIO):
    #                 pdf_source.seek(0)  # Asegurar que el puntero está al inicio
    #                 additional_reader = PdfReader(pdf_source, strict=False)
    #                 pdf_type = "BytesIO"
    #             elif isinstance(pdf_source, PdfReader):
    #                 additional_reader = pdf_source
    #                 pdf_type = "PdfReader"
    #             else:
    #                 raise ValueError(f"❌ Error: El PDF adicional en la posición {index} no es válido.")

    #             num_pages = len(additional_reader.pages)
    #             total_pages += num_pages
    #             print(f"✅ PDF adicional {index + 1} ({pdf_type}) tiene {num_pages} páginas.")

    #             for page_num in range(num_pages):
    #                 pdf_writer.add_page(additional_reader.pages[page_num])  # Agregar todas las páginas

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
    #     return pdf_output

    
    
    
    # def merge_pdfs_in_memory_3(self, pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
    #     Muestra un reporte con la cantidad de páginas en cada PDF y el total final.

    #     Args:
    #         pdf_list (list): Lista de PDFEditor o BytesIO.
    #         additional_pdfs (list, optional): Lista de BytesIO o PdfReader con PDFs adicionales.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     for unPDF in pdf_list:
    #         print('unPDF : ', unPDF)
    #         if not isinstance(unPDF, (PDFEditor, io.BytesIO)):
    #             raise TypeError("❌ Error: Todos los elementos en pdf_list deben ser PDFEditor o BytesIO.")
            
    #     if not isinstance(pdf_list, list):  # Asegurar que sea una lista
    #         pdf_list = [pdf_list]

    #     pdf_writer = PdfWriter()
    #     total_pages = 0  # Contador total de páginas

    #     # Convertir todo a BytesIO si es necesario
    #     pdf_bytes_list = []
    #     for index, pdf in enumerate(pdf_list):
    #         if isinstance(pdf, PDFEditor):
    #             pdf_bytes = self.pdf_editor_to_bytes(pdf)  # Convertir a BytesIO
    #             pdf_bytes_list.append(pdf_bytes)
    #             print(f"🔄 Convertido PDFEditor {index + 1} a BytesIO.")
    #         elif isinstance(pdf, io.BytesIO):
    #             pdf_bytes_list.append(pdf)
    #         else:
    #             raise TypeError(f"❌ Error: El elemento en la posición {index} no es un objeto PDFEditor o BytesIO válido.")

    #     # Agregar páginas de los PDFs principales
    #     print("\n📄 Reporte de PDFs a unir:")
    #     for index, pdf_bytes in enumerate(pdf_bytes_list):
    #         pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
    #         pdf_reader = PdfReader(pdf_bytes, strict=False)  # Leer el PDF
            
    #         num_pages = len(pdf_reader.pages)
    #         total_pages += num_pages
    #         print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

    #         for page_num in range(num_pages):
    #             pdf_writer.add_page(pdf_reader.pages[page_num])  # Agregar todas las páginas

    #     # Agregar PDFs adicionales si existen
    #     if additional_pdfs:
    #         for index, pdf_source in enumerate(additional_pdfs):
    #             if isinstance(pdf_source, io.BytesIO):
    #                 pdf_source.seek(0)  # Asegurar que el puntero está al inicio
    #                 additional_reader = PdfReader(pdf_source, strict=False)
    #                 pdf_type = "BytesIO"
    #             elif isinstance(pdf_source, PdfReader):
    #                 additional_reader = pdf_source
    #                 pdf_type = "PdfReader"
    #             else:
    #                 raise ValueError(f"❌ Error: El PDF adicional en la posición {index} no es válido.")

    #             num_pages = len(additional_reader.pages)
    #             total_pages += num_pages
    #             print(f"✅ PDF adicional {index + 1} ({pdf_type}) tiene {num_pages} páginas.")

    #             for page_num in range(num_pages):
    #                 pdf_writer.add_page(additional_reader.pages[page_num])  # Agregar todas las páginas

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
    #     return pdf_output

    def pdf_editor_to_bytes(self, pdf):
        """Convierte un objeto PDFEditor a BytesIO."""
        pdf_bytes = io.BytesIO()
        pdf.writer.write(pdf_bytes)
        pdf_bytes.seek(0)
        return pdf_bytes

    def pdf_to_bytesio(self, pdf):
        """Convierte cualquier tipo de PDF a un objeto io.BytesIO."""
        if isinstance(pdf, PDFEditor):
            return self.pdf_editor_to_bytes(pdf)  # Convertir PDFEditor a BytesIO
        elif isinstance(pdf, io.BytesIO):
            pdf.seek(0)  # Asegurar que el puntero está al inicio
            return pdf
        elif isinstance(pdf, PdfReader):
            pdf_bytes = io.BytesIO()
            writer = PdfWriter()
            for page in pdf.pages:
                writer.add_page(page)
            writer.write(pdf_bytes)
            pdf_bytes.seek(0)
            return pdf_bytes
        else:
            raise TypeError(f"❌ Error: Tipo de PDF no soportado ({type(pdf).__name__}).")

    # def merge_pdfs_in_memory(self, pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.
    #     Muestra un reporte con la cantidad de páginas en cada PDF y el total final.

    #     Args:
    #         pdf_list (list): Lista de PDFEditor, BytesIO o PdfReader.
    #         additional_pdfs (list, optional): Lista de PDFs adicionales en BytesIO o PdfReader.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     if not isinstance(pdf_list, list):  # Asegurar que sea una lista
    #         pdf_list = [pdf_list]

    #     pdf_writer = PdfWriter()
    #     total_pages = 0  # Contador total de páginas

    #     # Convertir todos los PDFs a BytesIO
    #     pdf_bytes_list = [self.pdf_to_bytesio(pdf) for pdf in pdf_list]

    #     # Agregar páginas de los PDFs principales
    #     print("\n📄 Reporte de PDFs a unir:")
    #     for index, pdf_bytes in enumerate(pdf_bytes_list):
    #         pdf_bytes.seek(0)  # Asegurar que el puntero está al inicio
    #         pdf_reader = PdfReader(pdf_bytes, strict=False)  # Leer el PDF
            
    #         num_pages = len(pdf_reader.pages)
    #         total_pages += num_pages
    #         print(f"✅ PDF {index + 1} tiene {num_pages} páginas.")

    #         for page_num in range(num_pages):
    #             pdf_writer.add_page(pdf_reader.pages[page_num])  # Agregar todas las páginas

    #     # Agregar PDFs adicionales si existen
    #     if additional_pdfs:
    #         additional_bytes_list = [self.pdf_to_bytesio(pdf) for pdf in additional_pdfs]

    #         for index, pdf_bytes in enumerate(additional_bytes_list):
    #             pdf_bytes.seek(0)
    #             additional_reader = PdfReader(pdf_bytes, strict=False)
    #             num_pages = len(additional_reader.pages)
    #             total_pages += num_pages
    #             print(f"✅ PDF adicional {index + 1} tiene {num_pages} páginas.")

    #             for page_num in range(num_pages):
    #                 pdf_writer.add_page(additional_reader.pages[page_num])  # Agregar todas las páginas

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     print(f"\n📑 Total de páginas en el PDF final: {total_pages}")
    #     return pdf_output


    
    # def merge_pdfs_in_memory(self, pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.

    #     Args:
    #         pdf_list (list): Lista de instancias de PDFEditor con páginas modificadas.
    #         additional_pdfs (list, optional): Lista de BytesIO o PdfReader con PDFs adicionales a combinar.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     pdf_writer = PdfWriter()

    #     # Verificar que cada entrada en pdf_list es un PDFEditor y mostrar cantidad de páginas
    #     for index, pdf_editor in enumerate(pdf_list):
    #         if not isinstance(pdf_editor, PDFEditor):
    #             raise TypeError(f"❌ Error: El elemento en la posición {index} no es una instancia de PDFEditor.")

    #         num_pages = len(pdf_editor.reader.pages)
    #         print(f"✅ PDF {index + 1}: {pdf_editor.pdf_path} tiene {num_pages} páginas.")

    #         # Agregar páginas modificadas u originales
    #         for i in range(num_pages):
    #             if i in pdf_editor.modified_pages:
    #                 pdf_writer.add_page(pdf_editor.modified_pages[i])  # Página modificada
    #             else:
    #                 pdf_writer.add_page(pdf_editor.reader.pages[i])  # Página original

    #     # Agregar PDFs adicionales si los hay
    #     if additional_pdfs:
    #         for index, pdf_source in enumerate(additional_pdfs):
    #             if isinstance(pdf_source, io.BytesIO):
    #                 additional_reader = PdfReader(pdf_source)
    #                 pdf_type = "BytesIO"
    #             elif isinstance(pdf_source, PdfReader):
    #                 additional_reader = pdf_source
    #                 pdf_type = "PdfReader"
    #             else:
    #                 raise ValueError(f"❌ Error: El PDF adicional en la posición {index} no es un objeto válido.")

    #             num_pages = len(additional_reader.pages)
    #             print(f"✅ PDF adicional {index + 1} ({pdf_type}) tiene {num_pages} páginas.")

    #             for page in additional_reader.pages:
    #                 pdf_writer.add_page(page)

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     return pdf_output


    # def merge_pdfs_in_memory(self , pdf_list, additional_pdfs=None):
    #     """
    #     Une múltiples PDFs en memoria y devuelve un objeto BytesIO con el contenido combinado.

    #     Args:
    #         pdf_list (list): Lista de instancias de PDFEditor con páginas modificadas.
    #         additional_pdfs (list, optional): Lista de BytesIO o PdfReader con PDFs adicionales a combinar.

    #     Returns:
    #         BytesIO: PDF combinado en memoria.
    #     """
    #     pdf_writer = PdfWriter()

    #     # Agregar páginas modificadas de cada instancia de PDFEditor
    #     for pdf_editor in pdf_list:
    #         for i in range(len(pdf_editor.reader.pages)):
    #             if i in pdf_editor.modified_pages:
    #                 pdf_writer.add_page(pdf_editor.modified_pages[i])  # Página modificada
    #             else:
    #                 pdf_writer.add_page(pdf_editor.reader.pages[i])  # Página original

    #     # Agregar PDFs adicionales si los hay
    #     if additional_pdfs:
    #         for pdf_source in additional_pdfs:
    #             if isinstance(pdf_source, io.BytesIO):
    #                 additional_reader = PdfReader(pdf_source)
    #             elif isinstance(pdf_source, PdfReader):
    #                 additional_reader = pdf_source
    #             else:
    #                 raise ValueError("Los PDFs adicionales deben ser BytesIO o PdfReader")

    #             for page in additional_reader.pages:
    #                 pdf_writer.add_page(page)

    #     # Guardar el PDF combinado en memoria
    #     pdf_output = io.BytesIO()
    #     pdf_writer.write(pdf_output)
    #     pdf_output.seek(0)  # Reiniciar el puntero al inicio

    #     return pdf_output
    
    
    from PyPDF2 import PdfReader, PdfWriter

    def save_multiples_pdf_to_disk(self, pdf_bytes_io, output_path):
        """
        Guarda un PDF en disco a partir de un objeto BytesIO, asegurando que todas las páginas se conserven.

        Args:
            pdf_bytes_io (BytesIO): PDF en memoria.
            output_path (str): Ruta donde se guardará el archivo PDF.
        """
        pdf_bytes_io.seek(0)
        reader = PdfReader(pdf_bytes_io)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)
    
    
    
    # def save_multiples_pdf_to_disk(self , pdf_bytes_io, output_path):
    #     """
    #     Guarda un PDF en disco a partir de un objeto BytesIO.

    #     Args:
    #         pdf_bytes_io (BytesIO): PDF en memoria.
    #         output_path (str): Ruta donde se guardará el archivo PDF.
    #     """
    #     with open(output_path, "wb") as f:
    #         pdf_bytes_io.seek(0)  # Asegurar que está en el inicio
    #         reader = PdfReader(pdf_bytes_io)
    #         #print(f"🔍 Verificación: El PDF tiene {len(reader.pages)} páginas antes de guardarse.")
    #         f.write(pdf_bytes_io.getvalue())
    
    # def setup_fonts(self, font_names):
    #     """ Registra múltiples fuentes personalizadas especificadas en font_names. """
    #     for font_name in font_names:
    #         font_path = self.fuentesREM.get(font_name, None)
    #         if font_path:
    #             pdfmetrics.registerFont(TTFont(font_name, font_path))
    #             self.fonts[font_name] = font_path
    #             #print(f"Fuente {font_name} configurada.")
    #         else:
    #             pass
    #             #print(f"Fuente {font_name} no encontrada en el diccionario.")

    # def add_text_to_page(self, text, position_mm, page_number, font_name="Helvetica", font_size=12, color=(0, 0, 0), align="left"):
    #     position_points = (self.mm_to_points(position_mm[0]), self.mm_to_points(position_mm[1]))
    #     packet = self._create_text_overlay(text, position_points, font_name, font_size, color, align)
    #     overlay_pdf = PdfFileReader(packet)

    #     if page_number in self.modified_pages:
    #         base_page = self.modified_pages[page_number]
    #     else:
    #         base_page = self.reader.getPage(page_number)

    #     overlay_page = overlay_pdf.getPage(0)
    #     base_page.mergePage(overlay_page)
    #     self.modified_pages[page_number] = base_page

    # def _create_text_overlay(self, text, position, font_name, font_size, color, align):
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)
    #     can.setFont(font_name, font_size)
    #     text_width = can.stringWidth(text, font_name, font_size)

    #     # Ajusta la posición X basada en la alineación
    #     if align == 'center':            
    #         start_x = ((position[0] - text_width) / 2) # * -1
    #     elif align == 'right':
    #         start_x = position[0] - text_width
    #     else:  # default is 'left'
    #         start_x = position[0]

    #     # Asegurarse de que los valores RGB estén correctamente escalados de 0-255 a 0-1
    #     r, g, b = color
    #     can.setFillColorRGB(r / 255.0, g / 255.0, b / 255.0)
    #     can.drawString(start_x, position[1], text)
    #     can.save()

    #     # Regresar al principio del buffer para que pueda ser leído por PdfFileReader
    #     packet.seek(0)
    #     return packet

    # def unirPDFs(self , unaEscuela,pdf_paths, output_pdf_path):
    #     hoja_vacía = cf.carpeta_A_DatosDeEntrada +  '/Plantillas/Plantilla de Fluidez Lectora 2024 medición mayo' + '/4-Página-4-vacía.pdf'
    #     pdf_mayo_2024 = PDF.PDFEditor(
    #         hoja_vacía ,
    #         unaEscuela
    #     ) 
        
    #     pdf_mayo_2024.fusionar_pdfs(
    #         output_pdf_path,
    #         pdf_paths,        
    #     )
    #     return
    
    # def fusionar_pdfs(self,nombre_salida, lista_de_pdfs):
    #     """
    #     Fusiona varios archivos PDF en un solo archivo.

    #     Args:
    #         nombre_salida (str): Ruta del archivo PDF de salida.
    #         lista_de_pdfs (list): Lista de rutas de archivos PDF a combinar.
    #     """
    #     merger = PdfMerger()

    #     for ruta_pdf in lista_de_pdfs:
    #         try:
    #             # Intentar abrir el archivo PDF
    #             with open(ruta_pdf, 'rb') as archivo_pdf:
    #                 merger.append(archivo_pdf)
    #         except FileNotFoundError:
    #             print(f"Error: El archivo {ruta_pdf} no se encontró.")
    #         except Exception as e:
    #             print(f"Error al procesar {ruta_pdf}: {e}")

    #     try:
    #         # Escribir el archivo de salida y cerrar el 'merger'
    #         with open(nombre_salida, 'wb') as salida_pdf:
    #             merger.write(salida_pdf)
    #         print(f"Archivo combinado creado: {nombre_salida}")
    #     except Exception as e:
    #         print(f"Error al escribir el archivo de salida: {e}")
    #     finally:
    #         merger.close()

    # def fusionar_pdfs(self , lista_de_pdfs):
    #     """
    #     Fusiona varios archivos PDF en un solo PDF en memoria.

    #     Args:
    #         lista_de_pdfs (list): Lista de rutas de archivos PDF a combinar.

    #     Returns:
    #         BytesIO: Objeto en memoria con el PDF combinado.
    #     """
    #     merger = PdfMerger()
    #     pdf_output = BytesIO()  # Crear un buffer en memoria

    #     for ruta_pdf in lista_de_pdfs:
    #         try:
    #             with open(ruta_pdf, 'rb') as archivo_pdf:
    #                 merger.append(archivo_pdf)
    #         except FileNotFoundError:
    #             print(f"Error: El archivo {ruta_pdf} no se encontró.")
    #         except Exception as e:
    #             print(f"Error al procesar {ruta_pdf}: {e}")

    #     try:
    #         # Escribir el PDF fusionado en memoria en lugar de un archivo físico
    #         merger.write(pdf_output)
    #         merger.close()
            
    #         # Volver al inicio del buffer para lectura posterior
    #         pdf_output.seek(0)
            
    #         return pdf_output  # Devuelve el objeto en memoria
    #     except Exception as e:
    #         print(f"Error al generar el PDF fusionado: {e}")
    #         return None
        
    # def fusionar_pdfs_memoria(self , lista_de_pdfs_memoria):
    #     """
    #     Fusiona varios PDFs en memoria en un solo PDF en memoria.

    #     Args:
    #         lista_de_pdfs_memoria (list): Lista de objetos BytesIO con PDFs.

    #     Returns:
    #         BytesIO: Objeto en memoria con el PDF combinado.
    #     """
    #     merger = PdfMerger()
    #     pdf_output = BytesIO()  # Buffer en memoria para el resultado

    #     for pdf_mem in lista_de_pdfs_memoria:
    #         try:
    #             pdf_mem.seek(0)  # Asegurarse de que está en el inicio
    #             merger.append(pdf_mem)
    #         except Exception as e:
    #             print(f"Error al procesar un PDF en memoria: {e}")

    #     try:
    #         merger.write(pdf_output)
    #         merger.close()
    #         pdf_output.seek(0)  # Volver al inicio para su lectura posterior
    #         return pdf_output  # Retornar el PDF fusionado en memoria
    #     except Exception as e:
    #         print(f"Error al generar el PDF fusionado: {e}")
    #         return None
        
    def load_pdf(self, template_path):
        # Cargar el PDF base desde la plantilla
        return None  # Reemplaza esto con la lógica real de carga del PDF
    
    # def save_pdf_memoria(self):
    #     """Guarda el PDF en memoria y devuelve un objeto BytesIO."""
    #     pdf_bytes = BytesIO()
    #     self.save_pdf(pdf_bytes)  # Asumiendo que `self.pdf` tiene un método `save`
    #     pdf_bytes.seek(0)  # Mover al inicio para su posterior lectura
    #     return pdf_bytes
    # def save_pdf_memoria(self):
    #     """Guarda el PDF en memoria y devuelve un objeto BytesIO."""
    #     pdf_bytes = BytesIO()

    #     if hasattr(self, "writer") and isinstance(self.writer, PdfWriter):
    #         self.writer.write(pdf_bytes)  # Escribimos el contenido en memoria
    #     else:
    #         raise AttributeError("No se encontró un objeto PdfWriter en la instancia.")

    #     pdf_bytes.seek(0)  # Mover al inicio para su posterior lectura
    #     return pdf_bytes
    def save_pdf_memoria(self):
        """Guarda el PDF en memoria y devuelve un objeto BytesIO."""
        pdf_bytes = BytesIO()

        if not self.writer.pages:
            # Si el writer no tiene páginas, agregamos todas las del reader
            for page in self.reader.pages:
                self.writer.add_page(page)

        self.writer.write(pdf_bytes)  # Escribimos el contenido en BytesIO
        pdf_bytes.seek(0)  # Movemos al inicio para su lectura
        return pdf_bytes
    
    def _create_empty_pdf(self):
        """
        Crea un PDF vacío de una página para superponer contenido.
        """
        packet = BytesIO()
        writer = PdfWriter()
        writer.add_blank_page(width=self.reader.pages[0].mediabox.width,
                            height=self.reader.pages[0].mediabox.height)
        writer.write(packet)
        packet.seek(0)
        return packet

    def add_text_to_page_free(
        self, 
        text, 
        position_mm, 
        page_number, 
        font_name="Helvetica", 
        font_size=12, 
        color=(0, 0, 0), 
        align="left",
        valign="top"  # <-- Nuevo parámetro opcional: vertical align
    ):
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter

        # Convertir posición en milímetros a puntos
        x_pt = self.mm_to_points(position_mm[0])
        y_pt = self.mm_to_points(position_mm[1])

        # Obtener el tamaño de la página actual
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]

        page_width = float(base_page.mediabox.width)
        page_height = float(base_page.mediabox.height)

        # Crear el canvas de overlay
        packet = self._create_empty_pdf()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
        can.setFont(font_name, font_size)
        can.setFillColorRGB(*color)

        # Medir el ancho y la altura del texto
        text_width = can.stringWidth(text, font_name, font_size)
        text_height = font_size  # Aproximadamente el tamaño de la fuente en puntos

        # Ajuste horizontal
        if align == "center":
            x_pt -= text_width / 2
        elif align == "right":
            x_pt -= text_width

        # Ajuste vertical
        if valign == "middle":
            y_pt -= text_height / 2
        elif valign == "bottom":
            y_pt -= text_height

        # Dibujar el texto
        can.drawString(x_pt, y_pt, text)
        can.save()

        # Leer el overlay
        packet.seek(0)
        overlay_pdf = PdfReader(packet)
        overlay_page = overlay_pdf.pages[0]

        # Mezclar el overlay con la página
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page

    def add_wrapped_text_to_page(
        self,
        text, 
        position_mm, 
        page_number, 
        font_name="Helvetica", 
        font_size=12, 
        color=(0, 0, 0), 
        align="left",
        interlineado=1.0,
        margen_derecho_mm=20
    ):
        from reportlab.pdfgen import canvas

        x_pt = self.mm_to_points(position_mm[0])
        y_pt = self.mm_to_points(position_mm[1])
        margen_derecho_pt = self.mm_to_points(margen_derecho_mm)

        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]

        page_width = float(base_page.mediabox.width)
        page_height = float(base_page.mediabox.height)

        packet = self._create_empty_pdf()
        can = canvas.Canvas(packet, pagesize=(page_width, page_height))
        can.setFont(font_name, font_size)
        can.setFillColorRGB(*color)

        text_height = font_size * interlineado
        max_line_width = page_width - x_pt - margen_derecho_pt

        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + " " + word if current_line else word
            test_width = can.stringWidth(test_line, font_name, font_size)
            if test_width <= max_line_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        for line in lines:
            line_width = can.stringWidth(line, font_name, font_size)
            line_x = x_pt
            if align == "center":
                line_x = x_pt + (max_line_width - line_width) / 2
            elif align == "right":
                line_x = x_pt + (max_line_width - line_width)

            can.drawString(line_x, y_pt, line)
            y_pt -= text_height

        can.save()

        packet.seek(0)
        overlay_pdf = PdfReader(packet)
        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page







    def add_text_to_page(self, text, position_mm, page_number, font_name="Helvetica", font_size=12, 
                     color=(0, 0, 0), align="left", 
                     box=False, box_color=(0, 0, 255), box_padding=3, box_border_width=2,
                     link_to_page=None):
        """
        Agrega texto a una página del PDF con opción de cuadro de fondo y enlace interno.
        
        Parámetros:
        - text: texto a insertar
        - position_mm: tupla (x, y) en milímetros
        - page_number: número de página donde insertar el texto
        - font_name: nombre de la fuente
        - font_size: tamaño de la fuente
        - color: color del texto RGB (0-255, 0-255, 0-255)
        - align: alineación del texto ('left', 'center', 'right')
        - box: si es True, dibuja un cuadro de fondo
        - box_color: color del cuadro RGB (0-255, 0-255, 0-255)
        - box_padding: espaciado interno del cuadro en mm
        - box_border_width: grosor del borde en puntos
        - link_to_page: número de página destino del enlace (None = sin enlace)
        """
        position_points = (self.mm_to_points(position_mm[0]), self.mm_to_points(position_mm[1]))
        
        packet = self._create_text_overlay(
            text, position_points, font_name, font_size, color, align,
            box=box, box_color=box_color, box_padding=box_padding, box_border_width=box_border_width,
            link_to_page=link_to_page
        )
        
        overlay_pdf = PdfReader(packet)
        
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]
        
        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page


    def _create_text_overlay(self, text, position, font_name, font_size, color, align,
                        box=False, box_color=(0, 0, 255), box_padding=3, box_border_width=2,
                        link_to_page=None):
        """
        Crea un overlay de texto con opción de cuadro de fondo y enlace interno.
        """
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        can.setFont(font_name, font_size)

        # Asegurarse de que los valores RGB estén correctamente escalados de 0-255 a 0-1
        r, g, b = color
        text_color = (r / 255.0, g / 255.0, b / 255.0)

        # Calcular el ancho máximo disponible para el texto
        if '-multiline' in align:
            max_width = A4[0] - 2 * self.mm_to_points(20)
            lines = simpleSplit(text, font_name, font_size, max_width)
        else:
            lines = [text]

        # Variables para el área del enlace
        link_rect = None
        
        # Si hay cuadro, calculamos sus dimensiones
        if box:
            # Calcular el ancho máximo del texto
            max_text_width = max([can.stringWidth(line, font_name, font_size) for line in lines])
            
            # Convertir padding a puntos
            padding_points = self.mm_to_points(box_padding)
            
            # Dimensiones del cuadro
            box_width = max_text_width + (padding_points * 2)
            box_height = (len(lines) * font_size * 1.2) + (padding_points * 2)
            
            # Posición del cuadro (usa la posición dada como esquina inferior izquierda)
            box_x = position[0]
            box_y = position[1]
            
            # Guardar área para el enlace
            if link_to_page is not None:
                link_rect = (box_x, box_y, box_x + box_width, box_y + box_height)
            
            # Dibujar el cuadro con color de fondo
            box_r, box_g, box_b = box_color
            can.setFillColorRGB(box_r / 255.0, box_g / 255.0, box_b / 255.0)
            #can.setStrokeColorRGB(0, 0, 0)  # Borde negro
            can.setLineWidth(box_border_width)
            can.rect(box_x, box_y, box_width, box_height, fill=1, stroke=1)

        # Configurar color del texto
        can.setFillColorRGB(text_color[0], text_color[1], text_color[2])

        # Calcular posición inicial del texto
        if box:
            # Convertir padding a puntos
            padding_points = self.mm_to_points(box_padding)
            
            # Calcular altura del cuadro
            box_height_calc = (len(lines) * font_size * 1.2) + (padding_points * 2)
            
            # Centrado vertical perfecto
            current_y = position[1] + (box_height_calc / 2) - (font_size * 0.35)
        else:
            current_y = position[1]
        
        # Variables para calcular el área del texto (si no hay box)
        text_min_x = float('inf')
        text_max_x = 0
        text_min_y = current_y
        text_max_y = current_y
        
        for line in lines:
            text_width = can.stringWidth(line, font_name, font_size)
            
            if box:
                # Centrar horizontalmente dentro del cuadro
                padding_points = self.mm_to_points(box_padding)
                max_text_width = max([can.stringWidth(l, font_name, font_size) for l in lines])
                box_width_calc = max_text_width + (padding_points * 2)
                
                # Posición X centrada dentro del cuadro
                start_x = position[0] + (box_width_calc / 2) - (text_width / 2)
            else:
                # Alineación normal sin cuadro
                if 'center' in align:
                    start_x = (A4[0] / 2) - (text_width / 2)
                elif 'right' in align:
                    start_x = A4[0] - self.mm_to_points(20) - text_width
                else:  # left
                    start_x = position[0]
                
                # Actualizar área del texto para el enlace
                text_min_x = min(text_min_x, start_x)
                text_max_x = max(text_max_x, start_x + text_width)
                text_min_y = min(text_min_y, current_y)

            can.drawString(start_x, current_y, line)
            current_y -= font_size * 1.2  # Bajar una línea con espaciado
        
        # Si no hay box pero hay enlace, calcular el área del texto
        if link_to_page is not None and not box:
            text_max_y = text_min_y + (len(lines) * font_size * 1.2)
            link_rect = (text_min_x, text_min_y, text_max_x, text_max_y)
        
        # Agregar el enlace interno si está definido
        if link_to_page is not None and link_rect is not None:
            from reportlab.pdfgen.canvas import Canvas
            
            # Crear un destino único para la página
            destination_name = f"page_{link_to_page}"
            
            # Agregar anotación de enlace usando linkAbsolute con destino interno
            can.linkAbsolute(
                destination_name,  # Nombre del destino
                destination_name,  # Mismo nombre
                link_rect,  # Área clicable (x1, y1, x2, y2)
                Border='[0 0 0]'  # Sin borde visible en el enlace
            )

        can.save()
        packet.seek(0)
        return packet
    
    def add_internal_link(self, page_number, rect_mm, destination_page):
        """
        Agrega un enlace interno a una página del PDF después de que el texto/cuadro ya esté dibujado.
        
        Parámetros:
        - page_number: página donde está el enlace
        - destination_page: página destino del enlace
        - rect_mm: tupla (x, y, ancho, alto) en milímetros del área clicable
        """
        from PyPDF2.generic import DictionaryObject, ArrayObject, NumberObject, NameObject
        
        # Validar que las páginas existen
        total_pages = len(self.reader.pages)
        
        if page_number >= total_pages:
            print(f"⚠️ Advertencia: La página {page_number} no existe (total: {total_pages} páginas)")
            return
        
        if destination_page >= total_pages:
            print(f"⚠️ Advertencia: La página destino {destination_page} no existe (total: {total_pages} páginas). No se agregó el enlace.")
            return
        
        # Convertir coordenadas de mm a puntos
        x_mm, y_mm, width_mm, height_mm = rect_mm
        x = self.mm_to_points(x_mm)
        y = self.mm_to_points(y_mm)
        width = self.mm_to_points(width_mm)
        height = self.mm_to_points(height_mm)
        
        # Obtener la página
        if page_number in self.modified_pages:
            page = self.modified_pages[page_number]
        else:
            page = self.reader.pages[page_number]
        
        # Crear el rectángulo del enlace
        link_rect = ArrayObject([
            NumberObject(x),
            NumberObject(y),
            NumberObject(x + width),
            NumberObject(y + height)
        ])
        
        # Crear la acción de ir a página
        go_to_action = DictionaryObject()
        go_to_action.update({
            NameObject("/S"): NameObject("/GoTo"),
            NameObject("/D"): ArrayObject([
                self.reader.pages[destination_page].indirect_reference,
                NameObject("/Fit")
            ])
        })
        
        # Crear la anotación de enlace
        link_annotation = DictionaryObject()
        link_annotation.update({
            NameObject("/Type"): NameObject("/Annot"),
            NameObject("/Subtype"): NameObject("/Link"),
            NameObject("/Rect"): link_rect,
            NameObject("/Border"): ArrayObject([NumberObject(0), NumberObject(0), NumberObject(0)]),
            NameObject("/A"): go_to_action
        })
        
        # Agregar la anotación a la página
        if "/Annots" in page:
            page["/Annots"].append(link_annotation)
        else:
            page[NameObject("/Annots")] = ArrayObject([link_annotation])
        
        # ✅ CRÍTICO: Marcar la página como modificada
        self.modified_pages[page_number] = page
        print(f"✅ Enlace agregado: Página {page_number} → Página {destination_page}")
        
    def verificar_paginas(self):
        """
        Verifica cuántas páginas tiene el PDF cargado.
        """
        total = len(self.reader.pages)
        print(f"📄 El PDF tiene {total} página(s)")
        print(f"   Páginas válidas: 0 a {total - 1}")
        return total


    # def _create_text_overlay(self, text, position, font_name, font_size, color, align):
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)
    #     can.setFont(font_name, font_size)

    #     # Asegurarse de que los valores RGB estén correctamente escalados de 0-255 a 0-1
    #     r, g, b = color
    #     can.setFillColorRGB(r / 255.0, g / 255.0, b / 255.0)

    #     # Calcular el ancho máximo disponible para el texto
    #     if '-multiline' in align:
    #         max_width = A4[0] - 2 * self.mm_to_points(20)  # Margen de 20 mm a cada lado
    #         lines = simpleSplit(text, font_name, font_size, max_width)
    #     else:
    #         lines = [text]

    #     # Ajustar la posición Y inicial
    #     current_y = position[1]
    #     for line in lines:
    #         text_width = can.stringWidth(line, font_name, font_size)
    #         if 'center' in align:
    #             start_x = (A4[0] / 2) - (text_width / 2)
    #         elif 'right' in align:
    #             start_x = A4[0] - self.mm_to_points(20) - text_width  # Alineación a la derecha con margen de 20 mm
    #         else:  # default is 'left'
    #             start_x = self.mm_to_points(20)  # Alineación a la izquierda con margen de 20 mm

    #         can.drawString(start_x, current_y, line)
    #         current_y -= font_size  # Bajar una línea

    #     can.save()

    #     # Regresar al principio del buffer para que pueda ser leído por PdfFileReader
    #     packet.seek(0)
    #     return packet



    def save_pdf(self, output_pdf_path):
        # Primero, agregar todas las páginas que no han sido modificadas
        for i in range(len(self.reader.pages)):  # Reemplaza getNumPages() con len(self.reader.pages)
            if i not in self.modified_pages:
                self.writer.add_page(self.reader.pages[i])  # Cambia addPage por add_page y getPage por pages[i]

        # Ahora, agregar todas las páginas modificadas
        for page_number, page in self.modified_pages.items():
            self.writer.add_page(page)  # Cambia addPage por add_page

        # Guardar el PDF en el archivo de salida
        with open(output_pdf_path, 'wb') as f:
            self.writer.write(f)
            
    def save_to_stream(self):
        """
        Guarda el PDF modificado en un BytesIO stream.
        IMPORTANTE: Usa un nuevo writer para asegurar que todas las anotaciones se guarden.
        """
        output = io.BytesIO()
        
        # Crear un nuevo writer para asegurar que todo se guarde correctamente
        new_writer = PdfWriter()
        
        # Agregar todas las páginas al writer
        for i in range(len(self.reader.pages)):
            if i in self.modified_pages:
                new_writer.add_page(self.modified_pages[i])
            else:
                new_writer.add_page(self.reader.pages[i])
        
        # Escribir en el stream
        new_writer.write(output)
        output.seek(0)
        return output




    def save(self, output):
        """
        Método unificado que detecta si es ruta o stream.
        
        Args:
            output (str or BytesIO): Ruta de archivo o stream BytesIO
        
        Returns:
            str or BytesIO: La misma salida proporcionada
        
        Example:
            # Guardar en archivo
            editor.save('output.pdf')
            
            # Guardar en memoria
            from io import BytesIO
            stream = BytesIO()
            editor.save(stream)
        """
        from io import BytesIO
        
        # Agregar páginas no modificadas
        for i in range(len(self.reader.pages)):
            if i not in self.modified_pages:
                self.writer.add_page(self.reader.pages[i])

        # Agregar páginas modificadas
        for page_number, page in self.modified_pages.items():
            self.writer.add_page(page)

        # Detectar tipo de salida
        if isinstance(output, BytesIO):
            # Es un stream
            self.writer.write(output)
            output.seek(0)
            return output
        elif isinstance(output, str):
            # Es una ruta de archivo
            with open(output, 'wb') as f:
                self.writer.write(f)
            return output
        else:
            raise TypeError("output debe ser str (ruta) o BytesIO (stream)")


    # ============================================================================
    # MÉTODOS ESTÁTICOS PARA UNIR PDFS EN MEMORIA
    # ============================================================================

    @staticmethod
    def unir_pdfs_en_memoria(lista_pdfs_bytes, verbose=True):
        """
        Une múltiples PDFs que están en memoria (bytes).
        
        Args:
            lista_pdfs_bytes (list): Lista de objetos bytes o BytesIO con contenido PDF
            verbose (bool): Si True, imprime información del proceso
        
        Returns:
            BytesIO: Objeto BytesIO con el PDF unificado, o None si hay error
        
        Example:
            # Leer PDFs en memoria
            pdf1 = open('doc1.pdf', 'rb').read()
            pdf2 = open('doc2.pdf', 'rb').read()
            
            # Unir en memoria
            pdf_unido = PDFEditor.unir_pdfs_en_memoria([pdf1, pdf2])
            
            # Guardar resultado
            with open('resultado.pdf', 'wb') as f:
                f.write(pdf_unido.getvalue())
        """
        from io import BytesIO
        from PyPDF2 import PdfMerger, PdfReader
        
        try:
            if not lista_pdfs_bytes:
                print("❌ Error: La lista está vacía")
                return None
            
            merger = PdfMerger()
            
            for i, pdf_data in enumerate(lista_pdfs_bytes, 1):
                try:
                    # Convertir a BytesIO si es bytes
                    if isinstance(pdf_data, bytes):
                        pdf_stream = BytesIO(pdf_data)
                    elif isinstance(pdf_data, BytesIO):
                        pdf_stream = pdf_data
                        pdf_stream.seek(0)  # Asegurar que esté al inicio
                    else:
                        print(f"⚠️  Tipo no soportado en posición {i}")
                        continue
                    
                    # Validar que sea un PDF válido
                    try:
                        PdfReader(pdf_stream)
                        pdf_stream.seek(0)  # Volver al inicio después de validar
                    except Exception as e:
                        print(f"❌ El archivo {i} no es un PDF válido: {e}")
                        continue
                    
                    merger.append(pdf_stream)
                    if verbose:
                        print(f"✓ PDF {i}/{len(lista_pdfs_bytes)} agregado")
                    
                except Exception as e:
                    print(f"❌ Error al procesar PDF {i}: {e}")
                    continue
            
            # Crear BytesIO para el resultado
            output = BytesIO()
            merger.write(output)
            merger.close()
            
            # Posicionar al inicio para lectura
            output.seek(0)
            
            if verbose:
                tamaño_kb = len(output.getvalue()) / 1024
                print(f"\n✅ PDF unificado creado en memoria ({tamaño_kb:.2f} KB)")
            
            return output
        
        except Exception as e:
            print(f"❌ Error al unir PDFs: {e}")
            return None


    @staticmethod
    def unir_pdfs_mixto(lista_items, verbose=True):
        """
        Une PDFs que pueden estar en memoria (bytes) o en disco (rutas).
        
        Args:
            lista_items (list): Lista con rutas (str), bytes, o BytesIO
            verbose (bool): Si True, imprime información
        
        Returns:
            BytesIO: PDF unificado en memoria
        
        Example:
            items = [
                'archivo1.pdf',           # Desde disco
                pdf_bytes,                # En memoria (bytes)
                BytesIO(otro_pdf),        # En memoria (BytesIO)
                'archivo2.pdf'            # Desde disco
            ]
            resultado = PDFEditor.unir_pdfs_mixto(items)
        """
        from io import BytesIO
        from PyPDF2 import PdfMerger, PdfReader
        import os
        
        try:
            merger = PdfMerger()
            
            for i, item in enumerate(lista_items, 1):
                try:
                    # Si es una ruta de archivo
                    if isinstance(item, str):
                        if not os.path.exists(item):
                            print(f"⚠️  No existe: {item}")
                            continue
                        
                        with open(item, 'rb') as f:
                            pdf_stream = BytesIO(f.read())
                        
                        if verbose:
                            print(f"✓ Agregado desde disco ({i}): {os.path.basename(item)}")
                    
                    # Si es bytes
                    elif isinstance(item, bytes):
                        pdf_stream = BytesIO(item)
                        if verbose:
                            tamaño_kb = len(item) / 1024
                            print(f"✓ Agregado desde memoria ({i}): {tamaño_kb:.2f} KB")
                    
                    # Si es BytesIO
                    elif isinstance(item, BytesIO):
                        pdf_stream = item
                        pdf_stream.seek(0)
                        if verbose:
                            print(f"✓ Agregado BytesIO ({i})")
                    
                    else:
                        print(f"⚠️  Tipo no soportado en posición {i}")
                        continue
                    
                    merger.append(pdf_stream)
                    
                except Exception as e:
                    print(f"❌ Error al procesar item {i}: {e}")
                    continue
            
            output = BytesIO()
            merger.write(output)
            merger.close()
            output.seek(0)
            
            if verbose:
                tamaño_kb = len(output.getvalue()) / 1024
                print(f"\n✅ PDF creado: {tamaño_kb:.2f} KB")
            
            return output
        
        except Exception as e:
            print(f"❌ Error: {e}")
            return None


    @staticmethod
    def guardar_pdf_desde_memoria(pdf_bytesio, ruta_salida):
        """
        Guarda un PDF que está en memoria a disco.
        
        Args:
            pdf_bytesio (BytesIO): PDF en memoria
            ruta_salida (str): Ruta donde guardar el archivo
        
        Returns:
            bool: True si se guardó exitosamente
        """
        import os
        
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(ruta_salida) or '.', exist_ok=True)
            
            with open(ruta_salida, 'wb') as f:
                pdf_bytesio.seek(0)
                f.write(pdf_bytesio.read())
            
            tamaño_kb = os.path.getsize(ruta_salida) / 1024
            print(f"✅ PDF guardado en: {ruta_salida} ({tamaño_kb:.2f} KB)")
            return True
        
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
            return False

    # def add_table_to_pdf(self, header, data, y_position_mm, page_number, output_pdf_path):
    #     """Añade una tabla al PDF en una página específica, centrando horizontalmente la tabla."""
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=letter)
        
    #     # Convertir los milímetros a puntos para la posición
    #     y_pos = self.mm_to_points(y_position_mm)

    #     color_encabezado = colors.Color(49/255, 122/255, 138/255)
    #     color_ultima_fila = colors.Color(157/255, 222/255, 220/255)
        
    #     # Crear la tabla
    #     table_data = [header] + data
    #     table = Table(table_data)
    #     table.setStyle(TableStyle([
    #         ('BACKGROUND', (0, 0), (-1, 0), color_encabezado),
    #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    #         ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    #         ('FONTSIZE', (0, 0), (-1, -1), 12),
    #         ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    #         ('BACKGROUND', (0, 1), (-1, -2), colors.white),  # Estilo de fondo para filas normales
    #         ('BACKGROUND', (0, -1), (-1, -1), color_ultima_fila),  # Estilo de fondo para la última fila
    #         ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #     ]))

    #     # Calcular el ancho y alto de la página para centrar la tabla
    #     width, height = letter
    #     table.wrapOn(can, width, height)
    #     table_width, table_height = table.wrap(0, 0)  # Obtiene el tamaño necesario para la tabla
    #     x_pos = (width - table_width) / 2  # Centra la tabla horizontalmente

    #     # Dibujar la tabla en el canvas
    #     table.drawOn(can, x_pos, y_pos)

    #     # Finalizar el dibujo y mover el contenido al PDF
    #     can.save()
    #     packet.seek(0)
    #     overlay_pdf = PdfFileReader(packet)

    #     # Merge the overlay into the original PDF
    #     base_page = self.reader.getPage(page_number)
    #     base_page.mergePage(overlay_pdf.getPage(0))
    #     self.writer.addPage(base_page)

    #     # Guardar el PDF actualizado
    #     with open(output_pdf_path, 'wb') as f:
    #         self.writer.write(f)

    # def add_overlay_to_pdf(self, overlay_pdf, page_number, output_pdf_path):
    #     """Añade un overlay PDF a una página específica y guarda el PDF final."""
    #     base_page = self.reader.getPage(page_number)
    #     base_page.mergePage(overlay_pdf.getPage(0))
    #     self.writer.addPage(base_page)

    #     with open(output_pdf_path, 'wb') as f:
    #         self.writer.write(f)

    # def create_table_overlay(self, header, data, y_position_mm):
    #     """Crea un overlay PDF con una tabla centrada horizontalmente."""
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=letter)

    #     y_pos = self.mm_to_points(y_position_mm)

    #     color_encabezado = colors.Color(49/255, 122/255, 138/255)
    #     color_ultima_fila = colors.Color(157/255, 222/255, 220/255)

    #     table_data = [header] + data
    #     table = Table(table_data)
    #     table.setStyle(TableStyle([
    #         ('BACKGROUND', (0, 0), (-1, 0), color_encabezado),
    #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    #         ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    #         ('FONTSIZE', (0, 0), (-1, -1), 12),
    #         ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    #         ('BACKGROUND', (0, 1), (-1, -2), colors.white),
    #         ('BACKGROUND', (0, -1), (-1, -1), color_ultima_fila),
    #         ('GRID', (0, 0), (-1, -1), 1, colors.black),

    #         # ('BACKGROUND', (0, 0), (-1, 0), color_encabezado),
    #         # ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #         # ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #         # ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
    #         # ('FONTSIZE', (0, 0), (-1, 0), 14),  # Aumenta el tamaño de la fuente para el título
    #         # ('BOTTOMPADDING', (0, 0), (-1, 0), 15),  # Aumenta el padding inferior del título
    #         # ('TOPPADDING', (0, 0), (-1, 0), 15),  # Aumenta el padding superior del título
    #         # ('FONTNAME', (1, 1), (-1, -1), 'REM-Regular'),
    #         # ('FONTSIZE', (1, 1), (-1, -1), 10),  # Tamaño de fuente para el resto de la tabla
    #         # ('BACKGROUND', (0, 1), (-1, -2), colors.white),
    #         # ('BACKGROUND', (0, -1), (-1, -1), color_ultima_fila),
    #         # ('GRID', (0, 0), (-1, -1), 1, colors.black),
    #     ]))

    #     width, height = letter
    #     table.wrapOn(can, width, height)
    #     table_width, table_height = table.wrap(0, 0)
    #     x_pos = (width - table_width) / 2

    #     table.drawOn(can, x_pos, y_pos)
    #     can.save()
    #     packet.seek(0)
    #     return PdfFileReader(packet)

    def add_matplotlib_figure_to_pdf(self, figure, position_mm, page_number, width_mm=None, height_mm=None):
        """
        Inserta una imagen generada por Matplotlib en una página específica del PDF.
        """
        import matplotlib.pyplot as plt
        from PIL import Image

        page_width_mm = 210  # A4 horizontal en mm

        try:
            # Guardar la figura de Matplotlib en un objeto BytesIO
            img_bytes = io.BytesIO()
            
            # 🧠 Intentar guardar con dpi más bajo y sin bbox_inches para evitar problemas de memoria
            figure.savefig(img_bytes, format="png", dpi=150)  # bbox_inches="tight" puede causar bitmap error
            img_bytes.seek(0)

            # Guardar la imagen en un archivo temporal
            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                temp_path = temp_file.name
                temp_file.write(img_bytes.read())

            # Crear un nuevo PDF en memoria
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=A4)

            # Si se proporcionan dimensiones, usar esas
            if width_mm and height_mm:
                width_pt = self.mm_to_points(width_mm)
                height_pt = self.mm_to_points(height_mm)
                x_position_mm = (page_width_mm - width_mm) / 2
                x_position_points = self.mm_to_points(x_position_mm)
            else:
                # Obtener tamaño real de la imagen desde el archivo
                img = Image.open(temp_path)
                img_width_mm = img.width / self.points_per_mm
                img_height_mm = img.height / self.points_per_mm
                width_pt = self.mm_to_points(img_width_mm)
                height_pt = self.mm_to_points(img_height_mm)
                x_position_mm = (page_width_mm - img_width_mm) / 2
                x_position_points = self.mm_to_points(x_position_mm)

            y_position_points = self.mm_to_points(position_mm[1])
            can.drawImage(temp_path, x_position_points, y_position_points, width=width_pt, height=height_pt, mask="auto")

            can.save()
            packet.seek(0)
            overlay_pdf = PdfReader(packet)

            # Mezclar con la página base
            if page_number in self.modified_pages:
                base_page = self.modified_pages[page_number]
            else:
                base_page = self.reader.pages[page_number]

            overlay_page = overlay_pdf.pages[0]
            base_page.merge_page(overlay_page)
            self.modified_pages[page_number] = base_page

        except Exception as e:
            print(f"❌ Error al agregar figura Matplotlib al PDF: {e}")

        finally:
            # 🔁 Cerrar la figura para liberar memoria
            plt.close(figure)


    # def add_matplotlib_figure_to_pdf(self, figure, position_mm, page_number, width_mm=None, height_mm=None):
    #     """
    #     Inserta una imagen generada por Matplotlib en una página específica del PDF.

    #     Args:
    #     figure (matplotlib.figure.Figure): Figura de Matplotlib a insertar.
    #     position_mm (tuple): Posición (x, y) en mm dentro del PDF.
    #     page_number (int): Número de la página en el PDF.
    #     width_mm (float): Ancho de la imagen en mm (opcional).
    #     height_mm (float): Alto de la imagen en mm (opcional).
    #     """
    #     page_width_mm = 210  # Ancho de página A4 en mm

    #     # Guardar la figura de Matplotlib en un objeto BytesIO
    #     img_bytes = io.BytesIO()
    #     figure.savefig(img_bytes, format="png", bbox_inches="tight", dpi=300)  # Guardar como PNG
    #     img_bytes.seek(0)  # Reiniciar el puntero al inicio

    #     # Guardar la imagen en un archivo temporal
    #     with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
    #         temp_path = temp_file.name
    #         temp_file.write(img_bytes.read())  # Escribir la imagen en el archivo temporal

    #     # Crear un nuevo PDF en memoria para dibujar la imagen
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)

    #     # Si se proporcionan dimensiones, calcular la posición centrada
    #     if width_mm and height_mm:
    #         width_pt = self.mm_to_points(width_mm)
    #         height_pt = self.mm_to_points(height_mm)
    #         x_position_mm = (page_width_mm - width_mm) / 2  # Centrar la imagen
    #         x_position_points = self.mm_to_points(x_position_mm)
    #     else:
    #         # Obtener tamaño real de la imagen
    #         from PIL import Image
    #         img = Image.open(temp_path)
    #         img_width_mm = img.width / self.points_per_mm
    #         img_height_mm = img.height / self.points_per_mm
    #         width_pt = self.mm_to_points(img_width_mm)
    #         height_pt = self.mm_to_points(img_height_mm)
    #         x_position_mm = (page_width_mm - img_width_mm) / 2
    #         x_position_points = self.mm_to_points(x_position_mm)

    #     y_position_points = self.mm_to_points(position_mm[1])
    #     can.drawImage(temp_path, x_position_points, y_position_points, width=width_pt, height=height_pt, mask="auto")

    #     # Finalizar el dibujo
    #     can.save()
    #     packet.seek(0)
    #     overlay_pdf = PdfReader(packet)

    #     # Obtener la página base del PDF y combinarla con la imagen
    #     if page_number in self.modified_pages:
    #         base_page = self.modified_pages[page_number]
    #     else:
    #         base_page = self.reader.pages[page_number]

    #     overlay_page = overlay_pdf.pages[0]
    #     base_page.merge_page(overlay_page)
    #     self.modified_pages[page_number] = base_page

    

    def add_table_to_page(self, header, data, y_position_mm, page_number, tableStyle, col_widths_mm=None):
        """Añade una tabla a una página específica del PDF, centrando la tabla horizontalmente y colocándola en la posición y especificada."""
        # Crear un paquete en memoria para dibujar la tabla
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        # Convertir la posición de y de milímetros a puntos
        y_position_points = mm_to_points(y_position_mm)

        # Preparar los datos de la tabla
        table_data = [header] + data

        # Si se proporcionan anchos de columna, convertirlos a puntos
        if col_widths_mm:
            col_widths = [mm_to_points(width) for width in col_widths_mm]
            table = Table(table_data, colWidths=col_widths)
        else:
            table = Table(table_data)

        # Añadir estilos adicionales para ajustar el texto y alinear verticalmente
        table_style = TableStyle(tableStyle)
        table_style.add('WORDWRAP', (0, 0), (-1, -1), 'CJK')  # Habilitar el ajuste de texto
        table_style.add('VALIGN', (0, 0), (-1, -1), 'MIDDLE')  # Alinear verticalmente al centro

        table.setStyle(table_style)

        # Obtener el tamaño de la página
        width, height = A4
        table_width, table_height = table.wrap(0, 0)
        x_position_points = (width - table_width) / 2  # Centrar horizontalmente

        # Dibujar la tabla en el lienzo
        table.drawOn(can, x_position_points, y_position_points)
        can.save()
        packet.seek(0)

        # Leer el overlay creado
        overlay_pdf = PdfReader(packet)

        # Obtener la página base del PDF y combinarla con el overlay
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
             base_page = self.reader.pages[page_number] # base_page = self.reader.getPage(page_number)

        overlay_page = overlay_pdf.pages[0] # overlay_page = overlay_pdf.getPage(0)
        base_page.merge_page(overlay_page) # base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page

        return self

    # def add_table_to_page(self, header, data, y_position_mm, page_number , tableStyle):
    #     """Añade una tabla a una página específica del PDF, centrando la tabla horizontalmente y colocándola en la posición y especificada."""
    #     # Crear un paquete en memoria para dibujar la tabla
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)

    #     # Convertir la posición de y de milímetros a puntos
    #     y_position_points = self.mm_to_points(y_position_mm)

    #     table_data = [header] + data
    #     table = Table(table_data)
    #     table.setStyle(TableStyle(tableStyle))

    #     width, height = letter
    #     table_width, table_height = table.wrap(0, 0)
    #     x_position_points = (width - table_width) / 2  # Centrar horizontalmente

    #     table.drawOn(can, x_position_points, y_position_points)
    #     can.save()
    #     packet.seek(0)

    #     # Leer el overlay creado
    #     overlay_pdf = PdfFileReader(packet)

    #     # Obtener la página base del PDF y combinarla con el overlay
    #     if page_number in self.modified_pages:
    #         base_page = self.modified_pages[page_number]
    #     else:
    #         base_page = self.reader.getPage(page_number)

    #     overlay_page = overlay_pdf.getPage(0)
    #     base_page.mergePage(overlay_page)
    #     self.modified_pages[page_number] = base_page

    #     return self

    def add_plotly_figure_to_pdf(self, figure, position_mm, page_number, width_mm=None, height_mm=None):
        """
        Inserta una imagen generada por Plotly en una página específica del PDF.

        Args:
        figure (plotly.graph_objects.Figure): Figura de Plotly a insertar.
        position_mm (tuple): Posición (x, y) en mm dentro del PDF.
        page_number (int): Número de la página en el PDF.
        width_mm (float): Ancho de la imagen en mm (opcional).
        height_mm (float): Alto de la imagen en mm (opcional).
        """
        page_width_mm = 210  # Ancho de página A4 en mm

        # Convertir la figura de Plotly en una imagen en BytesIO
        img_bytes = io.BytesIO()
        figure.write_image(img_bytes, format="png")  # Guardar como PNG
        img_bytes.seek(0)  # Reiniciar el puntero al inicio

        # Guardar la imagen en un archivo temporal
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(img_bytes.read())  # Escribir la imagen en el archivo temporal

        # Crear un nuevo PDF en memoria para dibujar la imagen
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        # Si se proporcionan dimensiones, calcular la posición centrada
        if width_mm and height_mm:
            width_pt = self.mm_to_points(width_mm)
            height_pt = self.mm_to_points(height_mm)
            x_position_mm = (page_width_mm - width_mm) / 2  # Centrar la imagen
            x_position_points = self.mm_to_points(x_position_mm)
        else:
            # Obtener tamaño real de la imagen
            img = Image.open(temp_path)
            img_width_mm = img.width / self.points_per_mm
            img_height_mm = img.height / self.points_per_mm
            width_pt = self.mm_to_points(img_width_mm)
            height_pt = self.mm_to_points(img_height_mm)
            x_position_mm = (page_width_mm - img_width_mm) / 2
            x_position_points = self.mm_to_points(x_position_mm)

        y_position_points = self.mm_to_points(position_mm[1])
        can.drawImage(temp_path, x_position_points, y_position_points, width=width_pt, height=height_pt, mask="auto")

        # Finalizar el dibujo
        can.save()
        packet.seek(0)
        overlay_pdf = PdfReader(packet)

        # Obtener la página base del PDF y combinarla con la imagen
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]

        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page



    

    def add_image_to_page(self, image_path, position_mm, page_number, width_mm=None, height_mm=None):
        """
        Inserta una imagen en una página específica del PDF, centrando la imagen horizontalmente.

        Args:
        image_path (str): Ruta al archivo de imagen.
        position_mm (tuple): Posición y en milímetros donde se colocará la imagen.
        page_number (int): Número de página en el PDF donde se insertará la imagen.
        width_mm (float): Ancho de la imagen en milímetros (opcional).
        height_mm (float): Alto de la imagen en milímetros (opcional).
        """
        page_width_mm = 210  # Ancho de una página tamaño carta en milímetros

        # Convertir la posición de milímetros a puntos
        y_position_points = self.mm_to_points(position_mm[1])

        # Crear un nuevo PDF en memoria para dibujar la imagen
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        
        if width_mm and height_mm:
            width_pt = self.mm_to_points(width_mm)
            height_pt = self.mm_to_points(height_mm)
            # Calcular la posición x para centrar la imagen horizontalmente
            x_position_mm = (page_width_mm - width_mm) / 2
            x_position_points = self.mm_to_points(x_position_mm)
            can.drawImage(image_path, x_position_points, y_position_points, width=width_pt, height=height_pt, mask='auto')
        else:
            # Obtener el tamaño de la imagen para calcular el centro
            img = Image.open(image_path)
            img_width_mm = img.width / self.points_per_mm
            x_position_mm = (page_width_mm - img_width_mm) / 2
            x_position_points = self.mm_to_points(x_position_mm)
            can.drawImage(image_path, x_position_points, y_position_points, mask='auto')

        # Finalizar el dibujo en el canvas
        can.save()
        packet.seek(0)
        overlay_pdf = PdfReader(packet)

        # Obtener la página base del PDF y combinarla con el overlay
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number] # base_page = self.reader.getPage(page_number)

        overlay_page = overlay_pdf.pages[0]# overlay_page = overlay_pdf.getPage(0)
        base_page.merge_page(overlay_page) # base_page.mergePage(overlay_page)
        self.modified_pages[page_number] = base_page



    # def listado_alumnos_NO_includos(data):
    #     tipos_desempeño = ['Avanzado', 'Medio', 'Básico', 'Crítico']
    #     cabecera = [
    #         'DNI',
    #         'Apellido',
    #         'Nombre',
    #         'Curso',
    #         'Div.',
    #         'Cant. palabras 1° medición 2023',
    #         'Cant. palabras 3° medición 2023',
    #         'Cant. palabras 1° medición 2024',
    #         'Nivel de desempeño 2024',
    #     ]

    #     pdfs = []

    #     for curso in sorted(set(alumno['curso'] for alumno in data)):
    #         buffer = io.BytesIO()
    #         doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    #         story = []
    #         data = [cabecera]
            
    #         for desempeño in tipos_desempeño:
    #             alumnos_filtrados = [alumno for alumno in data if alumno['curso'] == curso and alumno['desempeño'] == desempeño]
    #             for alumno in alumnos_filtrados:
    #                 data.append([alumno['nombre'], alumno['curso'], alumno['desempeño']])
            
    #         t = Table(data)
    #         t.setStyle(TableStyle([
    #             ('BACKGROUND', (0,0), (-1,0), colors.grey),
    #             ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    #             ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    #             ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    #             ('BOTTOMPADDING', (0,0), (-1,0), 12),
    #             ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    #         ]))
            
    #         story.append(t)
    #         story.append(Spacer(1, 12))
    #         doc.build(story)
    #         buffer.seek(0)
    #         pdfs.append(buffer)

    #     return pdfs

    def get_table_header_and_data(self , table):
        cabecera = []
        cabecera = table[0]        
        datos = table
        # borrar la primera fila porque es la cabecera y ya la tengo
        datos.pop(0)        
        return cabecera , datos

    
    # def add_table_to_page_v2(self,  table, y_position_mm, page_number, tableStyle, column_widths_mm):
        
    #     """Añade una tabla a una página específica del PDF, centrando la tabla horizontalmente y colocándola en la posición y especificada."""
    #     # obtiene la cabecera y los datos de la tabla
    #     header , table = self.get_table_header_and_data(table)

    #     # Crear un paquete en memoria para dibujar la tabla
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)

    #     # Convertir la posición de y de milímetros a puntos
    #     y_position_points = self.mm_to_points(y_position_mm)

    #     # Convertir anchos de columna de milímetros a puntos
    #     column_widths = [self.mm_to_points(width) for width in column_widths_mm]

    #     # Ajustar los títulos de las columnas
    #     styles = getSampleStyleSheet()
    #     title_style = styles['Normal']
    #     title_style.alignment = 1  # Centrado

    #     new_header = []
    #     for col in header:
    #         header_text = "<br/>".join(col.split())
    #         new_header.append(Paragraph(header_text, title_style))

    #     table_data = [new_header] + data
    #     table = Table(table_data, colWidths=column_widths)
    #     table.setStyle(TableStyle(tableStyle))

    #     width, height = A4
    #     table_width, table_height = table.wrap(0, 0)
    #     x_position_points = (width - table_width) / 2  # Centrar horizontalmente

    #     table.drawOn(can, x_position_points, height - y_position_points - table_height)
    #     can.save()
    #     packet.seek(0)

    #     # Leer el overlay creado
    #     overlay_pdf = PdfReader(packet)

    #     # Obtener la página base del PDF y combinarla con el overlay
    #     if page_number in self.modified_pages:
    #         base_page = self.modified_pages[page_number]
    #     else:
    #         base_page = self.reader.getPage(page_number)

    #     overlay_page = overlay_pdf.getPage(0)
    #     base_page.mergePage(overlay_page)
    #     self.modified_pages[page_number] = base_page

    #     return self




    def generar_pdf_por_curso(self, curso, gradoAño, desempeño, alumnosPorDesempeño, cabecera, hoja_vacia, output_pdf_path):
        # Dimensiones de A4
        page_width, page_height = A4
        margins = 5 * mm
        usable_width = page_width - 2 * margins
        
        # Crear un documento con tamaño A4
        buffer = "temp_report.pdf"
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=margins, leftMargin=margins, topMargin=margins, bottomMargin=margins)
        elements = []
        
        # Estilo para el título arriba de la tabla
        styles = getSampleStyleSheet()
        title_superior_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Bold',
            fontSize=11,
            leading=14,
            spaceAfter=6,
            textColor=colors.Color(0/255, 15/255, 159/255)  # Cambiar color de texto
        )

        # estilo de las columnas de la tabla
        title_columns_table_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Regular',
            fontSize=10,
            leading=14,
            spaceAfter=6,
            textColor=colors.black  # Cambiar color de texto
        )
        
        title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} con desempeño {desempeño}</b>"
        
        # Calcular ancho proporcional de las columnas
        num_columns = len(cabecera)
        #column_widths = [usable_width / num_columns] * num_columns
        # Define los anchos de las columnas en milímetros
        column_widths_mm = [13, 35, 35, 14 , 18, 19.5, 19.5, 19.5 , 25 ]  # anchos en milímetros

        # Convierte milímetros a puntos
        column_widths = [width * mm for width in column_widths_mm]
        
        # Ajustando los títulos de las columnas
        new_header = []
        for header in cabecera:
            header_text = "<br/>".join(header.split())
            new_header.append(Paragraph(header_text, title_columns_table_style))

        # Método para añadir el encabezado y el espacio antes de cada tabla
        def add_table_header(elements, title_text, title_superior_style):
            elements.append(Spacer(1, 30*mm))  # Espacio antes del título
            elements.append(Paragraph(title_text, title_superior_style))
            elements.append(Spacer(1, 4*mm))  # Espacio entre título y tabla

        # Preparar los datos para la tabla, 15 filas por página
        rows_per_page = 15
        total_rows = len(alumnosPorDesempeño)
        for start in range(0, total_rows, rows_per_page):
            end = min(start + rows_per_page, total_rows)
            
            # Añadir encabezado y espacios antes de la tabla
            add_table_header(elements, title_text, title_superior_style)
            
            # Datos para la tabla actual
            page_data = [new_header] + alumnosPorDesempeño[start:end]
            table = Table(page_data, colWidths=column_widths)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.Color(157/255, 222/255, 220/255)),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Centrado vertical del título de las columnas de la tabla
                ('FONTNAME', (0, 0), (-1, 0), 'REM-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 6),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('FONTNAME', (0, 1), (-1, -1), 'REM-Regular'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            elements.append(table)
            
            # Añadir un salto de página después de cada tabla, excepto después de la última
            if end < total_rows:
                elements.append(PageBreak())
        
        # Construir el PDF
        doc.build(elements)
        
        # Leer la plantilla y el documento generado
        reader_template = PdfReader(hoja_vacia)
        reader_generated = PdfReader(buffer)
        writer = PdfWriter()
        
        # Superponer cada página del documento generado sobre una página de la plantilla
        for i in range(len(reader_generated.pages)):
            template_page = PageObject.create_blank_page(width=reader_template.pages[0].mediabox.width, height=reader_template.pages[0].mediabox.height)
            template_page.merge_page(reader_template.pages[0])
            content_page = reader_generated.pages[i]
            template_page.merge_page(content_page)
            writer.add_page(template_page)
        
        # Guardar el archivo final
        with open(output_pdf_path, "wb") as f_out:
            writer.write(f_out)
        
        #print(f"PDF generado: {output_pdf_path}")

        return output_pdf_path
    

    # def tabla_listado_grande(self, tableStyle , title_text , column_widths_mm , table , hoja_vacia, output_pdf_path):

    #     cabecera , data = self.get_table_header_and_data(table)
        
        
    #     # Dimensiones de A4 en landscape
    #     page_width, page_height = landscape(A4)
    #     margins = 5 * mm
    #     usable_width = page_width - 2 * margins
        
    #     # Crear un documento con tamaño A4 en landscape
    #     buffer = "temp_report.pdf"
    #     doc = SimpleDocTemplate(buffer, pagesize=landscape(A4), rightMargin=margins, leftMargin=margins, topMargin=margins, bottomMargin=margins)
    #     elements = []
        
    #     # Estilo para el título arriba de la tabla
    #     styles = getSampleStyleSheet()
    #     title_superior_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Bold',
    #         fontSize=11,
    #         leading=14,
    #         spaceAfter=6,
    #         textColor=colors.Color(0/255, 15/255, 159/255)  # Cambiar color de texto
    #     )

    #     # estilo de las columnas de la tabla
    #     title_columns_table_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Regular',
    #         fontSize=10,
    #         leading=14,
    #         spaceAfter=6,
    #         textColor=colors.black  # Cambiar color de texto
    #     )
        
    #     #title_text = f"<b>Listado de estudiantes de {curso} {gradoAño} con desempeño {desempeño}</b>"
        
    #     # Calcular ancho proporcional de las columnas
    #     num_columns = len(cabecera)
    #     # Define los anchos de las columnas en milímetros
    #     #column_widths_mm = [18, 55, 55, 20 , 20, 25, 25, 25 , 35 ]  # anchos en milímetros

    #     # Convierte milímetros a puntos
    #     column_widths = [width * mm for width in column_widths_mm]
        
    #     # Ajustando los títulos de las columnas
    #     new_header = []
    #     for header in cabecera:
    #         #print('el tipo de header es: ' , type(header))
    #         header_text = "<br/>".join(header.split())
    #         new_header.append(Paragraph(header_text, title_columns_table_style))

    #     # Método para añadir el encabezado y el espacio antes de cada tabla
    #     def add_table_header(elements, title_text, title_superior_style):
    #         elements.append(Spacer(1, 30*mm))  # Espacio antes del título
    #         elements.append(Paragraph(title_text, title_superior_style))
    #         elements.append(Spacer(1, 4*mm))  # Espacio entre título y tabla

    #     # Preparar los datos para la tabla, 15 filas por página
    #     rows_per_page = 15
    #     total_rows = len(data)
    #     for start in range(0, total_rows, rows_per_page):
    #         end = min(start + rows_per_page, total_rows)
            
    #         # Añadir encabezado y espacios antes de la tabla
    #         add_table_header(elements, title_text, title_superior_style)
            
    #         # Datos para la tabla actual
    #         page_data = [new_header] + data[start:end]
    #         table = Table(page_data, colWidths=column_widths)
    #         table.setStyle(TableStyle(tableStyle))
    #         elements.append(table)
            
    #         # Añadir un salto de página después de cada tabla, excepto después de la última
    #         if end < total_rows:
    #             elements.append(PageBreak())
        
    #     # Construir el PDF
    #     doc.build(elements)
        
    #     # Leer la plantilla y el documento generado
    #     reader_template = PdfReader(hoja_vacia)
    #     reader_generated = PdfReader(buffer)
    #     writer = PdfWriter()
        
    #     # Superponer cada página del documento generado sobre una página de la plantilla
    #     for i in range(len(reader_generated.pages)):
    #         template_page = PageObject.create_blank_page(width=reader_template.pages[0].mediabox.width, height=reader_template.pages[0].mediabox.height)
    #         template_page.merge_page(reader_template.pages[0])
    #         content_page = reader_generated.pages[i]
    #         template_page.merge_page(content_page)
    #         writer.add_page(template_page)
        
    #     # Guardar el archivo final
    #     with open(output_pdf_path, "wb") as f_out:
    #         writer.write(f_out)
        
    #     return output_pdf_path

    from reportlab.lib.enums import TA_CENTER

    # def tabla_listado_grande(self, tableStyle, title_text, subtitle_text, column_widths_mm, table, hoja_vacia, output_pdf_path):
    #     cabecera, data = self.get_table_header_and_data(table)

    #     # Dimensiones de A4 en landscape
    #     page_width, page_height = landscape(A4)
    #     margins = 5 * mm
    #     usable_width = page_width - 2 * margins

    #     # Crear un documento con tamaño A4 en landscape
    #     buffer = "temp_report.pdf"
    #     doc = SimpleDocTemplate(
    #         buffer, pagesize=landscape(A4),
    #         rightMargin=margins, leftMargin=margins,
    #         topMargin=margins, bottomMargin=margins
    #     )
    #     elements = []

    #     # Estilo para el título (centrado)
    #     styles = getSampleStyleSheet()
    #     title_superior_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Bold',
    #         fontSize=11,
    #         leading=14,
    #         spaceAfter=2,
    #         textColor=colors.Color(0 / 255, 15 / 255, 159 / 255),
    #         alignment=TA_CENTER  # Centrar título
    #     )

    #     # Estilo para el subtítulo (centrado)
    #     subtitle_style = ParagraphStyle(
    #         'MySubtitleStyle',
    #         parent=styles['BodyText'],
    #         fontName='REM-Regular',
    #         fontSize=10,
    #         leading=12,
    #         spaceAfter=6,
    #         textColor=colors.black,
    #         alignment=TA_CENTER  # Centrar subtítulo
    #     )

    #     # Estilo de las columnas de la tabla
    #     title_columns_table_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Regular',
    #         fontSize=10,
    #         leading=14,
    #         spaceAfter=6,
    #         textColor=colors.black
    #     )

    #     # Convertir anchos de columnas de mm a puntos
    #     column_widths = [width * mm for width in column_widths_mm]

    #     # Ajustando los títulos de las columnas
    #     new_header = [Paragraph("<br/>".join(header.split()), title_columns_table_style) for header in cabecera]

    #     # Método para añadir título y subtítulo antes de la tabla
    #     def add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style):
    #         elements.append(Spacer(1, 30 * mm))  # Espacio antes del título
    #         elements.append(Paragraph(title_text, title_superior_style))

    #         if subtitle_text:  # Si hay subtítulo, agregarlo y alinear con el título
    #             elements.append(Spacer(1, 1 * mm))  # Espacio reducido entre título y subtítulo
    #             elements.append(Paragraph(subtitle_text, subtitle_style))

    #         elements.append(Spacer(1, 4 * mm))  # Espacio entre título/subtítulo y tabla

    #     # Preparar los datos para la tabla, 15 filas por página
    #     rows_per_page = 15
    #     total_rows = len(data)
    #     for start in range(0, total_rows, rows_per_page):
    #         end = min(start + rows_per_page, total_rows)

    #         # Añadir encabezado y espacios antes de la tabla
    #         add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style)

    #         # Datos para la tabla actual
    #         page_data = [new_header] + data[start:end]
    #         table = Table(page_data, colWidths=column_widths)
    #         table.setStyle(TableStyle(tableStyle))
    #         elements.append(table)

    #         # Añadir un salto de página después de cada tabla, excepto después de la última
    #         if end < total_rows:
    #             elements.append(PageBreak())

    #     # Construir el PDF
    #     doc.build(elements)

    #     # Leer la plantilla y el documento generado
    #     reader_template = PdfReader(hoja_vacia)
    #     reader_generated = PdfReader(buffer)
    #     writer = PdfWriter()

    #     # Superponer cada página del documento generado sobre una página de la plantilla
    #     for i in range(len(reader_generated.pages)):
    #         template_page = PageObject.create_blank_page(
    #             width=reader_template.pages[0].mediabox.width,
    #             height=reader_template.pages[0].mediabox.height
    #         )
    #         template_page.merge_page(reader_template.pages[0])
    #         content_page = reader_generated.pages[i]
    #         template_page.merge_page(content_page)
    #         writer.add_page(template_page)

    #     # Guardar el archivo final
    #     with open(output_pdf_path, "wb") as f_out:
    #         writer.write(f_out)

    #     # Guardar el path generado en la instancia
    #     if not hasattr(self, "generated_pdfs"):
    #         self.generated_pdfs = []
    #     self.generated_pdfs.append(output_pdf_path)

    #     return self  # Retorna la instancia de la clase en lugar del path

    # def tabla_listado_grande_(self, tableStyle, title_text, subtitle_text, column_widths_mm, table, hoja_vacia, output_pdf_path):
    #     cabecera, data = self.get_table_header_and_data(table)

    #     # Dimensiones de A4 en landscape
    #     page_width, page_height = landscape(A4)
    #     margins = 5 * mm
    #     usable_width = page_width - 2 * margins

    #     # Crear un documento con tamaño A4 en landscape
    #     buffer = "temp_report.pdf"
    #     doc = SimpleDocTemplate(
    #         buffer, pagesize=landscape(A4),
    #         rightMargin=margins, leftMargin=margins,
    #         topMargin=margins, bottomMargin=margins
    #     )
    #     elements = []

    #     # Estilo para el título (centrado)
    #     styles = getSampleStyleSheet()
    #     title_superior_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Bold',
    #         fontSize=11,
    #         leading=14,
    #         spaceAfter=2,
    #         textColor=colors.Color(0/255, 15/255, 159/255),
    #         alignment=TA_CENTER  # Centrar título
    #     )

    #     # Estilo para el subtítulo (centrado)
    #     subtitle_style = ParagraphStyle(
    #         'MySubtitleStyle',
    #         parent=styles['BodyText'],
    #         fontName='REM-Regular',
    #         fontSize=10,
    #         leading=12,
    #         spaceAfter=6,
    #         textColor=colors.black,
    #         alignment=TA_CENTER  # Centrar subtítulo
    #     )

    #     # Estilo de las columnas de la tabla
    #     title_columns_table_style = ParagraphStyle(
    #         'MyTitleStyle',
    #         parent=styles['Title'],
    #         fontName='REM-Regular',
    #         fontSize=10,
    #         leading=14,
    #         spaceAfter=6,
    #         textColor=colors.black
    #     )

    #     # Convertir anchos de columnas de mm a puntos
    #     column_widths = [width * mm for width in column_widths_mm]

    #     # Ajustando los títulos de las columnas
    #     new_header = [Paragraph("<br/>".join(header.split()), title_columns_table_style) for header in cabecera]

    #     # Método para añadir título y subtítulo antes de la tabla
    #     def add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style):
    #         elements.append(Spacer(1, 30 * mm))  # Espacio antes del título
    #         elements.append(Paragraph(title_text, title_superior_style))

    #         if subtitle_text:  # Si hay subtítulo, agregarlo y alinear con el título
    #             elements.append(Spacer(1, 1 * mm))  # Espacio reducido entre título y subtítulo
    #             elements.append(Paragraph(subtitle_text, subtitle_style))

    #         elements.append(Spacer(1, 4 * mm))  # Espacio entre título/subtítulo y tabla

    #     # Preparar los datos para la tabla, 15 filas por página
    #     rows_per_page = 15
    #     total_rows = len(data)
    #     for start in range(0, total_rows, rows_per_page):
    #         end = min(start + rows_per_page, total_rows)

    #         # Añadir encabezado y espacios antes de la tabla
    #         add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style)

    #         # Datos para la tabla actual
    #         page_data = [new_header] + data[start:end]
    #         table = Table(page_data, colWidths=column_widths)
    #         table.setStyle(TableStyle(tableStyle))
    #         elements.append(table)

    #         # Añadir un salto de página después de cada tabla, excepto después de la última
    #         if end < total_rows:
    #             elements.append(PageBreak())

    #     # Construir el PDF
    #     doc.build(elements)

    #     # Leer la plantilla y el documento generado
    #     reader_template = PdfReader(hoja_vacia)
    #     reader_generated = PdfReader(buffer)
    #     writer = PdfWriter()

    #     # Superponer cada página del documento generado sobre una página de la plantilla
    #     for i in range(len(reader_generated.pages)):
    #         template_page = PageObject.create_blank_page(
    #             width=reader_template.pages[0].mediabox.width,
    #             height=reader_template.pages[0].mediabox.height
    #         )
    #         template_page.merge_page(reader_template.pages[0])
    #         content_page = reader_generated.pages[i]
    #         template_page.merge_page(content_page)
    #         writer.add_page(template_page)

    #     # Guardar el archivo final
    #     with open(output_pdf_path, "wb") as f_out:
    #         writer.write(f_out)

    #     # Guardar las páginas generadas en self.modified_pages para que se pueda usar en merge_pdfs_in_memory
    #     self.modified_pages = {i: writer.pages[i] for i in range(len(writer.pages))}

    #     return self  # Devuelve la instancia de la clase PDFEditor en lugar de la ruta del PDF






    def tabla_listado_grande_bien(self, tableStyle, title_text, subtitle_text, column_widths_mm, table, hoja_vacia, output_pdf_path):
        """
        Genera una tabla dentro de un PDF y crea tantas páginas como sean necesarias.
        Muestra cuántas páginas se generaron.

        Args:
            tableStyle (list): Estilo de la tabla.
            title_text (str): Título del reporte.
            subtitle_text (str): Subtítulo del reporte.
            column_widths_mm (list): Lista con los anchos de las columnas en milímetros.
            table (list): Datos de la tabla.
            hoja_vacia (str): Ruta de la hoja vacía utilizada como plantilla.
            output_pdf_path (str): Ruta donde se guardará el archivo PDF generado.

        Returns:
            self: Devuelve la instancia de la clase PDFEditor.
        """
        cabecera, data = self.get_table_header_and_data(table)

        # Dimensiones de A4 en landscape
        page_width, page_height = landscape(A4)
        margins = 5 * mm
        usable_width = page_width - 2 * margins

        # Crear un documento temporal
        buffer = "temp_report.pdf"
        doc = SimpleDocTemplate(
            buffer, pagesize=landscape(A4),
            rightMargin=margins, leftMargin=margins,
            topMargin=margins, bottomMargin=margins
        )
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_superior_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Bold',
            fontSize=11,
            leading=14,
            spaceAfter=2,
            textColor=colors.Color(0/255, 15/255, 159/255),
            alignment=TA_CENTER
        )

        subtitle_style = ParagraphStyle(
            'MySubtitleStyle',
            parent=styles['BodyText'],
            fontName='REM-Regular',
            fontSize=10,
            leading=12,
            spaceAfter=6,
            textColor=colors.black,
            alignment=TA_CENTER
        )

        title_columns_table_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Regular',
            fontSize=10,
            leading=14,
            spaceAfter=6,
            textColor=colors.black
        )

        # Convertir anchos de columnas de mm a puntos
        column_widths = [width * mm for width in column_widths_mm]

        # Ajustando los títulos de las columnas
        new_header = [Paragraph("<br/>".join(header.split()), title_columns_table_style) for header in cabecera]

        # Método para añadir título y subtítulo antes de la tabla
        def add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style):
            elements.append(Spacer(1, 30 * mm))
            elements.append(Paragraph(title_text, title_superior_style))

            if subtitle_text:
                elements.append(Spacer(1, 1 * mm))
                elements.append(Paragraph(subtitle_text, subtitle_style))

            elements.append(Spacer(1, 4 * mm))

        # Preparar los datos para la tabla, 15 filas por página
        rows_per_page = 15
        total_rows = len(data)
        total_pages = 0  # Contador de páginas generadas

        for start in range(0, total_rows, rows_per_page):
            end = min(start + rows_per_page, total_rows)
            total_pages += 1  # Incrementar el contador de páginas

            add_table_header(elements, title_text, subtitle_text, title_superior_style, subtitle_style)

            # Datos para la tabla actual
            page_data = [new_header] + data[start:end]
            table = Table(page_data, colWidths=column_widths)
            table.setStyle(TableStyle(tableStyle))
            elements.append(table)

            if end < total_rows:
                elements.append(PageBreak())

        # Construir el PDF
        doc.build(elements)

        # Leer la plantilla y el documento generado
        reader_template = PdfReader(hoja_vacia)
        reader_generated = PdfReader(buffer)
        writer = PdfWriter()

        # Superponer cada página del documento generado sobre una página de la plantilla
        for i in range(len(reader_generated.pages)):
            template_page = PageObject.create_blank_page(
                width=reader_template.pages[0].mediabox.width,
                height=reader_template.pages[0].mediabox.height
            )
            template_page.merge_page(reader_template.pages[0])
            content_page = reader_generated.pages[i]
            template_page.merge_page(content_page)
            writer.add_page(template_page)

        # Guardar el archivo final
        with open(output_pdf_path, "wb") as f_out:
            writer.write(f_out)

        # Guardar las páginas generadas en self.modified_pages
        self.modified_pages = {i: writer.pages[i] for i in range(len(writer.pages))}

        # Mostrar mensaje con la cantidad de páginas generadas
        print(f"✅ Se generaron {total_pages} páginas en {output_pdf_path}")

        return self  # Devuelve la instancia de la clase PDFEditor

    def tabla_listado_grande_mal_mal(self, tableStyle, title_text, subtitle_text, column_widths_mm, table, hoja_vacia):
        """
        Genera una tabla dentro de un PDF y crea tantas páginas como sean necesarias.
        Retorna un objeto BytesIO con el contenido del PDF en memoria.
        """
        cabecera, data = self.get_table_header_and_data(table)

        # Dimensiones de A4 en landscape
        page_width, page_height = landscape(A4)
        margins = 5 * mm

        # Crear un buffer en memoria
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer, pagesize=landscape(A4),
            rightMargin=margins, leftMargin=margins,
            topMargin=margins, bottomMargin=margins
        )
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_superior_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Bold',
            fontSize=11,
            leading=14,
            spaceAfter=2,
            textColor=colors.Color(0/255, 15/255, 159/255),
            alignment=1  # TA_CENTER
        )

        subtitle_style = ParagraphStyle(
            'MySubtitleStyle',
            parent=styles['BodyText'],
            fontName='REM-Regular',
            fontSize=10,
            leading=12,
            spaceAfter=6,
            textColor=colors.black,
            alignment=1  # TA_CENTER
        )

        title_columns_table_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Regular',
            fontSize=10,
            leading=14,
            spaceAfter=6,
            textColor=colors.black
        )

        # Convertir anchos de columnas de mm a puntos
        column_widths = [width * mm for width in column_widths_mm]

        # Ajustando los títulos de las columnas
        new_header = [Paragraph("<br/>".join(header.split()), title_columns_table_style) for header in cabecera]

        # Método para añadir título y subtítulo antes de la tabla
        def add_table_header(elements, title_text, subtitle_text):
            elements.append(Spacer(1, 30 * mm))
            elements.append(Paragraph(title_text, title_superior_style))
            if subtitle_text:
                elements.append(Spacer(1, 1 * mm))
                elements.append(Paragraph(subtitle_text, subtitle_style))
            elements.append(Spacer(1, 4 * mm))

        # Preparar los datos para la tabla, 15 filas por página
        rows_per_page = 15
        total_rows = len(data)
        total_pages = 0

        for start in range(0, total_rows, rows_per_page):
            end = min(start + rows_per_page, total_rows)
            total_pages += 1

            add_table_header(elements, title_text, subtitle_text)
            page_data = [new_header] + data[start:end]
            table = Table(page_data, colWidths=column_widths)
            table.setStyle(TableStyle(tableStyle))
            elements.append(table)

            if end < total_rows:
                elements.append(PageBreak())

        # Construir el PDF en memoria
        doc.build(elements)
        buffer.seek(0)

        # Leer la plantilla y el documento generado
        reader_template = PdfReader(hoja_vacia)
        reader_generated = PdfReader(buffer)
        writer = PdfWriter()

        # Superponer cada página del documento generado sobre una página de la plantilla
        for i in range(len(reader_generated.pages)):
            template_page = reader_template.pages[0]
            content_page = reader_generated.pages[i]
            template_page.merge_page(content_page)
            writer.add_page(template_page)

        # Guardar en un nuevo buffer
        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)

        # Mostrar mensaje con la cantidad de páginas generadas
        print(f"✅ Se generaron {total_pages} páginas en memoria")

        return output_buffer  # Devuelve el PDF en memoria

    def tabla_listado_grande_OK(self, tableStyle, title_text, subtitle_text, column_widths_mm, table, hoja_vacia):
        """
        Genera una tabla dentro de un PDF y crea tantas páginas como sean necesarias.
        Retorna un objeto BytesIO con el contenido del PDF en memoria.
        """
        cabecera, data = self.get_table_header_and_data(table)

        # Dimensiones de A4 en landscape
        page_width, page_height = landscape(A4)
        margins = 5 * mm
        usable_width = page_width - 2 * margins

        # Crear un buffer en memoria
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer, pagesize=landscape(A4),
            rightMargin=margins, leftMargin=margins,
            topMargin=margins, bottomMargin=margins
        )
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_superior_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Bold',
            fontSize=11,
            leading=14,
            spaceAfter=2,
            textColor=colors.Color(0/255, 15/255, 159/255),
            alignment=TA_CENTER
        )

        subtitle_style = ParagraphStyle(
            'MySubtitleStyle',
            parent=styles['BodyText'],
            fontName='REM-Regular',
            fontSize=10,
            leading=12,
            spaceAfter=6,
            textColor=colors.black,
            alignment=TA_CENTER
        )

        title_columns_table_style = ParagraphStyle(
            'MyTitleStyle',
            parent=styles['Title'],
            fontName='REM-Regular',
            fontSize=10,
            leading=14,
            spaceAfter=6,
            textColor=colors.black
        )

        # Convertir anchos de columnas de mm a puntos
        column_widths = [width * mm for width in column_widths_mm]

        # Ajustando los títulos de las columnas
        new_header = [Paragraph("<br/>".join(header.split()), title_columns_table_style) for header in cabecera]

        # Método para añadir título y subtítulo antes de la tabla
        def add_table_header(elements, title_text, subtitle_text):
            elements.append(Spacer(1, 30 * mm))
            elements.append(Paragraph(title_text, title_superior_style))
            if subtitle_text:
                elements.append(Spacer(1, 1 * mm))
                elements.append(Paragraph(subtitle_text, subtitle_style))
            elements.append(Spacer(1, 4 * mm))

        # Preparar los datos para la tabla, 15 filas por página
        rows_per_page = 15
        total_rows = len(data)
        total_pages = 0

        for start in range(0, total_rows, rows_per_page):
            end = min(start + rows_per_page, total_rows)
            total_pages += 1

            add_table_header(elements, title_text, subtitle_text)
            page_data = [new_header] + data[start:end]
            table = Table(page_data, colWidths=column_widths)
            table.setStyle(TableStyle(tableStyle))
            elements.append(table)

            if end < total_rows:
                elements.append(PageBreak())

        # Construir el PDF en memoria
        doc.build(elements)
        buffer.seek(0)

        # Leer la plantilla y el documento generado
        reader_template = PdfReader(hoja_vacia)
        reader_generated = PdfReader(buffer)
        writer = PdfWriter()

        # Superponer cada página del documento generado sobre una página de la plantilla
        for i in range(len(reader_generated.pages)):
            template_page = PageObject.create_blank_page(
                width=reader_template.pages[0].mediabox.width,
                height=reader_template.pages[0].mediabox.height
            )
            template_page.merge_page(reader_template.pages[0])
            content_page = reader_generated.pages[i]
            template_page.merge_page(content_page)
            writer.add_page(template_page)

        # Guardar en un nuevo buffer
        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)

        # Mostrar mensaje con la cantidad de páginas generadas
        print(f"✅ Se generaron {total_pages} páginas en memoria")

        return output_buffer  # Devuelve el PDF en memoria
    
    def tabla_listado_grande_OK_2(self, tableStyle, title_text, subtitle_text, column_widths_mm, table_data, hoja_vacia,posicion_y_tabla_mm=20 ):
        """
        Genera un PDF con encabezado complejo y múltiples páginas si hay muchas filas.
        """

        # Dimensiones de A4 en landscape
        page_width, page_height = landscape(A4)
        margins = 5 * mm
        usable_width = page_width - 2 * margins

        # Crear un buffer en memoria
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer, pagesize=landscape(A4),
            rightMargin=margins, leftMargin=margins,
            topMargin=margins, bottomMargin=margins
        )
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Title'],
            fontName='Helvetica-Bold',
            fontSize=11,
            leading=14,
            spaceAfter=2,
            textColor=colors.Color(0/255, 15/255, 159/255),
            alignment=TA_CENTER
        )
        subtitle_style = ParagraphStyle(
            'SubtitleStyle',
            parent=styles['BodyText'],
            fontName='Helvetica',
            fontSize=10,
            leading=12,
            spaceAfter=6,
            textColor=colors.black,
            alignment=TA_CENTER
        )
        cell_style = ParagraphStyle(
            'CellStyle',
            fontName='Helvetica',
            fontSize=8,
            alignment=TA_CENTER
        )

        column_widths = [w * mm for w in column_widths_mm]

        # Construcción de encabezado multinivel
        header_data = [
            [
                Paragraph('DNI', cell_style), 
                Paragraph('APELLIDO', cell_style), 
                Paragraph('NOMBRE', cell_style),
                Paragraph('ÁLGEBRA Y FUNCIONES', cell_style), '', '',
                Paragraph('GEOMETRÍA Y MEDIDA', cell_style), '',
                Paragraph('NÚMEROS Y OPERACIONES', cell_style), '',
                Paragraph('TOTAL GENERAL', cell_style)
            ],
            [
                '', '', '',
                Paragraph('A) Reconocimiento de datos y conceptos', cell_style),
                Paragraph('B) Resolución de operaciones', cell_style),
                Paragraph('C) Comprensión de datos y conceptos', cell_style),
                Paragraph('C) Comprensión de datos y conceptos', cell_style),
                Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', cell_style),
                Paragraph('B) Resolución de operaciones', cell_style),
                Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', cell_style),
                ''
            ]
        ]

        # Aplicar estilos de combinación de celdas
        spans = [
            ('SPAN', (0, 0), (0, 1)),  # DNI
            ('SPAN', (1, 0), (1, 1)),  # APELLIDO
            ('SPAN', (2, 0), (2, 1)),  # NOMBRE
            ('SPAN', (3, 0), (5, 0)),  # ÁLGEBRA
            ('SPAN', (6, 0), (7, 0)),  # GEOMETRÍA
            ('SPAN', (8, 0), (9, 0)),  # NÚMEROS
            ('SPAN', (10, 0), (10, 1)),  # TOTAL GENERAL
        ]

        # 🔍 Filtrar filas completamente vacías antes de paginar
        #table_data = [fila for fila in table_data if any(str(celda).strip() for celda in fila)]
        
        # 1. Eliminar la primera fila si es cabecera duplicada
        #if table_data and table_data[0][0] == 'DNI':
        table_data = table_data[1:]

        # 2. Filtrar filas completamente vacías
        table_data = [fila for fila in table_data if any(str(celda).strip() for celda in fila)]
        
        #print(table_data[0])

        # Datos
        rows_per_page = 15
        total_rows = len(table_data)
        total_pages = 0

        for start in range(0, total_rows, rows_per_page):
            end = min(start + rows_per_page, total_rows)
            page_data = header_data + table_data[start:end]
            total_pages += 1

            # Título y subtítulo
            #elements.append(Spacer(1, 20))
            elements.append(Spacer(1, posicion_y_tabla_mm * mm))
            elements.append(Paragraph(title_text, title_style))
            if subtitle_text:
                elements.append(Spacer(1, 5))
                elements.append(Paragraph(subtitle_text, subtitle_style))
            elements.append(Spacer(1, 5))

            table = Table(page_data, colWidths=column_widths, repeatRows=2)
            style = TableStyle(tableStyle + spans)
            table.setStyle(style)
            elements.append(table)

            if end < total_rows:
                elements.append(PageBreak())

        doc.build(elements)
        buffer.seek(0)

        # Combinar con hoja vacía
        reader_template = PdfReader(hoja_vacia)
        reader_generated = PdfReader(buffer)
        writer = PdfWriter()

        for i in range(len(reader_generated.pages)):
            template_page = PageObject.create_blank_page(
                width=reader_template.pages[0].mediabox.width,
                height=reader_template.pages[0].mediabox.height
            )
            template_page.merge_page(reader_template.pages[0])
            content_page = reader_generated.pages[i]
            template_page.merge_page(content_page)
            writer.add_page(template_page)

        output_buffer = io.BytesIO()
        writer.write(output_buffer)
        output_buffer.seek(0)

        print(f"✅ Se generaron {total_pages} páginas con encabezado complejo")
        return output_buffer

    
    # def tabla_listado_grande_OK_2(self, tableStyle, title_text, subtitle_text, column_widths_mm, table_data, hoja_vacia):
    #     """
    #     Genera un PDF con encabezado complejo y múltiples páginas si hay muchas filas.
    #     """
        
        
    #     # Dimensiones de A4 en landscape
    #     page_width, page_height = landscape(A4)
    #     margins = 5 * mm
    #     usable_width = page_width - 2 * margins

    #     # Crear un buffer en memoria
    #     buffer = io.BytesIO()
    #     doc = SimpleDocTemplate(
    #         buffer, pagesize=landscape(A4),
    #         rightMargin=margins, leftMargin=margins,
    #         topMargin=margins, bottomMargin=margins
    #     )
    #     elements = []

    #     # Estilos
    #     styles = getSampleStyleSheet()
    #     title_style = ParagraphStyle(
    #         'TitleStyle',
    #         parent=styles['Title'],
    #         fontName='Helvetica-Bold',
    #         fontSize=11,
    #         leading=14,
    #         spaceAfter=2,
    #         textColor=colors.Color(0/255, 15/255, 159/255),
    #         alignment=TA_CENTER
    #     )
    #     subtitle_style = ParagraphStyle(
    #         'SubtitleStyle',
    #         parent=styles['BodyText'],
    #         fontName='Helvetica',
    #         fontSize=10,
    #         leading=12,
    #         spaceAfter=6,
    #         textColor=colors.black,
    #         alignment=TA_CENTER
    #     )
    #     cell_style = ParagraphStyle(
    #         'CellStyle',
    #         fontName='Helvetica',
    #         fontSize=8,
    #         alignment=TA_CENTER
    #     )

    #     column_widths = [w * mm for w in column_widths_mm]

    #     # Construcción de encabezado multinivel
    #     header_data = [
    #         [
    #             Paragraph('DNI', cell_style), 
    #             Paragraph('APELLIDO', cell_style), 
    #             Paragraph('NOMBRE', cell_style),
    #             Paragraph('ÁLGEBRA Y FUNCIONES', cell_style), '', '',
    #             Paragraph('GEOMETRÍA Y MEDIDA', cell_style), '',
    #             Paragraph('NÚMEROS Y OPERACIONES', cell_style), '',
    #             Paragraph('TOTAL GENERAL', cell_style)
    #         ],
    #         [
    #             '', '', '',
    #             Paragraph('A) Reconocimiento de datos y conceptos', cell_style),
    #             Paragraph('B) Resolución de operaciones', cell_style),
    #             Paragraph('C) Comprensión de datos y conceptos', cell_style),
    #             Paragraph('C) Comprensión de datos y conceptos', cell_style),
    #             Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', cell_style),
    #             Paragraph('B) Resolución de operaciones', cell_style),
    #             Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', cell_style),
    #             ''
    #         ],
    #         # [
    #         #     '', '', '',
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     Paragraph('<i>4 ítems</i>', cell_style),
    #         #     Paragraph('<i>2 ítems</i>', cell_style),
    #         #     ''
    #         # ]
    #     ]

    #     # Aplicar estilos de combinación de celdas
    #     spans = [
    #         ('SPAN', (0, 0), (0, 2)),  # DNI
    #         ('SPAN', (1, 0), (1, 2)),  # APELLIDO
    #         ('SPAN', (2, 0), (2, 2)),  # NOMBRE
    #         ('SPAN', (3, 0), (5, 0)),  # ÁLGEBRA
    #         ('SPAN', (6, 0), (7, 0)),  # GEOMETRÍA
    #         ('SPAN', (8, 0), (9, 0)),  # NÚMEROS
    #         ('SPAN', (10, 0), (10, 2)),  # TOTAL GENERAL
    #     ]

    #     # Datos
    #     rows_per_page = 15
    #     total_rows = len(table_data)
    #     total_pages = 0

    #     for start in range(0, total_rows, rows_per_page):
    #         end = min(start + rows_per_page, total_rows)
    #         page_data = header_data + table_data[start:end]
    #         total_pages += 1

    #         # Título y subtítulo
    #         elements.append(Spacer(1, 20))
    #         elements.append(Paragraph(title_text, title_style))
    #         if subtitle_text:
    #             elements.append(Spacer(1, 5))
    #             elements.append(Paragraph(subtitle_text, subtitle_style))
    #         elements.append(Spacer(1, 5))

    #         table = Table(page_data, colWidths=column_widths, repeatRows=2)
    #         style = TableStyle(tableStyle + spans)
    #         table.setStyle(style)
    #         elements.append(table)

    #         if end < total_rows:
    #             elements.append(PageBreak())

    #     doc.build(elements)
    #     buffer.seek(0)

    #     # Combinar con hoja vacía
    #     reader_template = PdfReader(hoja_vacia)
    #     reader_generated = PdfReader(buffer)
    #     writer = PdfWriter()

    #     for i in range(len(reader_generated.pages)):
    #         template_page = PageObject.create_blank_page(
    #             width=reader_template.pages[0].mediabox.width,
    #             height=reader_template.pages[0].mediabox.height
    #         )
    #         template_page.merge_page(reader_template.pages[0])
    #         content_page = reader_generated.pages[i]
    #         template_page.merge_page(content_page)
    #         writer.add_page(template_page)

    #     output_buffer = io.BytesIO()
    #     writer.write(output_buffer)
    #     output_buffer.seek(0)
        
        

    #     print(f"✅ Se generaron {total_pages} páginas con encabezado complejo")
    #     return output_buffer
    
    # # # # def tabla_listado_grande_OK_2(self,tableStyle, title_text, subtitle_text, column_widths_mm, table_data, hoja_vacia):
    # # # #     page_width, page_height = landscape(A4)
    # # # #     margins = 5 * mm

    # # # #     buffer = io.BytesIO()
    # # # #     doc = SimpleDocTemplate(
    # # # #         buffer, pagesize=landscape(A4),
    # # # #         rightMargin=margins, leftMargin=margins,
    # # # #         topMargin=margins, bottomMargin=margins
    # # # #     )
    # # # #     elements = []

    # # # #     styles = getSampleStyleSheet()
    # # # #     title_superior_style = ParagraphStyle(
    # # # #         'MyTitleStyle',
    # # # #         parent=styles['Title'],
    # # # #         fontName='Helvetica-Bold',
    # # # #         fontSize=11,
    # # # #         leading=14,
    # # # #         spaceAfter=2,
    # # # #         textColor=colors.Color(0/255, 15/255, 159/255),
    # # # #         alignment=TA_CENTER
    # # # #     )
    # # # #     subtitle_style = ParagraphStyle(
    # # # #         'MySubtitleStyle',
    # # # #         parent=styles['BodyText'],
    # # # #         fontName='Helvetica',
    # # # #         fontSize=10,
    # # # #         leading=12,
    # # # #         spaceAfter=6,
    # # # #         textColor=colors.black,
    # # # #         alignment=TA_CENTER
    # # # #     )
    # # # #     header_style = ParagraphStyle(
    # # # #         'HeaderStyle',
    # # # #         parent=styles['Normal'],
    # # # #         fontName='Helvetica-Bold',
    # # # #         fontSize=7,
    # # # #         alignment=TA_CENTER
    # # # #     )
    # # # #     subheader_style = ParagraphStyle(
    # # # #         'SubHeaderStyle',
    # # # #         parent=styles['Normal'],
    # # # #         fontName='Helvetica',
    # # # #         fontSize=6,
    # # # #         alignment=TA_CENTER
    # # # #     )

    # # # #     col_widths = [w * mm for w in column_widths_mm]

    # # # #     # Crear encabezado complejo
    # # # #     header_row1 = [
    # # # #         Paragraph('DNI', header_style),
    # # # #         Paragraph('APELLIDO', header_style),
    # # # #         Paragraph('NOMBRE', header_style),
    # # # #         Paragraph('ÁLGEBRA Y FUNCIONES', header_style), '', '',
    # # # #         Paragraph('GEOMETRÍA Y MEDIDA', header_style), '',
    # # # #         Paragraph('NÚMEROS Y OPERACIONES', header_style), '',
    # # # #         Paragraph('TOTAL<br/>GENERAL', header_style)
    # # # #     ]
    # # # #     header_row2 = [
    # # # #         '', '', '',
    # # # #         Paragraph('A) Reconocimiento de datos y conceptos', subheader_style),
    # # # #         Paragraph('B) Resolución de operaciones', subheader_style),
    # # # #         Paragraph('C) Comprensión de datos y conceptos', subheader_style),
    # # # #         Paragraph('C) Comprensión de datos y conceptos', subheader_style),
    # # # #         Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', subheader_style),
    # # # #         Paragraph('B) Resolución de operaciones', subheader_style),
    # # # #         Paragraph('D) Resolución de situaciones en contexto intra/extra matemático', subheader_style),
    # # # #         ''
    # # # #     ]
        
    # # # #     # Aplicar estilos de combinación de celdas
    # # # #     spans = [
    # # # #         ('SPAN', (0, 0), (0, 2)),  # DNI
    # # # #         ('SPAN', (1, 0), (1, 2)),  # APELLIDO
    # # # #         ('SPAN', (2, 0), (2, 2)),  # NOMBRE
    # # # #         ('SPAN', (3, 0), (5, 0)),  # ÁLGEBRA
    # # # #         ('SPAN', (6, 0), (7, 0)),  # GEOMETRÍA
    # # # #         ('SPAN', (8, 0), (9, 0)),  # NÚMEROS
    # # # #         ('SPAN', (10, 0), (10, 2)),  # TOTAL GENERAL
    # # # #     ]

    # # # #     rows_per_page = 15
    # # # #     total_rows = len(table_data)
    # # # #     total_pages = 0

    # # # #     for start in range(0, total_rows, rows_per_page):
    # # # #         end = min(start + rows_per_page, total_rows)
    # # # #         page_data = header_data + table_data[start:end]
    # # # #         total_pages += 1

    # # # #         # Título y subtítulo
    # # # #         elements.append(Spacer(1, 20))
    # # # #         elements.append(Paragraph(title_text, title_style))
    # # # #         if subtitle_text:
    # # # #             elements.append(Spacer(1, 5))
    # # # #             elements.append(Paragraph(subtitle_text, subtitle_style))
    # # # #         elements.append(Spacer(1, 5))

    # # # #         table = Table(page_data, colWidths=column_widths, repeatRows=3)
    # # # #         style = TableStyle(tableStyle + spans)
    # # # #         table.setStyle(style)
    # # # #         elements.append(table)

    # # # #         if end < total_rows:
    # # # #             elements.append(PageBreak())

    # # # #     doc.build(elements)
    # # # #     buffer.seek(0)

    # # # #     # Superponer sobre plantilla PDF (opcional si se pasa hoja_vacia)
    # # # #     output_buffer = io.BytesIO()
    # # # #     if hoja_vacia:
    # # # #         reader_template = PdfReader(hoja_vacia)
    # # # #         reader_generated = PdfReader(buffer)
    # # # #         writer = PdfWriter()

    # # # #         for i in range(len(reader_generated.pages)):
    # # # #             template_page = PageObject.create_blank_page(
    # # # #                 width=reader_template.pages[0].mediabox.width,
    # # # #                 height=reader_template.pages[0].mediabox.height
    # # # #             )
    # # # #             template_page.merge_page(reader_template.pages[0])
    # # # #             content_page = reader_generated.pages[i]
    # # # #             template_page.merge_page(content_page)
    # # # #             writer.add_page(template_page)
    # # # #         writer.write(output_buffer)
    # # # #         output_buffer.seek(0)
    # # # #         return output_buffer
    # # # #     else:
    # # # #         return buffer




    
    def merge_pdfs(self,paths, output_path):
        """
        Combina varios archivos PDF en un solo archivo.

        Args:
            paths (list): Lista de rutas de archivos PDF a combinar.
            output_path (str): Ruta del archivo PDF de salida.
        """
        writer = PdfWriter()

        for path in paths:
            reader = PdfReader(path)
            for page in reader.pages:
                writer.add_page(page)

        # El error podría provenir de cómo manejas el archivo de salida.
        # Asegúrate de que 'output_path' es una cadena que representa la ruta del archivo de salida.
        with open(output_path, 'wb') as f:
            writer.write(f)

    

    
    @staticmethod
    def calculate_column_widths(num_columns, first_column_width_mm, total_width_mm):
        """Calcula los anchos de las columnas asignando un ancho fijo a la primera columna y distribuyendo el resto entre las demás."""
        first_column_width_points = first_column_width_mm * mm
        remaining_width_points = (total_width_mm - first_column_width_mm) * mm
        other_column_width_points = remaining_width_points / (num_columns - 1)

        column_widths = [first_column_width_points] + [other_column_width_points] * (num_columns - 1)
        return column_widths
    
    @staticmethod
    def mm_to_points_(mm_value):
        return mm_value * mm  # ReportLab already provides this conversion
    
    
    def add_table_to_page_v2(
        self,
        table,
        y_position_mm,
        page_number,
        tableStyle,
        fontName='Helvetica',
        fontSize=6,
        col_widths_=[],
        center_title=True,  # Nuevo parámetro
        max_col_width_mm=40  # Nuevo parámetro para controlar ancho máximo en mm
    ):
        """Añade una tabla a una página específica del PDF, con control de título centrado y ajuste automático de columnas anchas."""

        def wrap_header_text(col, fontName, fontSize, max_col_width_points):
            # Si el texto entero cabe, devolverlo entero
            full_width = stringWidth(col, fontName, fontSize)
            if full_width <= max_col_width_points:
                return col

            # Si no cabe, intentar dividir en 2 líneas de forma balanceada
            words = col.split()
            if len(words) == 1:
                return col  # No se puede partir

            # Intentar distintas posiciones de corte
            best_split = col
            min_max_line_width = float('inf')

            for split_idx in range(1, len(words)):
                line1 = " ".join(words[:split_idx])
                line2 = " ".join(words[split_idx:])
                line1_width = stringWidth(line1, fontName, fontSize)
                line2_width = stringWidth(line2, fontName, fontSize)
                max_line_width = max(line1_width, line2_width)

                if max_line_width <= max_col_width_points and max_line_width < min_max_line_width:
                    best_split = line1 + "<br/>" + line2
                    min_max_line_width = max_line_width

            return best_split

        # ---------------------------
        # Resto de tu función normal:
        # ---------------------------

        header, data = self.get_table_header_and_data(table)

        # Crear un paquete en memoria para dibujar la tabla
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        # Convertir la posición de y de milímetros a puntos
        y_position_points = self.mm_to_points_(y_position_mm)

        # Estilo del título de las columnas
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            name='TitleStyle',
            parent=styles['Normal'],
            alignment=1 if center_title else 0,  # Centrado o no
            fontName='REM-Bold',
            fontSize=fontSize,
            textColor=colors.whitesmoke,
            backColor=colors.Color(49 / 255, 122 / 255, 138 / 255)
        )

        # Conversión de mm a puntos para el ancho máximo
        max_col_width_points = self.mm_to_points_(max_col_width_mm)

        # Preparar encabezados con formato (con ajuste automático de líneas mejorado)
        new_header = []
        for col in header:
            header_text = wrap_header_text(col, fontName, fontSize, max_col_width_points)
            new_header.append(Paragraph(header_text, title_style))

        table_data = [new_header] + data

        # Calcular ancho máximo por columna (en puntos)
        num_columns = len(header)
        column_widths = col_widths_ if col_widths_ else [0] * num_columns

        for row in table_data:
            for i, cell in enumerate(row):
                if isinstance(cell, Paragraph):
                    text = cell.text
                else:
                    text = str(cell)

                # Aumentamos el padding a 30 puntos
                cell_width = stringWidth(text, fontName, fontSize) + 30
                if cell_width > column_widths[i]:
                    column_widths[i] = cell_width

        # Crear la tabla
        table = Table(table_data, colWidths=column_widths)
        table.setStyle(TableStyle(tableStyle))

        width, height = A4
        table_width, table_height = table.wrap(0, 0)
        x_position_points = (width - table_width) / 2  # Centrado horizontal

        # Dibujar tabla
        table.drawOn(can, x_position_points, height - y_position_points - table_height)
        can.save()
        packet.seek(0)

        # Leer overlay creado
        overlay_pdf = PdfReader(packet)

        # Obtener página base y combinar con overlay
        if page_number in self.modified_pages:
            base_page = self.modified_pages[page_number]
        else:
            base_page = self.reader.pages[page_number]

        overlay_page = overlay_pdf.pages[0]
        base_page.merge_page(overlay_page)
        self.modified_pages[page_number] = base_page

        return self

    # def add_table_to_page_v3(
    #     self,
    #     table,
    #     y_position_mm,
    #     page_number,
    #     tableStyle,
    #     col_widths_=[],
    #     center_title=True,
    #     max_col_width_mm=40
    # ):
    #     """Añade una tabla a una página específica del PDF respetando completamente el estilo de `tableStyle`."""

    #     def wrap_text_auto(col, fontName, fontSize, max_width):
    #         """Ajusta el texto para que no supere el ancho máximo permitido, insertando saltos de línea."""
    #         width = stringWidth(col, fontName, fontSize)
    #         if width <= max_width:
    #             return col
    #         words = col.split()
    #         if len(words) == 1:
    #             return col
    #         best_split = col
    #         min_max_line_width = float('inf')
    #         for split_idx in range(1, len(words)):
    #             line1 = " ".join(words[:split_idx])
    #             line2 = " ".join(words[split_idx:])
    #             max_width_ = max(stringWidth(line1, fontName, fontSize), stringWidth(line2, fontName, fontSize))
    #             if max_width_ <= max_col_width_mm and max_width_ < min_max_line_width:
    #                 best_split = line1 + "<br/>" + line2
    #                 min_max_line_width = max_width_
    #         return best_split

    #     header, data = self.get_table_header_and_data(table)

    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)

    #     y_position_points = self.mm_to_points_(y_position_mm)
    #     max_col_width_points = self.mm_to_points_(max_col_width_mm)

    #     # Extraer estilo del encabezado desde tableStyle (si existe)
    #     font_name_header = 'Helvetica-Bold'
    #     font_size_header = 10
    #     text_color_header = colors.black

    #     for cmd in tableStyle:
    #         if cmd[0] == 'FONTNAME' and cmd[1] == (0, 0):
    #             font_name_header = cmd[3]
    #         if cmd[0] == 'FONTSIZE' and cmd[1] == (0, 0):
    #             font_size_header = cmd[3]
    #         if cmd[0] == 'TEXTCOLOR' and cmd[1] == (0, 0):
    #             text_color_header = cmd[3]

    #     # Construir encabezado con estilo Paragraph que respete los atributos extraídos
    #     new_header = []
    #     for col in header:
    #         wrapped = wrap_text_auto(col, font_name_header, font_size_header, max_col_width_points)
    #         alignment = 1 if center_title else 0
    #         new_header.append(Paragraph(wrapped, ParagraphStyle(
    #             name='AutoHeaderStyle',
    #             alignment=alignment,
    #             fontName=font_name_header,
    #             fontSize=font_size_header,
    #             textColor=text_color_header,  # Aplica color al texto del encabezado
    #             spaceAfter=3,
    #             leading=font_size_header + 2
    #         )))

    #     # Combinar encabezado y datos
    #     table_data = [new_header] + data

    #     # Determinar anchos de columna si no se pasan manualmente
    #     num_columns = len(header)
    #     column_widths = col_widths_ if col_widths_ else [0] * num_columns
    #     for row in table_data:
    #         for i, cell in enumerate(row):
    #             text = cell.text if isinstance(cell, Paragraph) else str(cell)
    #             width = stringWidth(text, font_name_header, font_size_header) + 20
    #             if width > column_widths[i]:
    #                 column_widths[i] = width

    #     # Crear tabla y aplicar estilo
    #     tabla = Table(table_data, colWidths=column_widths)
    #     tabla.setStyle(TableStyle(tableStyle))

    #     # Calcular posición de la tabla centrada en el eje X
    #     width, height = A4
    #     table_width, table_height = tabla.wrap(0, 0)
    #     x_position_points = (width - table_width) / 2

    #     # Dibujar tabla sobre el canvas
    #     tabla.drawOn(can, x_position_points, height - y_position_points - table_height)
    #     can.save()
    #     packet.seek(0)

    #     # Combinar página base con la nueva tabla
    #     overlay_pdf = PdfReader(packet)
    #     base_page = self.modified_pages.get(page_number, self.reader.pages[page_number])
    #     base_page.merge_page(overlay_pdf.pages[0])
    #     self.modified_pages[page_number] = base_page

    #     return self
    
    # def add_table_to_page_v3(
    #     self,
    #     table,
    #     y_position_mm,
    #     page_number,
    #     tableStyle,
    #     col_widths_=[],
    #     center_title=True,
    #     max_col_width_mm=40
    # ):
    #     """Añade una tabla a una página específica del PDF respetando completamente el estilo de `tableStyle`."""

    #     def wrap_text_auto(col, fontName, fontSize, max_width):
    #         """Ajusta el texto para que no supere el ancho máximo permitido, insertando saltos de línea."""
    #         width = stringWidth(col, fontName, fontSize)
    #         if width <= max_width:
    #             return col
    #         words = col.split()
    #         if len(words) == 1:
    #             return col
    #         best_split = col
    #         min_max_line_width = float('inf')
    #         for split_idx in range(1, len(words)):
    #             line1 = " ".join(words[:split_idx])
    #             line2 = " ".join(words[split_idx:])
    #             max_width_ = max(stringWidth(line1, fontName, fontSize), stringWidth(line2, fontName, fontSize))
    #             if max_width_ <= max_width and max_width_ < min_max_line_width:
    #                 best_split = line1 + "<br/>" + line2
    #                 min_max_line_width = max_width_
    #         return best_split

    #     # Separar encabezado y datos
    #     header, data = self.get_table_header_and_data(table)

    #     # Inicializar PDF en memoria
    #     packet = io.BytesIO()
    #     can = canvas.Canvas(packet, pagesize=A4)

    #     y_position_points = self.mm_to_points_(y_position_mm)
    #     max_col_width_points = self.mm_to_points_(max_col_width_mm)

    #     # Extraer estilo del encabezado desde tableStyle (si existe)
    #     font_name_header = 'Helvetica-Bold'
    #     font_size_header = 10
    #     text_color_header = colors.black

    #     for cmd in tableStyle:
    #         if cmd[0] == 'FONTNAME' and cmd[1] == (0, 0):
    #             font_name_header = cmd[3]
    #         if cmd[0] == 'FONTSIZE' and cmd[1] == (0, 0):
    #             font_size_header = cmd[3]
    #         if cmd[0] == 'TEXTCOLOR' and cmd[1] == (0, 0):
    #             text_color_header = cmd[3]

    #     # Crear Paragraphs para encabezado con estilos y saltos de línea automáticos
    #     new_header = []
    #     for col in header:
    #         wrapped = wrap_text_auto(col, font_name_header, font_size_header, max_col_width_points)
    #         alignment = 1 if center_title else 0
    #         new_header.append(Paragraph(wrapped, ParagraphStyle(
    #             name='AutoHeaderStyle',
    #             alignment=alignment,
    #             fontName=font_name_header,
    #             fontSize=font_size_header,
    #             textColor=text_color_header,
    #             spaceAfter=3,
    #             leading=font_size_header + 2
    #         )))

    #     # Preparar la data completa
    #     table_data = [new_header] + data

    #     # Calcular número de columnas
    #     num_columns = len(header)

    #     # Si se proveen anchos, convertirlos a puntos (desde mm)
    #     if col_widths_:
    #         column_widths = [self.mm_to_points_(w) for w in col_widths_]
    #     else:
    #         # Si no se proveen, calcular automáticamente según el contenido
    #         column_widths = [0] * num_columns
    #         for row in table_data:
    #             for i, cell in enumerate(row):
    #                 text = cell.text if isinstance(cell, Paragraph) else str(cell)
    #                 width = stringWidth(text, font_name_header, font_size_header) + 20
    #                 if width > column_widths[i]:
    #                     column_widths[i] = width

    #     # Crear la tabla
    #     tabla = Table(table_data, colWidths=column_widths)
    #     tabla.setStyle(TableStyle(tableStyle))

    #     # Posicionar la tabla centrada horizontalmente en la página
    #     width, height = A4
    #     table_width, table_height = tabla.wrap(0, 0)
    #     x_position_points = (width - table_width) / 2

    #     # Dibujar en el canvas
    #     tabla.drawOn(can, x_position_points, height - y_position_points - table_height)
    #     can.save()
    #     packet.seek(0)

    #     # Combinar con la página original
    #     overlay_pdf = PdfReader(packet)
    #     base_page = self.modified_pages.get(page_number, self.reader.pages[page_number])
    #     base_page.merge_page(overlay_pdf.pages[0])
    #     self.modified_pages[page_number] = base_page

    #     return self
    
    def add_table_to_page_v3(
        self,
        table,
        y_position_mm,
        page_number,
        tableStyle,
        col_widths_=None,
        center_title=True,
        max_col_width_mm=40
    ):
        """Añade una tabla a una página específica del PDF respetando completamente el estilo de `tableStyle`."""

        def wrap_text_auto(col, fontName, fontSize, max_width):
            width = stringWidth(col, fontName, fontSize)
            if width <= max_width:
                return col
            words = col.split()
            if len(words) == 1:
                return col
            best_split = col
            min_max_line_width = float('inf')
            for split_idx in range(1, len(words)):
                line1 = " ".join(words[:split_idx])
                line2 = " ".join(words[split_idx:])
                max_width_ = max(
                    stringWidth(line1, fontName, fontSize),
                    stringWidth(line2, fontName, fontSize)
                )
                if max_width_ <= max_width and max_width_ < min_max_line_width:
                    best_split = line1 + "<br/>" + line2
                    min_max_line_width = max_width_
            return best_split

        # Obtener encabezado y filas
        header, data = self.get_table_header_and_data(table)

        # Preparar canvas
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)

        y_position_points = self.mm_to_points_(y_position_mm)
        max_col_width_points = self.mm_to_points_(max_col_width_mm)

        # Extraer estilo del encabezado
        font_name_header = 'Helvetica-Bold'
        font_size_header = 10
        text_color_header = colors.black
        for cmd in tableStyle:
            if cmd[0] == 'FONTNAME' and cmd[1] == (0, 0):
                font_name_header = cmd[3]
            if cmd[0] == 'FONTSIZE' and cmd[1] == (0, 0):
                font_size_header = cmd[3]
            if cmd[0] == 'TEXTCOLOR' and cmd[1] == (0, 0):
                text_color_header = cmd[3]

        # Crear encabezados como Paragraphs
        new_header = []
        for col in header:
            wrapped = wrap_text_auto(col, font_name_header, font_size_header, max_col_width_points)
            alignment = 1 if center_title else 0
            new_header.append(Paragraph(wrapped, ParagraphStyle(
                name='AutoHeaderStyle',
                alignment=alignment,
                fontName=font_name_header,
                fontSize=font_size_header,
                textColor=text_color_header,
                spaceAfter=3,
                leading=font_size_header + 2
            )))

        table_data = [new_header] + data
        num_columns = len(header)

        # Calcular anchos
        if isinstance(col_widths_, list):
            column_widths = [self.mm_to_points_(w) for w in col_widths_]

        elif isinstance(col_widths_, dict):
            if all(isinstance(k, int) for k in col_widths_):
                column_widths = [
                    self.mm_to_points_(col_widths_.get(i, max_col_width_mm)) for i in range(num_columns)
                ]
            elif all(isinstance(k, str) for k in col_widths_):
                # Obtener texto plano desde Paragraphs del encabezado
                header_texts = [
                    h.getPlainText() if isinstance(h, Paragraph) else str(h) for h in new_header
                ]
                column_widths = [
                    self.mm_to_points_(col_widths_.get(header_texts[i], max_col_width_mm))
                    for i in range(num_columns)
                ]
            else:
                raise ValueError("El diccionario col_widths_ debe tener claves int (índices) o str (nombres de columnas)")
        else:
            # Calcular automáticamente si no se proveen
            column_widths = [0] * num_columns
            for row in table_data:
                for i, cell in enumerate(row):
                    text = cell.getPlainText() if isinstance(cell, Paragraph) else str(cell)
                    width = stringWidth(text, font_name_header, font_size_header) + 20
                    if width > column_widths[i]:
                        column_widths[i] = width

        # Crear tabla
        tabla = Table(table_data, colWidths=column_widths)
        tabla.setStyle(TableStyle(tableStyle))

        width, height = A4
        table_width, table_height = tabla.wrap(0, 0)
        x_position_points = (width - table_width) / 2
        tabla.drawOn(can, x_position_points, height - y_position_points - table_height)

        can.save()
        packet.seek(0)
        overlay_pdf = PdfReader(packet)
        base_page = self.modified_pages.get(page_number, self.reader.pages[page_number])
        base_page.merge_page(overlay_pdf.pages[0])
        self.modified_pages[page_number] = base_page

        return self


    
    # def unirPDFs(unaEscuela,pdf_paths, output_pdf_path):
    #     hoja_vacía = 'D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeEntrada\Plantillas\Escuelas' + '/4-Página-4-vacía.pdf'
    #     pdf_agosto_2024 = PDF.PDFEditor(
    #         hoja_vacía ,
    #         unaEscuela
    #     ) 
        
    #     pdf_agosto_2024.fusionar_pdfs(
    #         output_pdf_path,
    #         pdf_paths,        
    #     )
    #     return
    
    @staticmethod
    @staticmethod
    def definitivo_unir_PDFs(listaDeRutasPDFs, rutaFinal=None, retornar_stream=False):
        """
        Une PDFs desde rutas de archivos.
        
        Args:
            listaDeRutasPDFs (list): Lista de rutas de PDFs a unir
            rutaFinal (str, optional): Ruta donde guardar el PDF unido
            retornar_stream (bool): Si True, retorna BytesIO en lugar de guardar
        
        Returns:
            BytesIO or None: Stream si retornar_stream=True, None en caso contrario
        
        Example:
            # Guardar en disco (comportamiento original)
            PDFEditor.definitivo_unir_PDFs(['pdf1.pdf', 'pdf2.pdf'], 'salida.pdf')
            
            # Retornar en memoria
            stream = PDFEditor.definitivo_unir_PDFs(
                ['pdf1.pdf', 'pdf2.pdf'], 
                retornar_stream=True
            )
        """
        from PyPDF2 import PdfMerger
        from io import BytesIO
        
        merge = PdfMerger()
        
        for file in listaDeRutasPDFs:
            if file is not None and isinstance(file, str) and file.strip() != "":
                merge.append(file)
            else:
                print(f"⚠️  Archivo inválido o None en la lista, se omite: {file}")
        
        if retornar_stream:
            # Retornar en memoria
            output = BytesIO()
            merge.write(output)
            merge.close()
            output.seek(0)
            print(f"✅ PDF unido creado en memoria")
            return output
        else:
            # Guardar en disco (comportamiento original)
            if rutaFinal is None:
                raise ValueError("rutaFinal es obligatorio cuando retornar_stream=False")
            
            merge.write(rutaFinal)
            merge.close()
            print(f"✅ PDF final guardado en: {rutaFinal}")
            return None
        
    def insertar_imagen_bytes(self, imagen_bytes, x_mm, y_mm, page_number, ancho_mm=None, alto_mm=None, mantener_aspecto=True):
        """
        Inserta una imagen desde bytes en la posición especificada del PDF.
        
        Parámetros:
        - imagen_bytes: bytes de la imagen (PNG, JPG, etc.)
        - x_mm: posición horizontal en milímetros desde la esquina inferior izquierda
        - y_mm: posición vertical en milímetros desde la esquina inferior izquierda
        - page_number: número de página (0-indexed) donde insertar la imagen
        - ancho_mm: ancho deseado en milímetros (opcional)
        - alto_mm: alto deseado en milímetros (opcional)
        - mantener_aspecto: si True, mantiene la proporción de la imagen
        
        Retorna:
        - self para permitir encadenamiento de métodos
        """
        from io import BytesIO
        from reportlab.lib.utils import ImageReader
        from reportlab.pdfgen import canvas
        
        # Convertir mm a puntos
        x_points = self.mm_to_points(x_mm)
        y_points = self.mm_to_points(y_mm)
        
        try:
            # Crear ImageReader desde los bytes
            img_reader = ImageReader(BytesIO(imagen_bytes))
            
            # Obtener dimensiones originales de la imagen
            img_width, img_height = img_reader.getSize()
            
            # Calcular dimensiones finales
            if ancho_mm is None and alto_mm is None:
                # Usar dimensiones originales
                ancho_final = img_width
                alto_final = img_height
            elif ancho_mm and alto_mm and not mantener_aspecto:
                # Usar dimensiones especificadas sin mantener aspecto
                ancho_final = self.mm_to_points(ancho_mm)
                alto_final = self.mm_to_points(alto_mm)
            elif ancho_mm and not alto_mm:
                # Solo ancho especificado, calcular alto
                ancho_final = self.mm_to_points(ancho_mm)
                alto_final = (img_height * ancho_final) / img_width
            elif alto_mm and not ancho_mm:
                # Solo alto especificado, calcular ancho
                alto_final = self.mm_to_points(alto_mm)
                ancho_final = (img_width * alto_final) / img_height
            else:
                # Ambos especificados, mantener aspecto
                ancho_final = self.mm_to_points(ancho_mm)
                alto_final = self.mm_to_points(alto_mm)
                
                ratio_original = img_width / img_height
                ratio_destino = ancho_final / alto_final
                
                if ratio_original > ratio_destino:
                    # La imagen es más ancha proporcionalmente
                    alto_final = ancho_final / ratio_original
                else:
                    # La imagen es más alta proporcionalmente
                    ancho_final = alto_final * ratio_original
            
            # Crear el overlay con la imagen
            packet = BytesIO()
            
            # Obtener las dimensiones de la página
            if page_number in self.modified_pages:
                base_page = self.modified_pages[page_number]
            else:
                base_page = self.reader.pages[page_number]
            
            # Obtener tamaño de la página
            page_width = float(base_page.mediabox.width)
            page_height = float(base_page.mediabox.height)
            
            can = canvas.Canvas(packet, pagesize=(page_width, page_height))
            
            # Dibujar la imagen
            can.drawImage(
                img_reader,
                x_points, y_points,
                width=ancho_final,
                height=alto_final,
                preserveAspectRatio=mantener_aspecto,
                mask='auto'
            )
            
            can.save()
            packet.seek(0)
            
            # Crear el overlay PDF y fusionarlo con la página base
            overlay_pdf = PdfReader(packet)
            overlay_page = overlay_pdf.pages[0]
            base_page.merge_page(overlay_page)
            self.modified_pages[page_number] = base_page
            
        except Exception as e:
            raise Exception(f"Error al insertar imagen desde bytes: {str(e)}")
        
        return self
    
    
    
    
    @staticmethod
    def fusionar_pdfs_desde_bytes(lista_pdf_bytes, escuela_data=None, nombre_operacion="PDFs", verbose=True):
        """
        Fusiona múltiples PDFs desde objetos BytesIO usando PyPDF2 directamente.
        
        Esta función es más eficiente que usar final_union_PDFs con PDFEditors intermedios,
        ya que evita conversiones innecesarias que pueden causar pérdida de modificaciones
        en páginas modificadas (como imágenes insertadas).
        
        Parámetros:
        -----------
        lista_pdf_bytes : list[BytesIO]
            Lista de objetos BytesIO conteniendo PDFs a fusionar.
            Cada BytesIO debe contener un PDF completo y válido.
        
        escuela_data : dict, opcional
            Diccionario con la información de la escuela. Si es None, se usa un dict vacío.
            Default: None
        
        nombre_operacion : str, opcional
            Nombre descriptivo de la operación para los logs.
            Útil para identificar qué tipo de PDFs se están fusionando.
            Default: "PDFs"
        
        verbose : bool, opcional
            Si es True, imprime logs del proceso de fusión.
            Default: True
        
        Retorna:
        --------
        PDFEditor
            Un único objeto PDFEditor con todos los PDFs fusionados.
            Contiene todas las páginas de los PDFs de entrada en orden.
        
        Raises:
        -------
        ValueError
            Si lista_pdf_bytes está vacía o es None.
        
        TypeError
            Si algún elemento de lista_pdf_bytes no es un BytesIO válido.
        
        Ejemplo de uso:
        ---------------
        >>> from io import BytesIO
        >>> from PyPDF2 import PdfWriter
        >>> 
        >>> # Crear PDFs de ejemplo
        >>> pdf1_bytes = BytesIO()
        >>> pdf2_bytes = BytesIO()
        >>> pdf3_bytes = BytesIO()
        >>> 
        >>> # Fusionar
        >>> escuela = {"Escuela_ID": 123, "Nombre": "Escuela Ejemplo"}
        >>> pdf_fusionado = PDFEditor.fusionar_pdfs_desde_bytes(
        ...     [pdf1_bytes, pdf2_bytes, pdf3_bytes],
        ...     escuela_data=escuela,
        ...     nombre_operacion="Reportes de Matemática"
        ... )
        >>> 
        >>> # Guardar resultado
        >>> pdf_fusionado.save('reporte_final.pdf')
        
        Notas:
        ------
        - Esta función lee directamente los PDFs desde BytesIO sin crear PDFEditors intermedios
        - Es especialmente útil cuando los PDFs tienen modificaciones (imágenes, texto, etc.)
        - Más eficiente en memoria que crear múltiples PDFEditors y luego fusionarlos
        - Si solo necesitas fusionar un PDF, lo retorna directamente sin procesamiento adicional
        
        Ver también:
        ------------
        final_union_PDFs : Para fusionar objetos PDFEditor
        merge_pdfs_in_memory : Para fusionar desde rutas de archivos
        """
        from PyPDF2 import PdfReader, PdfWriter
        from io import BytesIO
        
        # Validaciones
        if not lista_pdf_bytes:
            raise ValueError("❌ Error: La lista de PDFs está vacía")
        
        if not isinstance(lista_pdf_bytes, list):
            raise TypeError("❌ Error: lista_pdf_bytes debe ser una lista")
        
        # Si escuela_data es None, usar diccionario vacío
        if escuela_data is None:
            escuela_data = {}
        
        # Logs iniciales
        if verbose:
            print(f'\n🔗 Fusionando {len(lista_pdf_bytes)} {nombre_operacion}...')
        
        # Caso especial: solo un PDF
        if len(lista_pdf_bytes) == 1:
            lista_pdf_bytes[0].seek(0)
            pdf_final = PDFEditor(lista_pdf_bytes[0], escuela_data)
            if verbose:
                print(f'  ℹ️  Solo un PDF, sin necesidad de fusión')
            return pdf_final
        
        # Fusionar múltiples PDFs usando PyPDF2 directamente
        writer_final = PdfWriter()
        total_paginas = 0
        
        for idx, pdf_bytes in enumerate(lista_pdf_bytes):
            try:
                # Asegurar que el puntero está al inicio
                pdf_bytes.seek(0)
                
                # Leer el PDF
                reader = PdfReader(pdf_bytes)
                num_paginas = len(reader.pages)
                
                # Agregar cada página del PDF
                for page in reader.pages:
                    writer_final.add_page(page)
                
                total_paginas += num_paginas
                
                if verbose:
                    print(f'  ✓ PDF {idx+1}/{len(lista_pdf_bytes)} fusionado ({num_paginas} página(s))')
                
            except Exception as e:
                if verbose:
                    print(f'  ❌ Error al fusionar PDF {idx+1}: {str(e)}')
                raise ValueError(f"Error al procesar PDF en posición {idx+1}: {str(e)}")
        
        # Guardar el PDF fusionado en memoria
        output_fusionado = BytesIO()
        writer_final.write(output_fusionado)
        output_fusionado.seek(0)
        
        # Verificar el PDF fusionado
        if verbose:
            verificacion_final = PdfReader(output_fusionado)
            num_pages_final = len(verificacion_final.pages)
            print(f'  🔍 PDF fusionado: {num_pages_final} página(s) totales')
            output_fusionado.seek(0)  # Volver al inicio después de la verificación
        
        # Crear PDFEditor desde el PDF fusionado
        pdf_final = PDFEditor(output_fusionado, escuela_data)
        
        if verbose:
            print(f'  ✅ Fusión completada exitosamente')
        
        return pdf_final


    # ============================================================================
    # EJEMPLO DE CÓMO AGREGAR A LA CLASE PDFEditor
    # ============================================================================

    """
    Para agregar este método a tu clase PDFEditor, copia el método completo
    (desde @staticmethod hasta return pdf_final) y pégalo dentro de la clase PDFEditor
    en tu archivo PDFEditor_mejorado_CON_ALIAS.py

    Ubicación sugerida: después de los métodos de fusión existentes como:
    - final_union_PDFs
    - final_union_PDFs_2
    - merge_pdfs_in_memory

    Ejemplo de ubicación en el archivo:

    class PDFEditor:
        def __init__(self, ...):
            ...
        
        # ... otros métodos ...
        
        @classmethod
        def final_union_PDFs(cls, pdf_editors):
            ...
        
        @staticmethod
        def fusionar_pdfs_desde_bytes(lista_pdf_bytes, escuela_data=None, ...):
            # <-- PEGAR AQUÍ EL MÉTODO
            ...
        
        # ... resto de métodos ...
    """
    
    def insertar_imagen_segura(self, imagen, x_mm, y_mm, page_number=0, ancho_mm=None, 
                          max_altura_mm=None, ajustar_si_excede=True, debug=False):
        """
        Inserta una imagen en el PDF desde bytes o desde un archivo.
        Wrapper que acepta tanto bytes como rutas de archivo.
        
        Parámetros:
        -----------
        imagen : bytes o str
            - Si es bytes: datos de la imagen directamente
            - Si es str: ruta al archivo de imagen (PNG, JPG, etc.)
        
        [Resto de parámetros igual que insertar_imagen_bytes_segura]
        
        Ejemplo de uso:
        ---------------
        >>> # Desde archivo (nuevo)
        >>> pdf_editor.insertar_imagen_segura(
        ...     imagen=r"ruta/a/imagen.png",
        ...     x_mm=30,
        ...     y_mm=100,
        ...     ancho_mm=120
        ... )
        
        >>> # Desde bytes (original)
        >>> pdf_editor.insertar_imagen_segura(
        ...     imagen=img_data,
        ...     x_mm=30,
        ...     y_mm=100,
        ...     ancho_mm=120
        ... )
        """
        # Detectar si es ruta de archivo o bytes
        if isinstance(imagen, str):
            # Es una ruta de archivo, leer los bytes
            try:
                with open(imagen, 'rb') as f:
                    imagen_bytes = f.read()
                if debug:
                    print(f'  📁 Imagen cargada desde: {imagen}')
            except FileNotFoundError:
                raise FileNotFoundError(f'No se encontró el archivo: {imagen}')
            except Exception as e:
                raise Exception(f'Error al leer archivo {imagen}: {str(e)}')
        elif isinstance(imagen, bytes):
            # Ya son bytes, usar directamente
            imagen_bytes = imagen
        else:
            raise TypeError(f'El parámetro imagen debe ser bytes o str (ruta), recibido: {type(imagen)}')
        
        # Llamar a la función original con los bytes
        return self.insertar_imagen_bytes_segura(
            imagen_bytes=imagen_bytes,
            x_mm=x_mm,
            y_mm=y_mm,
            page_number=page_number,
            ancho_mm=ancho_mm,
            max_altura_mm=max_altura_mm,
            ajustar_si_excede=ajustar_si_excede,
            debug=debug
        )
    
    
    def insertar_imagen_bytes_segura(self, imagen_bytes, x_mm, y_mm, page_number=0, ancho_mm=None, 
                                 max_altura_mm=None, ajustar_si_excede=True, debug=False):
        """
        Inserta una imagen en el PDF validando que no exceda los límites de la página.
        Versión mejorada de insertar_imagen_bytes con validación automática.
        
        Parámetros:
        -----------
        imagen_bytes : bytes
            Bytes de la imagen a insertar
        x_mm : float
            Posición X en milímetros (desde la izquierda)
        y_mm : float
            Posición Y en milímetros (desde abajo)
        page_number : int, opcional
            Número de página donde insertar (default: 0)
        ancho_mm : float, opcional
            Ancho deseado de la imagen en milímetros. Si es None, usa el ancho original
        max_altura_mm : float, opcional
            Altura máxima permitida. Si la imagen excede, se ajusta automáticamente
        ajustar_si_excede : bool, opcional
            Si True, ajusta automáticamente si excede límites. Si False, lanza error (default: True)
        debug : bool, opcional
            Si True, muestra información detallada de validación (default: False)
        
        Retorna:
        --------
        dict : Información sobre la inserción con las siguientes keys:
            - 'exito': bool - Si la inserción fue exitosa
            - 'ajustado': bool - Si se realizaron ajustes automáticos
            - 'ancho_original': float - Ancho solicitado originalmente
            - 'ancho_final': float - Ancho final usado
            - 'altura_final': float - Altura final de la imagen
            - 'advertencias': list - Lista de advertencias generadas
        
        Raises:
        -------
        ValueError : Si ajustar_si_excede=False y la imagen excede los límites
        
        Ejemplo de uso:
        ---------------
        >>> # Uso básico (igual que insertar_imagen_bytes)
        >>> pdf_editor.insertar_imagen_bytes_segura(
        ...     imagen_bytes=img_data,
        ...     x_mm=30,
        ...     y_mm=100,
        ...     ancho_mm=120
        ... )
        
        >>> # Con validación estricta (lanza error si no cabe)
        >>> resultado = pdf_editor.insertar_imagen_bytes_segura(
        ...     imagen_bytes=img_data,
        ...     x_mm=30,
        ...     y_mm=100,
        ...     ancho_mm=120,
        ...     max_altura_mm=150,
        ...     ajustar_si_excede=False  # No ajustar, solo validar
        ... )
        
        >>> # Con debug para ver validaciones
        >>> resultado = pdf_editor.insertar_imagen_bytes_segura(
        ...     imagen_bytes=img_data,
        ...     x_mm=30,
        ...     y_mm=100,
        ...     ancho_mm=120,
        ...     debug=True
        ... )
        >>> if resultado['ajustado']:
        ...     print(f"Imagen ajustada: {resultado['ancho_original']}mm → {resultado['ancho_final']:.2f}mm")
        """
        from PIL import Image
        from io import BytesIO
        
        # Constantes de página A4
        ANCHO_PAGINA_MM = 210
        ALTO_PAGINA_MM = 297
        MARGEN_SEGURIDAD_MM = 5  # Margen de seguridad para evitar recortes
        
        # Inicializar resultado
        resultado = {
            'exito': False,
            'ajustado': False,
            'ancho_original': ancho_mm,
            'ancho_final': ancho_mm,
            'altura_final': 0,
            'advertencias': []
        }
        
        try:
            # Obtener dimensiones de la imagen
            img_pil = Image.open(BytesIO(imagen_bytes))
            ancho_px, alto_px = img_pil.size
            
            # Si no se especificó ancho, usar el original (convertido a mm asumiendo 72 DPI)
            if ancho_mm is None:
                ancho_mm = ancho_px * 25.4 / 72  # Convertir px a mm
                resultado['ancho_original'] = ancho_mm
                if debug:
                    print(f'  ℹ️  Ancho no especificado, usando original: {ancho_mm:.2f}mm')
            
            # Calcular altura en mm basada en el ancho
            ratio = alto_px / ancho_px
            altura_calculada_mm = ancho_mm * ratio
            
            if debug:
                print(f'  🔍 Validando imagen:')
                print(f'     • Dimensiones originales: {ancho_px}px × {alto_px}px (ratio: {ratio:.3f})')
                print(f'     • Ancho solicitado: {ancho_mm:.2f}mm')
                print(f'     • Altura calculada: {altura_calculada_mm:.2f}mm')
                print(f'     • Posición: x={x_mm:.2f}mm, y={y_mm:.2f}mm')
                print(f'     • Página: {page_number}')
            
            # Calcular espacios disponibles
            espacio_disponible_ancho = ANCHO_PAGINA_MM - x_mm - MARGEN_SEGURIDAD_MM
            espacio_disponible_altura = ALTO_PAGINA_MM - y_mm - MARGEN_SEGURIDAD_MM
            
            if debug:
                print(f'     • Espacio disponible: ancho={espacio_disponible_ancho:.2f}mm, altura={espacio_disponible_altura:.2f}mm')
            
            # VALIDACIÓN 1: Verificar posición X válida
            if x_mm < 0 or x_mm >= ANCHO_PAGINA_MM:
                raise ValueError(f'Posición X inválida: {x_mm}mm (debe estar entre 0 y {ANCHO_PAGINA_MM}mm)')
            
            # VALIDACIÓN 2: Verificar posición Y válida
            if y_mm < 0 or y_mm >= ALTO_PAGINA_MM:
                raise ValueError(f'Posición Y inválida: {y_mm}mm (debe estar entre 0 y {ALTO_PAGINA_MM}mm)')
            
            # VALIDACIÓN 3: Verificar que no exceda el ancho de la página
            if ancho_mm > espacio_disponible_ancho:
                advertencia = f'Imagen excede ancho disponible: {ancho_mm:.2f}mm > {espacio_disponible_ancho:.2f}mm'
                resultado['advertencias'].append(advertencia)
                
                if debug or not ajustar_si_excede:
                    print(f'     ⚠️  {advertencia}')
                
                if ajustar_si_excede:
                    ancho_mm = espacio_disponible_ancho
                    altura_calculada_mm = ancho_mm * ratio
                    if debug:
                        print(f'     ✅ Ajustando ancho a {ancho_mm:.2f}mm (altura: {altura_calculada_mm:.2f}mm)')
                    resultado['ajustado'] = True
                else:
                    raise ValueError(advertencia)
            
            # VALIDACIÓN 4: Verificar que no exceda la altura disponible
            if altura_calculada_mm > espacio_disponible_altura:
                advertencia = f'Imagen excede altura disponible: {altura_calculada_mm:.2f}mm > {espacio_disponible_altura:.2f}mm'
                resultado['advertencias'].append(advertencia)
                
                if debug or not ajustar_si_excede:
                    print(f'     ⚠️  {advertencia}')
                
                if ajustar_si_excede:
                    # Ajustar por altura disponible
                    altura_calculada_mm = espacio_disponible_altura
                    ancho_mm = altura_calculada_mm / ratio
                    if debug:
                        print(f'     ✅ Ajustando por altura: ancho={ancho_mm:.2f}mm, altura={altura_calculada_mm:.2f}mm')
                    resultado['ajustado'] = True
                else:
                    raise ValueError(advertencia)
            
            # VALIDACIÓN 5: Aplicar max_altura_mm si se especificó
            if max_altura_mm is not None and altura_calculada_mm > max_altura_mm:
                advertencia = f'Imagen excede altura máxima: {altura_calculada_mm:.2f}mm > {max_altura_mm}mm'
                resultado['advertencias'].append(advertencia)
                
                if debug or not ajustar_si_excede:
                    print(f'     ⚠️  {advertencia}')
                
                if ajustar_si_excede:
                    altura_calculada_mm = max_altura_mm
                    ancho_mm = altura_calculada_mm / ratio
                    if debug:
                        print(f'     ✅ Ajustando a altura máxima: ancho={ancho_mm:.2f}mm, altura={altura_calculada_mm:.2f}mm')
                    resultado['ajustado'] = True
                else:
                    raise ValueError(advertencia)
            
            # Validación final de límites
            limite_derecho = x_mm + ancho_mm
            limite_superior = y_mm + altura_calculada_mm
            
            if limite_derecho > ANCHO_PAGINA_MM:
                advertencia = f'Imagen sobresale por derecha: {limite_derecho:.2f}mm > {ANCHO_PAGINA_MM}mm'
                resultado['advertencias'].append(advertencia)
                if not ajustar_si_excede:
                    raise ValueError(advertencia)
            
            if limite_superior > ALTO_PAGINA_MM:
                advertencia = f'Imagen sobresale por arriba: {limite_superior:.2f}mm > {ALTO_PAGINA_MM}mm'
                resultado['advertencias'].append(advertencia)
                if not ajustar_si_excede:
                    raise ValueError(advertencia)
            
            # TODO VALIDADO - INSERTAR IMAGEN
            if debug:
                print(f'     ✅ Dimensiones finales: {ancho_mm:.2f}mm × {altura_calculada_mm:.2f}mm')
                print(f'     📍 Posición: ({x_mm:.2f}, {y_mm:.2f})')
                print(f'     📏 Límites: derecha={limite_derecho:.2f}mm, superior={limite_superior:.2f}mm')
            
            # Llamar al método original insertar_imagen_bytes
            self.insertar_imagen_bytes(
                imagen_bytes=imagen_bytes,
                x_mm=x_mm,
                y_mm=y_mm,
                page_number=page_number,
                ancho_mm=ancho_mm
            )
            
            resultado['exito'] = True
            resultado['ancho_final'] = ancho_mm
            resultado['altura_final'] = altura_calculada_mm
            
            if debug:
                if resultado['ajustado']:
                    print(f'     ⚠️  Imagen ajustada automáticamente')
                    print(f'     📊 Cambio: {resultado["ancho_original"]:.2f}mm → {ancho_mm:.2f}mm')
                else:
                    print(f'     ✅ Imagen insertada sin ajustes')
            
            return resultado
            
        except Exception as e:
            error_msg = f'Error al insertar imagen: {str(e)}'
            resultado['advertencias'].append(error_msg)
            if debug:
                print(f'     ❌ {error_msg}')
            raise
        
    """
    MÉTODOS PARA AGREGAR A LA CLASE PDFEditor
    ==========================================

    Agregar estos métodos a tu clase PDF.PDFEditor en el archivo PDFEditor_mejorado_CON_ALIAS.py

    Estos métodos permiten trabajar con PDFs guardándolos temporalmente en disco,
    lo cual evita problemas de corrupción y memoria.
    """


    # ============================================================================
    # MÉTODOS DE INSTANCIA (trabajan con self)
    # ============================================================================

    def guardar_temporal(self, nombre_archivo, directorio_temporal=None):
        """
        Guarda este PDFEditor en disco como archivo temporal.
        
        Parámetros:
        -----------
        nombre_archivo : str
            Nombre del archivo (sin extensión o con .pdf)
            Ejemplo: "hoja_7_curso_1A" o "hoja_7_curso_1A.pdf"
        directorio_temporal : str, opcional
            Ruta al directorio donde guardar. Si es None, usa directorio predeterminado
        
        Retorna:
        --------
        str : Ruta completa al archivo guardado
        
        Ejemplo:
        --------
        >>> pdf_editor = PDF.PDFEditor(...)
        >>> ruta = pdf_editor.guardar_temporal("hoja_7_1A")
        >>> print(f"Guardado en: {ruta}")
        """
        import os
        
        # Asegurar que el nombre termina en .pdf
        if not nombre_archivo.endswith('.pdf'):
            nombre_archivo += '.pdf'
        
        # Definir directorio temporal
        if directorio_temporal is None:
            directorio_temporal = os.path.join(
                os.getcwd(), 
                'temp_pdfs_fusion'
            )
        
        # Crear directorio si no existe
        os.makedirs(directorio_temporal, exist_ok=True)
        
        # Ruta completa del archivo
        ruta_archivo = os.path.join(directorio_temporal, nombre_archivo)
        
        try:
            # Obtener bytes del PDFEditor usando save_to_stream
            pdf_bytes = self.save_to_stream()
            
            # Si es BytesIO, obtener los bytes
            if hasattr(pdf_bytes, 'getvalue'):
                pdf_bytes_data = pdf_bytes.getvalue()
            else:
                pdf_bytes_data = pdf_bytes
            
            # Guardar en disco
            with open(ruta_archivo, 'wb') as f:
                f.write(pdf_bytes_data)
            
            # Verificar que se guardó correctamente
            tamaño_bytes = os.path.getsize(ruta_archivo)
            tamaño_kb = tamaño_bytes / 1024
            
            print(f'  💾 PDF guardado: {nombre_archivo}')
            print(f'     • Ruta: {ruta_archivo}')
            print(f'     • Tamaño: {tamaño_kb:.2f} KB ({tamaño_bytes:,} bytes)')
            
            return ruta_archivo
            
        except Exception as e:
            print(f'  ❌ Error al guardar {nombre_archivo}: {e}')
            raise


    # ============================================================================
    # MÉTODOS ESTÁTICOS (no necesitan self, trabajan con archivos)
    # ============================================================================

    @staticmethod
    def leer_pdfs_desde_disco(lista_rutas, validar=True):
        """
        Lee múltiples archivos PDF desde disco y retorna lista de PdfReader.
        
        Parámetros:
        -----------
        lista_rutas : list of str
            Lista con las rutas completas a los archivos PDF
        validar : bool, opcional
            Si True, valida que cada archivo existe y es válido (default: True)
        
        Retorna:
        --------
        list of PdfReader : Lista de objetos PdfReader listos para fusionar
        
        Ejemplo:
        --------
        >>> rutas = [
        ...     "/temp/hoja_7_1A.pdf",
        ...     "/temp/hoja_8_1A.pdf"
        ... ]
        >>> readers = PDF.PDFEditor.leer_pdfs_desde_disco(rutas)
        >>> print(f"Se leyeron {len(readers)} PDFs")
        """
        from PyPDF2 import PdfReader
        from io import BytesIO
        import os
        
        readers = []
        
        print(f'\n📂 Leyendo {len(lista_rutas)} archivo(s) PDF desde disco...')
        
        for idx, ruta in enumerate(lista_rutas):
            try:
                # Validar que el archivo existe
                if validar and not os.path.exists(ruta):
                    print(f'  ❌ [{idx+1}] Archivo no encontrado: {ruta}')
                    raise FileNotFoundError(f'Archivo no encontrado: {ruta}')
                
                # Leer el PDF
                with open(ruta, 'rb') as f:
                    pdf_bytes = f.read()
                
                reader = PdfReader(BytesIO(pdf_bytes))
                
                # Validar que el PDF es válido
                if validar:
                    num_paginas = len(reader.pages)
                    if num_paginas == 0:
                        print(f'  ⚠️  [{idx+1}] PDF sin páginas: {os.path.basename(ruta)}')
                else:
                    num_paginas = len(reader.pages)
                
                readers.append(reader)
                
                tamaño_bytes = len(pdf_bytes)
                tamaño_kb = tamaño_bytes / 1024
                
                print(f'  ✅ [{idx+1}] {os.path.basename(ruta)}: {num_paginas} página(s), {tamaño_kb:.2f} KB')
                
            except Exception as e:
                print(f'  ❌ [{idx+1}] Error al leer {os.path.basename(ruta)}: {e}')
                raise
        
        print(f'  📊 Total leído: {len(readers)} PDF(s)')
        
        return readers


    @staticmethod
    def fusionar_pdfs_desde_disco(lista_rutas, escuela_data=None, ruta_salida=None, 
                                eliminar_temporales=False, nombre_operacion=None):
        """
        Fusiona múltiples archivos PDF desde disco usando PdfMerger.
        
        Parámetros:
        -----------
        lista_rutas : list of str
            Lista con las rutas completas a los archivos PDF a fusionar (en orden)
        escuela_data : dict, opcional
            Diccionario con datos de la escuela (para crear el PDFEditor final)
        ruta_salida : str, opcional
            Ruta donde guardar el PDF fusionado. Si es None, retorna PDFEditor
        eliminar_temporales : bool, opcional
            Si True, elimina los archivos temporales después de fusionar (default: False)
        nombre_operacion : str, opcional
            Nombre descriptivo de la operación (para logging)
        
        Retorna:
        --------
        PDFEditor or str : Si ruta_salida es None, retorna PDFEditor con el PDF fusionado.
                        Si ruta_salida se especifica, guarda el archivo y retorna la ruta.
        
        Ejemplo:
        --------
        >>> # Fusionar y retornar PDFEditor
        >>> pdf_final = PDF.PDFEditor.fusionar_pdfs_desde_disco(
        ...     lista_rutas, 
        ...     escuela_data=una_escuela
        ... )
        
        >>> # Fusionar, guardar y limpiar temporales
        >>> ruta = PDF.PDFEditor.fusionar_pdfs_desde_disco(
        ...     lista_rutas,
        ...     escuela_data=una_escuela,
        ...     ruta_salida="/output/reporte.pdf",
        ...     eliminar_temporales=True
        ... )
        """
        from PyPDF2 import PdfMerger
        from io import BytesIO
        import os
        
        operacion = nombre_operacion or "PDFs"
        
        print(f'\n🔗 Fusionando {len(lista_rutas)} archivo(s) PDF ({operacion})...')
        
        try:
            # Crear el merger
            merger = PdfMerger()
            
            # Agregar cada PDF en orden
            for idx, ruta in enumerate(lista_rutas):
                if not os.path.exists(ruta):
                    raise FileNotFoundError(f'Archivo no encontrado: {ruta}')
                
                merger.append(ruta)
                print(f'  ✅ [{idx+1}] Agregado: {os.path.basename(ruta)}')
            
            # Guardar el resultado
            if ruta_salida:
                # Crear directorio si no existe
                directorio_salida = os.path.dirname(ruta_salida)
                if directorio_salida:
                    os.makedirs(directorio_salida, exist_ok=True)
                
                # Guardar en disco
                merger.write(ruta_salida)
                merger.close()
                
                tamaño_bytes = os.path.getsize(ruta_salida)
                tamaño_mb = tamaño_bytes / (1024 * 1024)
                
                print(f'\n  💾 PDF fusionado guardado:')
                print(f'     • Ruta: {ruta_salida}')
                print(f'     • Tamaño: {tamaño_mb:.2f} MB ({tamaño_bytes:,} bytes)')
                
                # Eliminar temporales si se solicitó
                if eliminar_temporales:
                    print(f'\n  🗑️  Eliminando archivos temporales...')
                    for ruta in lista_rutas:
                        try:
                            os.remove(ruta)
                            print(f'     ✅ Eliminado: {os.path.basename(ruta)}')
                        except Exception as e:
                            print(f'     ⚠️  No se pudo eliminar {os.path.basename(ruta)}: {e}')
                
                return ruta_salida
            else:
                # Retornar como PDFEditor
                output = BytesIO()
                merger.write(output)
                merger.close()
                output.seek(0)
                
                tamaño_bytes = len(output.getvalue())
                tamaño_mb = tamaño_bytes / (1024 * 1024)
                
                print(f'\n  ✅ PDF fusionado en memoria:')
                print(f'     • Tamaño: {tamaño_mb:.2f} MB ({tamaño_bytes:,} bytes)')
                
                # Crear PDFEditor con el resultado
                
                pdf_final = PDFEditor(output, escuela_data)
                
                # Eliminar temporales si se solicitó
                if eliminar_temporales:
                    print(f'\n  🗑️  Eliminando archivos temporales...')
                    for ruta in lista_rutas:
                        try:
                            os.remove(ruta)
                            print(f'     ✅ Eliminado: {os.path.basename(ruta)}')
                        except Exception as e:
                            print(f'     ⚠️  No se pudo eliminar {os.path.basename(ruta)}: {e}')
                
                return pdf_final
                
        except Exception as e:
            print(f'  ❌ Error al fusionar PDFs: {e}')
            raise


    @staticmethod
    def limpiar_directorio_temporal(directorio_temporal=None):
        """
        Elimina todos los archivos PDF del directorio temporal.
        
        Parámetros:
        -----------
        directorio_temporal : str, opcional
            Ruta al directorio temporal. Si es None, usa el predeterminado
        
        Retorna:
        --------
        int : Número de archivos eliminados
        
        Ejemplo:
        --------
        >>> PDF.PDFEditor.limpiar_directorio_temporal()
        >>> # Limpia temp_pdfs_fusion/
        """
        import os
        
        if directorio_temporal is None:
            directorio_temporal = os.path.join(os.getcwd(), 'temp_pdfs_fusion')
        
        if not os.path.exists(directorio_temporal):
            print(f'ℹ️  Directorio temporal no existe: {directorio_temporal}')
            return 0
        
        print(f'\n🗑️  Limpiando directorio temporal: {directorio_temporal}')
        
        archivos_eliminados = 0
        
        for archivo in os.listdir(directorio_temporal):
            if archivo.endswith('.pdf'):
                ruta_archivo = os.path.join(directorio_temporal, archivo)
                try:
                    os.remove(ruta_archivo)
                    archivos_eliminados += 1
                    print(f'  ✅ Eliminado: {archivo}')
                except Exception as e:
                    print(f'  ⚠️  Error al eliminar {archivo}: {e}')
        
        print(f'  📊 Total eliminado: {archivos_eliminados} archivo(s)')
        
        # Intentar eliminar el directorio si está vacío
        try:
            if not os.listdir(directorio_temporal):
                os.rmdir(directorio_temporal)
                print(f'  ✅ Directorio temporal eliminado')
        except:
            pass
        
        return archivos_eliminados