# Contexto del proyecto para Claude Code

## Qué es este proyecto
Refactor limpio del operativo Matemática (originalmente en `python_data_analysis_v3`).
Genera reportes PDF por escuela a partir de CSVs pre-procesados.

## Proyecto fuente (referencia, NO tocar)
`C:\Users\w10-21h2\Documents\GitHub\python_data_analysis_v3\src\_main_\Matemática\Año_2025\mes_12_diciembre`

## Arquitectura

```
Matemática/
├── src/
│   ├── __init__.py              # registra PROJECT_ROOT en sys.path
│   ├── paths.py                 # proc_matematica(año_mes, fn), proc_matematica_pdf(año_mes, nivel, fn)
│   ├── libs/
│   │   ├── io/utils.py          # cargar_csv, guardar_csv (encoding utf-8-sig)
│   │   ├── pdf/editor.py        # PDFEditor (reportlab + PyPDF2) — no modificar
│   │   └── visualizaciones/     # histograma, tabla_participacion, tabla_efectividad,
│   │                            # grafico_subeje, tabla_procesos
│   └── matematica/
│       ├── filtros.py           # TODOS los filtros consolidados
│       ├── preprocessor.py      # process(df, año_mes) — limpieza nominal
│       ├── reporte_pdf.py       # generar_reportes_pdf(cfg, año_mes) — orquestador
│       └── secciones/           # caratula, hojas_1_2_3, hoja_4..9_nominal
└── operativos/
    └── 2025/mes_12_diciembre/
        ├── config.py            # AÑO_MES, rutas RAW, TEMPLATES_*, DICTS_*; auto-crea carpetas
        ├── main.py              # entrada: ETAPA1 nominal → ETAPA2 PDFs
        └── data/raw/            # CSVs y templates PDF van aquí (NO en git)
```

## Decisiones de diseño clave
- **Un solo `cargar_datos(cfg)`** en `reporte_pdf.py` carga todos los CSVs; se pasan como `datos` dict a cada sección
- **`config.py` auto-crea carpetas** al ser importado — sin setup manual
- **`importlib.util`** para cargar config desde carpeta que empieza con dígito (`2025`)
- **Raw data co-ubicada** con el operativo; processed centralizado en `data/processed/`
- **Encoding `utf-8-sig`** en todos los CSVs para compatibilidad con Excel
- **Nivel** = `'Primario'` o `'Secundario'` (no PRIMARIA/SECUNDARIA — eso es para DICT_PREGUNTA_RESPUESTA)

## Datos de entrada (van en data/raw/matematica/ — NO en git)
- `df_0_Alcance.csv`, `df_1_Histogramas.csv`, `df_2_Efectividad.csv`
- `df_3_Graficos_subeje.csv`, `df_4_Tabla_procesos.csv`, `df_5_Item_opcion_elegida.csv`
- `df_6_Nominal_prueba_NIVEL_UNIFICADO_CON_FRACCIONES.csv`
- `df_niveles_unificados.csv`, `df_Escuela_ID_CURSO_NORMALIZADO_list.csv`
- `df_datos_institucionales_Escuela_ID.csv`, `df_nominal_cantidad_de_alumnos_por_escuela_y_curso.csv`
- Templates PDF en `templates/Primario/` y `templates/Secundario/`

## Cómo agregar un nuevo operativo
1. Copiar `operativos/2025/mes_12_diciembre/` con el nuevo nombre
2. Actualizar `AÑO_MES`, `NOMINAL['archivo']`, `DICT_PREGUNTA_RESPUESTA` en `config.py`
3. Colocar CSVs y templates en `data/raw/`
4. Correr `python operativos/2025/mes_XX_XXXX/main.py`

## Pendientes conocidos
- Hoja 8 (tabla opciones de respuesta): función `crear_tabla_análisis_del_tipo_de_respuestas` existe en el proyecto fuente (`_12_.../tabla/crear_tabla_resultados.py`) pero no está cableada en `hoja_7_y_8.py` todavía
- `DICT_PREGUNTA_RESPUESTA` en config tiene valores placeholder — reemplazar con respuestas reales
- Ver `mejoras.md` para lista completa de pendientes y sugerencias
