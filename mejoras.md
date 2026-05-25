# Mejoras, Sugerencias y Pendientes — Proyecto Matemática

---

## Mejoras logradas (vs. proyecto original)

El proyecto original estaba en:
`python_data_analysis_v3/src/_main_/Matemática/Año_2025/mes_12_diciembre`

| Área | Original | Refactor nuevo |
|------|----------|----------------|
| Estructura | Scripts numerados `a_6_*.py` … `a_15_*.py` sueltos en una carpeta | Paquete limpio con `src/matematica/` + `secciones/` + `libs/` |
| Carga de datos | Cada script cargaba su propio CSV como global al importar | Un solo `cargar_datos(cfg)` en `reporte_pdf.py`; todo se pasa como `datos` dict |
| Filtros | Docenas de pequeños `filtrar_*.py` en subdirectorios separados | Todo consolidado en `src/matematica/filtros.py` |
| Rutas | Hardcodeadas o relativas al script | Centralizadas en `src/paths.py`; raw data co-ubicada con operativo |
| Config | Variables dispersas en múltiples archivos | Un solo `config.py` por operativo; auto-crea carpetas al importar |
| Templates PDF | Rutas hardcodeadas | En `config.py` bajo `TEMPLATES_PRIMARIO` / `TEMPLATES_SECUNDARIO` |
| Visualizaciones | Mezcladas con lógica de negocio | Separadas en `src/libs/visualizaciones/` |
| Estado global | Muchos `df = pd.read_csv(...)` al nivel de módulo | Sin estado global; todo por argumentos |
| Multi-nivel | Lógica de Primario/Secundario mezclada | Selección por nivel via dict de templates en config |
| Reporte por escuela | Script monolítico de cientos de líneas | 7 secciones independientes (`caratula.py` … `hoja_9_nominal.py`) |

---

## Sugerencias inmediatas (antes de correr el operativo)

- **Completar hoja 8**: la tabla de opciones de respuesta (`crear_tabla_respuestas`) aún no está cableada en `hoja_7_y_8.py`. Importar `crear_tabla_análisis_del_tipo_de_respuestas` desde `src/libs/visualizaciones/tabla_opciones_respuesta.py` directamente, en lugar del patrón `datos['crear_tabla_respuestas']`.
- **Actualizar `DICT_PREGUNTA_RESPUESTA`** en `config.py` con las respuestas correctas reales (actualmente son placeholders A/B/C/D cíclicos).
- **Colocar los CSVs** de entrada en `operativos/2025/mes_12_diciembre/data/raw/matematica/`.
- **Colocar los templates PDF** en `data/raw/matematica/templates/Primario/` y `.../Secundario/`.
- **Verificar posiciones** de imágenes en hojas 7-8 ejecutando con una sola escuela de prueba y ajustando `x_mm` / `y_mm`.

---

## Cosas a mejorar en revisiones futuras

- [ ] Reemplazar `print()` con `logging` para poder controlar verbosidad sin tocar el código
- [ ] Agregar barra de progreso (`tqdm`) para el loop de escuelas
- [ ] Añadir un resumen de errores por sección al final (qué escuelas/cursos fallaron y en qué hoja)
- [ ] Parametrizar las posiciones de imagen en `hoja_7_y_8.py` (actualmente hardcodeadas) vía config o constantes
- [ ] Agregar tests unitarios para `filtros.py` con DataFrames mock
- [ ] Soporte para INICIAL (Sala 5) en el generador de reportes PDF (actualmente solo Primario y Secundario tienen templates)
- [ ] Modo de ejecución parcial: poder regenerar solo una escuela sin procesar todo el nominal
- [ ] Validación de CSVs al inicio (columnas requeridas presentes, tipos correctos) para fallar rápido con error claro
- [ ] Separar ETAPA 1 (nominal) de ETAPA 2 (PDFs) con flags de CLI para poder correr solo una etapa

---

## Patrón de arquitectura del proyecto

- `config.py` → auto-crea carpetas → sin setup manual al clonar
- `importlib.util` → carga config desde carpeta que empieza con dígito (`2025`)
- Raw data co-ubicada con el operativo: `operativos/2025/mes_12_diciembre/data/raw/`
- Processed centralizado: `data/processed/matematica/{AÑO_MES}/`
- `src/__init__.py` → registra PROJECT_ROOT en sys.path
- Encoding `utf-8-sig` en todos los CSVs para compatibilidad con Excel

---

## Cómo agregar un nuevo operativo

1. Copiar la carpeta `operativos/2025/mes_12_diciembre/` con nuevo nombre
2. Actualizar `AÑO_MES` en `config.py`
3. Actualizar `NOMINAL['archivo']` con el nombre del nuevo CSV
4. Actualizar `DICT_PREGUNTA_RESPUESTA` con las respuestas correctas del nuevo operativo
5. Actualizar `DICT_EJES_CON_PROCESOS` si cambia la distribución de ítems por eje
6. Colocar CSVs y templates en las carpetas `data/raw/` correspondientes
7. Correr `python operativos/2025/mes_XX_XXXX/main.py`
