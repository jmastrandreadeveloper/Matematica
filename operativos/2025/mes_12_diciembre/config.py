# Configuración del operativo: Matemática - Diciembre 2025
# Al cargar este archivo se crean automáticamente todas las carpetas necesarias.

AÑO_MES = '2025_12'

import os as _os
import sys as _sys
_OPERATIVO_DIR = _os.path.dirname(_os.path.abspath(__file__))
RAW_MATEMATICA = _os.path.join(_OPERATIVO_DIR, 'data', 'raw', 'matematica')
RAW_NOMINAL    = _os.path.join(_OPERATIVO_DIR, 'data', 'raw', 'nominal')

_PROJECT_ROOT = _os.path.abspath(_os.path.join(_OPERATIVO_DIR, '..', '..', '..'))
if _PROJECT_ROOT not in _sys.path:
    _sys.path.insert(0, _PROJECT_ROOT)
import src.paths as _paths
_os.makedirs(RAW_MATEMATICA, exist_ok=True)
_os.makedirs(RAW_NOMINAL, exist_ok=True)
_paths.proc_matematica(AÑO_MES, '')
_paths.proc_matematica_pdf(AÑO_MES, 'Primario', '')
_paths.proc_matematica_pdf(AÑO_MES, 'Secundario', '')
del _os, _sys, _paths, _PROJECT_ROOT, _OPERATIVO_DIR

# -----------------------------------------------------------------------------
# ARCHIVOS DE ENTRADA
# Los CSVs de df_0 a df_6 van en data/raw/matematica/
# El nominal va en data/raw/nominal/
# -----------------------------------------------------------------------------
NOMINAL = {
    'archivo': '_NOMINAL_MATEMATICA_DICIEMBRE_2025.csv',
    'nombre':  'df_nominal_matematica',
}

# -----------------------------------------------------------------------------
# PDF TEMPLATES POR NIVEL
# Copiar los PDFs template dentro de data/raw/matematica/templates/
# -----------------------------------------------------------------------------
import os as _os
_OPERATIVO_DIR = _os.path.dirname(_os.path.abspath(__file__))
_TPL_PRIMARIO   = _os.path.join(_OPERATIVO_DIR, 'data', 'raw', 'matematica', 'templates', 'Primario')
_TPL_SECUNDARIO = _os.path.join(_OPERATIVO_DIR, 'data', 'raw', 'matematica', 'templates', 'Secundario')

TEMPLATES_PRIMARIO = {
    'caratula':      _os.path.join(_TPL_PRIMARIO, '0-CARATULA.pdf'),
    'hojas_1_2_3':   _os.path.join(_TPL_PRIMARIO, '1-2-3.pdf'),
    'hoja_4':        _os.path.join(_TPL_PRIMARIO, '4.pdf'),
    'hoja_5':        _os.path.join(_TPL_PRIMARIO, '5.pdf'),
    'hoja_6':        _os.path.join(_TPL_PRIMARIO, '6.pdf'),
    'hoja_7_y_8':    _os.path.join(_TPL_PRIMARIO, '7_y_8.pdf'),
    'hoja_9_nominal':_os.path.join(_TPL_PRIMARIO, '9_nominal.pdf'),
}

TEMPLATES_SECUNDARIO = {
    'caratula':      _os.path.join(_TPL_SECUNDARIO, '0-CARATULA.pdf'),
    'hojas_1_2_3':   _os.path.join(_TPL_SECUNDARIO, '1-2-3.pdf'),
    'hoja_4':        _os.path.join(_TPL_SECUNDARIO, '4.pdf'),
    'hoja_5':        _os.path.join(_TPL_SECUNDARIO, '5.pdf'),
    'hoja_6':        _os.path.join(_TPL_SECUNDARIO, '6.pdf'),
    'hoja_7_y_8':    _os.path.join(_TPL_SECUNDARIO, '7_y_8.pdf'),
    'hoja_9_nominal':_os.path.join(_TPL_SECUNDARIO, '9_nominal.pdf'),
}
del _os, _OPERATIVO_DIR, _TPL_PRIMARIO, _TPL_SECUNDARIO

# -----------------------------------------------------------------------------
# CANTIDAD DE PREGUNTAS POR NIVEL Y CURSO
# -----------------------------------------------------------------------------
DICT_CANTIDAD_PREGUNTAS = {
    'INICIAL': {'Sala 5': 6},
    'PRIMARIA': {
        '1°': 8, '2°': 8, '3°': 14, '4°': 14, '5°': 14, '6°': 14, '7°': 14,
    },
    'SECUNDARIA': {
        '1°': 20, '2°': 20, '3°': 20, '4°': 20, '5°': 20,
    },
}

# -----------------------------------------------------------------------------
# EJES TEMÁTICOS POR NIVEL Y CURSO
# -----------------------------------------------------------------------------
DICT_EJES_TEMÁTICOS = {
    'PRIMARIA': {
        '1°': ['Números', 'Operaciones', 'Espacio', 'Geometría', 'Estadística'],
        '2°': ['Números', 'Operaciones', 'Espacio', 'Geometría', 'Estadística'],
        '3°': ['Números', 'Operaciones', 'Geometría', 'Medida', 'Probabilidad'],
        '4°': ['Números', 'Operaciones', 'Cálculo', 'Geometría', 'Medida', 'Estadística'],
        '5°': ['Números', 'Operaciones', 'Geometría', 'Medida', 'Probabilidad'],
        '6°': ['Números', 'Operaciones', 'Cálculo', 'Geometría', 'Medida', 'Estadística', 'Probabilidad'],
        '7°': ['Números', 'Operaciones', 'Cálculo', 'Geometría', 'Medida', 'Estadística', 'Álgebra'],
    },
    'SECUNDARIA': {
        '1°': ['Álgebra', 'Estadística', 'Funciones', 'Geometría', 'Medida', 'Números', 'Operaciones'],
        '2°': ['Álgebra', 'Estadística', 'Funciones', 'Geometría', 'Medida', 'Números'],
        '3°': ['Álgebra', 'Estadística', 'Funciones', 'Medida', 'Números y Álgebra', 'Probabilidad'],
        '4°': ['Álgebra', 'Estadística', 'Funciones', 'Geometría', 'Medida', 'Números y Álgebra'],
        '5°': ['Álgebra', 'Funciones', 'Geometría', 'Medida', 'Probabilidad'],
    },
}

# -----------------------------------------------------------------------------
# RESPUESTA CORRECTA POR ÍTEM (número de pregunta → opción correcta)
# -----------------------------------------------------------------------------
DICT_PREGUNTA_RESPUESTA = {
    'PRIMARIA': {
        '1°': {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'C', 7: 'A', 8: 'B'},
        '2°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D'},
        '3°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D',
               9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'A', 14: 'B'},
        '4°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D',
               9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'A', 14: 'B'},
        '5°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D',
               9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'A', 14: 'B'},
        '6°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D',
               9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'A', 14: 'B'},
        '7°': {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'A', 6: 'B', 7: 'C', 8: 'D',
               9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'A', 14: 'B'},
    },
    'SECUNDARIA': {
        '1°': {i: 'A' for i in range(1, 21)},
        '2°': {i: 'A' for i in range(1, 21)},
        '3°': {i: 'A' for i in range(1, 21)},
        '4°': {i: 'A' for i in range(1, 21)},
        '5°': {i: 'A' for i in range(1, 21)},
    },
    'INICIAL': {
        'Sala 5': {i: 'A' for i in range(1, 7)},
    },
}
# IMPORTANTE: reemplazar los valores placeholder con las respuestas correctas reales

# -----------------------------------------------------------------------------
# EJES TEMÁTICOS CON PROCESOS COGNITIVOS POR NIVEL Y CURSO
# (cantidad de ítems por eje — usada para la tabla nominal de alumnos)
# -----------------------------------------------------------------------------
DICT_EJES_CON_PROCESOS = {
    'PRIMARIA': {
        '1°': {'NÚMEROS': 2, 'OPERACIONES': 2, 'ESPACIO': 1, 'GEOMETRÍA': 1, 'ESTADÍSTICA': 1},
        '2°': {'NÚMEROS': 1, 'OPERACIONES': 2, 'ESPACIO': 1, 'GEOMETRÍA': 1, 'ESTADÍSTICA': 1},
        '3°': {'NÚMEROS': 2, 'OPERACIONES': 2, 'GEOMETRÍA': 1, 'MEDIDA': 2, 'PROBABILIDAD': 1},
        '4°': {'NÚMEROS': 3, 'OPERACIONES': 2, 'CÁLCULO': 1, 'GEOMETRÍA': 2, 'MEDIDA': 2, 'ESTADÍSTICA': 1},
        '5°': {'NÚMEROS': 2, 'OPERACIONES': 2, 'GEOMETRÍA': 1, 'MEDIDA': 2, 'PROBABILIDAD': 1},
        '6°': {'NÚMEROS': 2, 'OPERACIONES': 2, 'CÁLCULO': 1, 'GEOMETRÍA': 2, 'MEDIDA': 2,
               'ESTADÍSTICA': 2, 'PROBABILIDAD': 2},
        '7°': {'NÚMEROS': 1, 'OPERACIONES': 2, 'CÁLCULO': 1, 'GEOMETRÍA': 1, 'MEDIDA': 1,
               'ESTADÍSTICA': 2, 'ÁLGEBRA': 2},
    },
    'SECUNDARIA': {
        '1°': {'ÁLGEBRA': 4, 'ESTADÍSTICA': 2, 'FUNCIONES': 2, 'GEOMETRÍA': 2, 'MEDIDA': 3,
               'NÚMEROS': 2, 'OPERACIONES': 2},
        '2°': {'ÁLGEBRA': 4, 'ESTADÍSTICA': 2, 'FUNCIONES': 3, 'GEOMETRÍA': 2, 'MEDIDA': 3, 'NÚMEROS': 2},
        '3°': {'ÁLGEBRA': 3, 'ESTADÍSTICA': 1, 'FUNCIONES': 4, 'MEDIDA': 4,
               'NÚMEROS Y ÁLGEBRA': 3, 'PROBABILIDAD': 2},
        '4°': {'ÁLGEBRA': 3, 'ESTADÍSTICA': 1, 'FUNCIONES': 3, 'GEOMETRÍA': 3, 'MEDIDA': 2,
               'NÚMEROS Y ÁLGEBRA': 3},
        '5°': {'ÁLGEBRA': 3, 'FUNCIONES': 4, 'GEOMETRÍA': 2, 'MEDIDA': 3, 'PROBABILIDAD': 3},
    },
}
