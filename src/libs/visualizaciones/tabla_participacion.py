"""
Genera la tabla de participación por curso como imagen PNG.
Entrada: lista de dicts con {'Grado / Año', 'Participantes', 'Matrícula'}.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO


def generar_tabla_participacion(
    datos: list,
    filename: str = 'tabla_participacion.png',
    return_bytes: bool = False,
    altura_fila: float = 0.5,
) -> bytes | str:
    grados, participantes, matricula, porcentajes, pct_num = [], [], [], [], []

    for reg in datos:
        grados.append(reg['Grado / Año'])
        participantes.append(reg['Participantes'])
        matricula.append(reg['Matrícula'])
        if reg['Grado / Año'] != 'Total general':
            pct = (reg['Participantes'] / reg['Matrícula'] * 100) if reg['Matrícula'] > 0 else 0.0
            porcentajes.append(f'{pct:.1f}%')
            pct_num.append(pct)
        else:
            promedio = np.mean(pct_num) if pct_num else 0.0
            porcentajes.append(f'{promedio:.1f}%')

    num_filas = len(datos)
    fig, ax = plt.subplots(figsize=(10, (num_filas + 1) * altura_fila * 2))
    ax.axis('tight')
    ax.axis('off')

    datos_tabla = [[grados[i], participantes[i], matricula[i], porcentajes[i]] for i in range(num_filas)]

    tabla = ax.table(
        cellText=datos_tabla,
        colLabels=['Grado / Año', 'Participantes', 'Matrícula', '% de Participación'],
        cellLoc='center',
        loc='center',
        bbox=[0, 0, 1, 1],
    )
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(11)

    for j in range(4):
        cell = tabla[(0, j)]
        cell.set_height(altura_fila)
        cell.set_facecolor('#1E3A8A')
        cell.set_text_props(weight='bold', color='white', fontsize=12)
        cell.set_edgecolor('white')
        cell.set_linewidth(1.5)

    for i in range(1, num_filas + 1):
        es_total = i == num_filas
        for j in range(4):
            cell = tabla[(i, j)]
            cell.set_height(altura_fila)
            cell.set_edgecolor('black')
            cell.set_linewidth(1.5)
            if es_total:
                cell.set_facecolor('#00B4D8')
                cell.set_text_props(weight='bold', color='white', fontsize=15)
            elif j == 0:
                cell.set_facecolor('#60A5FA')
                cell.set_text_props(weight='bold', color='white', fontsize=15)
            else:
                cell.set_facecolor('#FFFFFF')
                cell.set_text_props(weight='bold', color='black', fontsize=15)

    if return_bytes:
        buf = BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=300, facecolor='white', pad_inches=0)
        buf.seek(0)
        img_bytes = buf.getvalue()
        plt.close()
        return img_bytes
    else:
        plt.savefig(filename, bbox_inches='tight', dpi=300, facecolor='white', pad_inches=0)
        plt.close()
        return filename
