"""
Genera el gráfico de barras de efectividad por sub-eje.
Entrada: lista de dicts con {Eje, % Efectividad, CURSO_NORMALIZADO, Escuela_ID}.
"""
import gc
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import numpy as np
import pandas as pd
from io import BytesIO
from typing import Union


def graficar_efectividad_por_eje(
    datos_efectividad: list,
    datos_nivel: dict,
    figsize: tuple = (10, 6),
    color_barras: str = '#5B2C6F',
    mostrar_valores: bool = True,
    mostrar_flecha: bool = False,
    dpi: int = 300,
    filename: str = 'efectividad_por_eje.png',
    return_bytes: bool = False,
) -> Union[bytes, str]:
    """
    Parámetros:
    - datos_efectividad: lista de dicts {Eje, % Efectividad, CURSO_NORMALIZADO}
    - datos_nivel: dict {NIVEL_UNIFICADO}
    """
    if not datos_efectividad:
        raise ValueError('No hay datos de efectividad para graficar')

    df = pd.DataFrame(datos_efectividad).sort_values('Eje')
    ejes = df['Eje'].tolist()
    efectividades = (df['% Efectividad'] * 100).tolist()

    plt.close('all')
    gc.collect()

    fig, ax = plt.subplots(figsize=figsize)
    x_pos = np.arange(len(ejes))
    barras = ax.bar(x_pos, efectividades, color=color_barras, width=0.6)

    ax.set_ylim(0, 100)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)}%'))
    ax.set_yticks(np.arange(0, 101, 25))
    ax.set_xticks(x_pos)
    ax.set_xticklabels(ejes, fontsize=11)
    ax.set_xlabel('Sub Eje', fontsize=12, fontweight='bold')

    if mostrar_valores:
        for barra, valor in zip(barras, efectividades):
            ax.text(barra.get_x() + barra.get_width() / 2., barra.get_height() + 2,
                    f'{valor:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold',
                    color=color_barras)

    if mostrar_flecha and efectividades:
        idx_max = efectividades.index(max(efectividades))
        b = barras[idx_max]
        ax.add_patch(FancyArrowPatch(
            (b.get_x() + b.get_width() / 2, b.get_height() + 8),
            (b.get_x() + b.get_width() / 2, b.get_height() + 18),
            arrowstyle='->,head_width=0.8,head_length=0.8',
            color='#00D9B5', linewidth=4, zorder=5,
        ))

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_axisbelow(True)
    plt.subplots_adjust(bottom=0.15)

    if return_bytes:
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=dpi, facecolor='white', pad_inches=0)
        buf.seek(0)
        img_bytes = buf.getvalue()
        plt.close(fig)
        gc.collect()
        return img_bytes
    else:
        plt.savefig(filename, format='png', bbox_inches='tight', dpi=dpi, facecolor='white', pad_inches=0)
        plt.close(fig)
        gc.collect()
        return filename
