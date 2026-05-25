"""
Genera el diagrama de barras de cantidad de respuestas correctas alcanzadas.
Entrada: registro de df_1_Histogramas + nivel + dict de cantidad de preguntas por nivel/curso.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO


def generar_imagen_histograma(
    datos_histograma: dict,
    datos_nivel: dict,
    dict_cantidad_preguntas: dict,
    figsize: tuple = (5, 6),
    color: str = '#1f4788',
    dpi: int = 300,
    filename: str = 'histograma.png',
    return_bytes: bool = False,
):
    """
    Parámetros:
    - datos_histograma: dict con Escuela_ID, CURSO_NORMALIZADO, c_0..c_N
    - datos_nivel: dict con Escuela_ID, NIVEL_UNIFICADO
    - dict_cantidad_preguntas: {'INICIAL': {'Sala 5': N}, 'PRIMARIA': {'1°': N, ...}, 'SECUNDARIA': {...}}
    - return_bytes: True → retorna bytes PNG; False → guarda en filename
    """
    if not datos_histograma:
        raise ValueError('No se proporcionaron datos de histograma')
    if not datos_nivel:
        raise ValueError('No se proporcionaron datos de nivel')

    curso_normalizado = datos_histograma['CURSO_NORMALIZADO']
    nivel = datos_nivel['NIVEL_UNIFICADO'].upper()

    if nivel == 'INICIAL':
        nivel_dict, curso_lookup = 'INICIAL', 'Sala 5'
    elif nivel == 'PRIMARIO':
        nivel_dict, curso_lookup = 'PRIMARIA', curso_normalizado
    else:
        nivel_dict, curso_lookup = 'SECUNDARIA', curso_normalizado

    max_preguntas = dict_cantidad_preguntas.get(nivel_dict, {}).get(curso_lookup)
    if max_preguntas is None:
        raise ValueError(f'No se encontró cantidad de preguntas para {nivel_dict} - {curso_lookup}')

    valores = []
    for i in range(max_preguntas + 1):
        v = datos_histograma.get(f'c_{i}')
        if v is None or v == '' or (isinstance(v, float) and np.isnan(v)):
            valores.append(0.0)
        else:
            valores.append(float(v))
    valores = np.array(valores)

    fig, ax = plt.subplots(figsize=figsize)
    x_pos = np.arange(len(valores))
    bars = ax.bar(x_pos, valores, color=color, edgecolor='none', width=0.8)

    for bar, valor in zip(bars, valores):
        if valor > 0:
            ax.text(bar.get_x() + bar.get_width() / 2., bar.get_height(),
                    f'{int(valor)}', ha='center', va='bottom', fontsize=10)

    ax.set_xlabel('Cantidad de ítems de la prueba', fontsize=11)
    ax.set_ylabel('Cantidad de Estudiantes', fontsize=11)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(range(len(valores)), fontsize=10)
    ax.set_ylim(0, max(valores) * 1.15 if max(valores) > 0 else 10)
    ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='gray', linewidth=0.5)
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    plt.tight_layout()

    if return_bytes:
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=dpi, facecolor='white', pad_inches=0)
        buf.seek(0)
        img_bytes = buf.getvalue()
        plt.close(fig)
        return img_bytes
    else:
        plt.savefig(filename, format='png', bbox_inches='tight', dpi=dpi, facecolor='white', pad_inches=0)
        plt.close(fig)
        return filename
