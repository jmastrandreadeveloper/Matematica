"""
Funciones de filtrado consolidadas — reemplazan los múltiples módulos filtrar_*
del proyecto original. Todas reciben DataFrames ya cargados y los filtran.
"""
import pandas as pd


# ---------------------------------------------------------------------------
# Escuelas y cursos
# ---------------------------------------------------------------------------

def obtener_escuelas(df_institucional: pd.DataFrame) -> list:
    """Retorna lista de Escuela_IDs únicos."""
    return sorted(df_institucional['Escuela_ID'].unique().tolist())


def obtener_cursos_escuela(df_cursos: pd.DataFrame, escuela_id) -> list:
    """Retorna lista de CURSO_NORMALIZADO para una escuela."""
    filtrado = df_cursos[df_cursos['Escuela_ID'] == escuela_id]
    return filtrado['CURSO_NORMALIZADO'].tolist()


def obtener_nivel_escuela(df_niveles: pd.DataFrame, escuela_id) -> str | None:
    """Retorna NIVEL_UNIFICADO para una escuela (primer registro)."""
    filtrado = df_niveles[df_niveles['Escuela_ID'] == escuela_id]
    if filtrado.empty:
        return None
    return filtrado.iloc[0]['NIVEL_UNIFICADO']


def filtrar_datos_institucionales(df_institucional: pd.DataFrame, escuela_id) -> dict | None:
    """Retorna datos institucionales de una escuela como dict."""
    filtrado = df_institucional[df_institucional['Escuela_ID'] == escuela_id]
    if filtrado.empty:
        return None
    return filtrado.iloc[0].to_dict()


# ---------------------------------------------------------------------------
# Filtros genéricos por escuela / escuela+curso
# ---------------------------------------------------------------------------

def filtrar_por_escuela(df: pd.DataFrame, escuela_id) -> pd.DataFrame:
    return df[df['Escuela_ID'] == escuela_id].copy()


def filtrar_por_escuela_y_curso(df: pd.DataFrame, escuela_id, curso: str) -> pd.DataFrame:
    return df[(df['Escuela_ID'] == escuela_id) & (df['CURSO_NORMALIZADO'] == curso)].copy()


# ---------------------------------------------------------------------------
# Participación (df_0_Alcance + df_nominal_cantidad)
# ---------------------------------------------------------------------------

def preparar_tabla_participacion(
    df_alcance: pd.DataFrame,
    df_matricula: pd.DataFrame,
    escuela_id,
    cursos: list,
) -> list:
    """
    Prepara la lista de dicts para generar_tabla_participacion().
    Columnas esperadas:
      df_alcance:   Escuela_ID, CURSO_NORMALIZADO, ' Alumnos evaluados'
      df_matricula: Escuela_ID, CURSO_NORMALIZADO, 'matricula_por_escuela_y_curso'
    """
    alc = filtrar_por_escuela(df_alcance, escuela_id)[['CURSO_NORMALIZADO', ' Alumnos evaluados']]
    mat = filtrar_por_escuela(df_matricula, escuela_id)[['CURSO_NORMALIZADO', 'matricula_por_escuela_y_curso']]

    base = pd.DataFrame({'CURSO_NORMALIZADO': cursos})
    base = base.merge(alc, on='CURSO_NORMALIZADO', how='left')
    base = base.merge(mat, on='CURSO_NORMALIZADO', how='left')
    base = base.fillna(0)

    datos = []
    for _, row in base.iterrows():
        datos.append({
            'Grado / Año': row['CURSO_NORMALIZADO'],
            'Participantes': int(row.get(' Alumnos evaluados', 0)),
            'Matrícula': int(row.get('matricula_por_escuela_y_curso', 0)),
        })
    total_part = sum(d['Participantes'] for d in datos)
    total_mat = sum(d['Matrícula'] for d in datos)
    datos.append({'Grado / Año': 'Total general', 'Participantes': total_part, 'Matrícula': total_mat})
    return datos


# ---------------------------------------------------------------------------
# Efectividad (df_2_Efectividad)
# ---------------------------------------------------------------------------

def preparar_tabla_efectividad(df_efectividad: pd.DataFrame, escuela_id) -> list:
    """
    Columnas esperadas: Escuela_ID, CURSO_NORMALIZADO, % Efectividad (0-1 float).
    Retorna lista de dicts para generar_tabla_efectividad().
    """
    filtrado = filtrar_por_escuela(df_efectividad, escuela_id)
    if filtrado.empty:
        return []
    filtrado = filtrado.rename(columns={'CURSO_NORMALIZADO': 'GRADO / AÑO'})
    filtrado['% Efectividad'] = (filtrado['% Efectividad'] * 100).round(1)
    datos = filtrado[['GRADO / AÑO', '% Efectividad']].copy()
    datos['% Efectividad'] = datos['% Efectividad'].apply(lambda x: f'{x}%')
    resultado = datos.to_dict(orient='records')
    promedio = filtrado['% Efectividad'].mean()
    resultado.append({'GRADO / AÑO': 'Total general', '% Efectividad': f'{round(promedio, 1)}%'})
    return resultado


# ---------------------------------------------------------------------------
# Gráfico sub-eje (df_3_Graficos_subeje)
# ---------------------------------------------------------------------------

def filtrar_graficos_subeje(df: pd.DataFrame, escuela_id, curso: str) -> list:
    filtrado = filtrar_por_escuela_y_curso(df, escuela_id, curso)
    return filtrado.to_dict(orient='records')


# ---------------------------------------------------------------------------
# Procesos cognitivos (df_4_Tabla_procesos)
# ---------------------------------------------------------------------------

def filtrar_tabla_procesos(df: pd.DataFrame, escuela_id, curso: str) -> list:
    filtrado = filtrar_por_escuela_y_curso(df, escuela_id, curso)
    return filtrado.to_dict(orient='records')


# ---------------------------------------------------------------------------
# Opciones de respuesta (df_5_Item_opcion_elegida)
# ---------------------------------------------------------------------------

def filtrar_opcion_respuesta(df: pd.DataFrame, escuela_id, curso: str) -> list:
    filtrado = filtrar_por_escuela_y_curso(df, escuela_id, curso)
    return filtrado.to_dict(orient='records')


# ---------------------------------------------------------------------------
# Nominal de prueba (df_6_Nominal_prueba)
# ---------------------------------------------------------------------------

def extraer_alumnos_por_escuela_curso(
    df: pd.DataFrame,
    escuela_id,
    curso: str,
    dict_ejes: dict,
    incluir_division: bool = True,
    incluir_total: bool = True,
) -> pd.DataFrame:
    """
    Extrae listado nominal de alumnos con columnas de ejes relevantes.
    Adaptado de _13_Resultados_Nominales/filtrar/extraer_alumnos_por_escuela_y_curso.py
    """
    _MAPEO_COLUMNAS = {
        'ÁLGEBRA': 'Álgebra', 'CÁLCULO': 'Cálculo', 'ESPACIO': 'Espacio',
        'ESTADÍSTICA': 'Estadística', 'FUNCIONES': 'Funciones', 'GEOMETRÍA': 'Geometría',
        'MEDIDA': 'Medida', 'NÚMEROS': 'Números', 'NÚMEROS Y ÁLGEBRA': 'Números y Álgebra',
        'OPERACIONES': 'Operaciones', 'PROBABILIDAD': 'Probabilidad',
    }
    _NIVEL_MAP = {'Primario': 'PRIMARIA', 'Secundario': 'SECUNDARIA'}

    df_filtrado = df[(df['Escuela_ID'] == escuela_id) & (df['CURSO_NORMALIZADO'] == curso)].copy()
    if df_filtrado.empty:
        return pd.DataFrame()

    nivel = df_filtrado['NIVEL_UNIFICADO'].iloc[0]
    nivel_dict = _NIVEL_MAP.get(nivel)
    ejes_curso = dict_ejes.get(nivel_dict, {}).get(curso, {}) if nivel_dict else {}
    columnas_ejes = [_MAPEO_COLUMNAS[e] for e in ejes_curso if e in _MAPEO_COLUMNAS]

    columnas_base = ['Escuela_ID', 'CURSO_NORMALIZADO', 'NIVEL_UNIFICADO']
    if incluir_division:
        columnas_base.append('División')
    columnas_base += ['Alumno_ID', 'Apellido y Nombre', 'DNI']
    columnas_finales = columnas_base + columnas_ejes
    if incluir_total:
        columnas_finales.append('Total general')

    columnas_disponibles = [c for c in columnas_finales if c in df_filtrado.columns]
    df_resultado = df_filtrado[columnas_disponibles].copy()

    # Truncar nombres
    df_resultado['Apellido y Nombre'] = df_resultado['Apellido y Nombre'].apply(
        lambda x: str(x)[:15] + '...' if len(str(x)) > 15 else x
    )

    # Convertir numericos
    excluir = {'Escuela_ID', 'CURSO_NORMALIZADO', 'NIVEL_UNIFICADO', 'DNI', 'Apellido y Nombre', 'División', 'Alumno_ID'}
    for col in [c for c in df_resultado.columns if c not in excluir]:
        df_resultado[col] = df_resultado[col].fillna(0)
        try:
            df_resultado[col] = df_resultado[col].astype(float).astype(int)
        except (ValueError, TypeError):
            pass

    if 'DNI' in df_resultado.columns:
        try:
            df_resultado['DNI'] = df_resultado['DNI'].fillna(0).astype(float).astype(int)
        except (ValueError, TypeError):
            pass

    # Ordenar
    if 'Total general' in df_resultado.columns and 'División' in df_resultado.columns:
        df_resultado = df_resultado.sort_values(['División', 'Total general'], ascending=[True, True])
    elif 'División' in df_resultado.columns:
        df_resultado = df_resultado.sort_values('División')

    if 'Alumno_ID' in df_resultado.columns:
        df_resultado = df_resultado.drop('Alumno_ID', axis=1)

    return df_resultado.reset_index(drop=True)
