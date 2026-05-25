"""
Genera la tabla de porcentaje de efectividad por grado/año como imagen PNG.
Entrada: lista de dicts con {'GRADO / AÑO', '% Efectividad'}.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO


def generar_tabla_efectividad(
    datos: list,
    filename: str = 'tabla_efectividad.png',
    return_bytes: bool = False,
    altura_fila: float = 0.5,
) -> bytes | str:
    grados = [r['GRADO / AÑO'] for r in datos]
    efectividad = [r['% Efectividad'] for r in datos]

    num_filas = len(datos)
    fig, ax = plt.subplots(figsize=(6, (num_filas + 1) * altura_fila * 2))
    ax.axis('tight')
    ax.axis('off')

    datos_tabla = [[grados[i], efectividad[i]] for i in range(num_filas)]

    tabla = ax.table(
        cellText=datos_tabla,
        colLabels=['GRADO / AÑO', '% Efectividad'],
        cellLoc='center',
        loc='center',
        bbox=[0, 0, 1, 1],
    )
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(11)

    for j in range(2):
        cell = tabla[(0, j)]
        cell.set_height(altura_fila)
        cell.set_facecolor('#1E5BA8')
        cell.set_text_props(weight='bold', color='white', fontsize=12)
        cell.set_edgecolor('black')
        cell.set_linewidth(2)

    for i in range(1, num_filas + 1):
        for j in range(2):
            cell = tabla[(i, j)]
            cell.set_height(altura_fila)
            cell.set_edgecolor('black')
            cell.set_linewidth(2)
            if i == num_filas:
                cell.set_facecolor('#00A3E0')
                cell.set_text_props(weight='bold', color='white', fontsize=15)
            else:
                cell.set_facecolor('#FFFFFF')
                cell.set_text_props(color='black', fontsize=15)

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
