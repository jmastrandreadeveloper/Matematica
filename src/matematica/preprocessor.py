"""
Preprocesamiento del nominal de Matemática.
Produce df_nominal_processed y df_datos_institucionales.
"""
import pandas as pd
import src.paths as paths
from src.libs.io.utils import guardar_csv


def process(df: pd.DataFrame, año_mes: str):
    """
    Limpia y normaliza el nominal de Matemática.
    Retorna [df_nominal_processed, df_datos_institucionales].
    """
    nombre = df.Name

    # Cursos válidos
    cursos_validos = ['Sala 5', '1°', '2°', '3°', '4°', '5°', '6°', '7°']
    df = df[df['CURSO_NORMALIZADO'].isin(cursos_validos)].copy()

    # Renombrar columnas
    renombres = {
        'Apellido_Alumno ': 'Apellido',
        'Nombre_Alumno ':   'Nombre',
        'CURSO_NORMALIZADO': 'Curso ',
        'Número_escuela':   'Número',
        'Nombre_Escuela':   'Escuela',
    }
    df = df.rename(columns={k: v for k, v in renombres.items() if k in df.columns})

    # Limpiar columna edad
    if 'Edad' in df.columns:
        df['Edad'] = pd.to_numeric(df['Edad'], errors='coerce')

    # Agregar Nivel_Unificado si no existe
    if 'Nivel_Unificado' not in df.columns and 'Nivel' in df.columns:
        _mapa_nivel = {
            'PRIMARIO': 'Primario', 'Primario': 'Primario',
            'SECUNDARIO': 'Secundario', 'Secundario': 'Secundario',
            'INICIAL': 'Inicial', 'Inicial': 'Inicial',
        }
        df['Nivel_Unificado'] = df['Nivel'].map(_mapa_nivel).fillna(df['Nivel'])

    # Eliminar filas con Escuela_ID = 0
    if 'Escuela_ID' in df.columns:
        df = df[df['Escuela_ID'] != 0]

    # Eliminar Grado Múltiple
    if 'Curso ' in df.columns:
        df = df[df['Curso '] != 'Grado Múltiple']

    # Ordenar por Escuela_ID
    if 'Escuela_ID' in df.columns:
        df = df.sort_values('Escuela_ID').reset_index(drop=True)

    # Guardar nominal procesado
    ruta_processed = paths.proc_matematica(año_mes, f'{nombre}_df_nominal_processed.csv')
    guardar_csv(df, ruta_processed)

    # Construir datos institucionales (una fila por escuela)
    cols_excluir = {'Apellido', 'Nombre', 'DNI', 'Fecha_Nacimiento', 'ciclo_lectivo',
                    'Alumno_ID', 'Sexo', 'Edad', 'Edad_Correcta', 'Curso ', 'División', 'Turno',
                    'Modalidad', 'Alumno_división', 'División_ID'}
    cols_inst = [c for c in df.columns if c not in cols_excluir]

    if 'Escuela_ID' in cols_inst:
        df_inst = df[cols_inst].drop_duplicates(subset=['Escuela_ID']).reset_index(drop=True)
    else:
        df_inst = df[cols_inst].copy()

    ruta_inst = paths.proc_matematica(año_mes, f'{nombre}_df_datos_institucionales.csv')
    guardar_csv(df_inst, ruta_inst)

    return [df, df_inst]
