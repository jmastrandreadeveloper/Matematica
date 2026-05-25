import pandas as pd


def cargar_csv(filepath: str, **kwargs) -> pd.DataFrame:
    """Carga un CSV con encoding utf-8-sig y manejo de errores."""
    try:
        df = pd.read_csv(filepath, encoding='utf-8-sig', low_memory=False, **kwargs)
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, encoding='latin-1', low_memory=False, **kwargs)
    return df


def guardar_csv(df: pd.DataFrame, filepath: str, index: bool = False) -> None:
    df.to_csv(filepath, index=index, encoding='utf-8-sig')
    print(f'Guardado: {filepath}')
