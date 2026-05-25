import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DATA_PROCESSED = os.path.join(PROJECT_ROOT, 'data', 'processed')
PROC_MATEMATICA = os.path.join(DATA_PROCESSED, 'matematica')


def proc_matematica(año_mes: str, filename: str) -> str:
    ruta = os.path.join(PROC_MATEMATICA, año_mes)
    os.makedirs(ruta, exist_ok=True)
    return os.path.join(ruta, filename)


def proc_matematica_pdf(año_mes: str, nivel: str, filename: str) -> str:
    ruta = os.path.join(PROC_MATEMATICA, año_mes, 'reportes_pdf', nivel)
    os.makedirs(ruta, exist_ok=True)
    return os.path.join(ruta, filename)
