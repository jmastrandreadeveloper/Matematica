"""
Genera la tabla de porcentaje de efectividad por proceso cognitivo como imagen PNG.
Entrada: lista de dicts con {Eje, Proceso cognitivo, % Efectividad}.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
from io import BytesIO


def generar_tabla_procesos(
    datos,
    filename: str = 'tabla_procesos.png',
    return_bytes: bool = False,
    altura_fila: float = 0.65,
) -> bytes | str:
    df = pd.DataFrame(datos) if isinstance(datos, list) else datos.copy()
    df['Proceso_limpio'] = df['Proceso cognitivo'].str.replace(r'^[A-Z]\s+', '', regex=True)
    df = df.sort_values('Eje').reset_index(drop=True)

    num_rows = len(df)
    altura_figura = num_rows * altura_fila + 1.2
    fig, ax = plt.subplots(figsize=(14, altura_figura))
    ax.axis('off')

    col_widths = [0.10, 0.22, 0.09]
    total_width = sum(col_widths)
    row_height = altura_fila / (num_rows / max(len(df), 1))
    x_start, y_start = 0, 0.88
    margen_texto = 0.01

    headers = ['Sub Eje', 'Proceso cognitivo', '% de Efectividad']
    x_pos = x_start
    for header, width in zip(headers, col_widths):
        rect = Rectangle((x_pos, y_start), width, row_height, linewidth=2, edgecolor='black', facecolor='#1E5BA8')
        ax.add_patch(rect)
        ax.text(x_pos + width / 2, y_start + row_height / 2, header,
                ha='center', va='center', color='white', weight='bold', fontsize=16)
        x_pos += width

    y_pos = y_start
    for eje_name, group in df.groupby('Eje', sort=False):
        num_filas_eje = len(group)
        eje_height = row_height * num_filas_eje
        y_centro = y_pos - eje_height / 2

        rect = Rectangle((x_start, y_pos - eje_height), col_widths[0], eje_height,
                          linewidth=2, edgecolor='black', facecolor='#8BB8E8')
        ax.add_patch(rect)
        ax.text(x_start + margen_texto, y_centro, eje_name,
                ha='left', va='center', color='black', weight='bold', fontsize=15)

        current_y = y_pos
        for _, row in group.iterrows():
            rect = Rectangle((x_start + col_widths[0], current_y - row_height), col_widths[1], row_height,
                              linewidth=2, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            ax.text(x_start + col_widths[0] + margen_texto, current_y - row_height / 2,
                    row['Proceso_limpio'], ha='left', va='center', color='black', fontsize=16)

            efectividad_texto = f"{row['% Efectividad'] * 100:.1f}%"
            rect = Rectangle((x_start + col_widths[0] + col_widths[1], current_y - row_height), col_widths[2], row_height,
                              linewidth=2, edgecolor='black', facecolor='white')
            ax.add_patch(rect)
            ax.text(x_start + col_widths[0] + col_widths[1] + col_widths[2] / 2,
                    current_y - row_height / 2, efectividad_texto,
                    ha='center', va='center', color='black', fontsize=16, weight='bold')
            current_y -= row_height

        y_pos = current_y

    ax.set_xlim(x_start, x_start + total_width)
    ax.set_ylim(y_pos, y_start + row_height)

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
