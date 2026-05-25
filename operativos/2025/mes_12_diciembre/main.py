"""
Punto de entrada: Matemática - Diciembre 2025

Pasos:
  1. Procesar el nominal (limpieza + datos institucionales)
  2. Generar reportes PDF por escuela
"""
import os
import sys

_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

import src  # activa el __init__.py que registra el path
from src.libs.io.utils import cargar_csv
from src.matematica.preprocessor import process as processNominal
from src.matematica.reporte_pdf import generar_reportes_pdf

import importlib.util as _ilu
_cfg_path = os.path.join(os.path.dirname(__file__), 'config.py')
_spec = _ilu.spec_from_file_location('config', _cfg_path)
cfg = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(cfg)


def procesar_nominal():
    filepath = os.path.join(cfg.RAW_NOMINAL, cfg.NOMINAL['archivo'])
    df = cargar_csv(filepath)
    df.Name = cfg.NOMINAL['nombre']
    processNominal(df, cfg.AÑO_MES)


if __name__ == '__main__':
    # ETAPA 1: Nominal
    print('=' * 60)
    print('ETAPA 1 - Procesando Nominal')
    print('=' * 60)
    procesar_nominal()

    # ETAPA 2: Reportes PDF por escuela
    print('=' * 60)
    print('ETAPA 2 - Generando reportes PDF por escuela')
    print('=' * 60)
    generar_reportes_pdf(cfg, cfg.AÑO_MES)

    print('=' * 60)
    print('Proceso completado.')
    print('=' * 60)
