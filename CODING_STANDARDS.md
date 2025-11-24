# 📏 Guía de Estándares de Código
# Proyecto BMW Pricing - Data Engineering & Analysis

**Versión:** 1.0  
**Fecha:** Noviembre 2025  
**Propósito:** Normalizar el código entre todos los integrantes para facilitar la integración final

---

<a id="tabla-de-contenidos"></a>
## 📋 Tabla de Contenidos

- [Convenciones Generales](#convenciones-generales)
- [Nombres de Variables](#nombres-de-variables)
- [Estructura del Notebook](#estructura-del-notebook)
- [Librerías y Imports](#librerías-y-imports)
- [Carga de Datos](#carga-de-datos)
- [Análisis Exploratorio](#análisis-exploratorio)
- [Limpieza de Duplicados](#limpieza-de-duplicados)
- [Tratamiento de Valores Nulos](#tratamiento-de-valores-nulos)
- [Detección de Outliers](#detección-de-outliers)
- [Feature Engineering](#feature-engineering)
- [Documentación y Comentarios](#documentación-y-comentarios)
- [Visualizaciones](#visualizaciones)
- [Funciones Reutilizables](#funciones-reutilizables)
- [Checklist Final](#checklist-final)

---

<a id="convenciones-generales"></a>
## Convenciones Generales

### Reglas Básicas

```python
# ✅ HACER
- Usar inglés para nombres de columnas del dataset original
- Usar snake_case para variables: mi_variable_nombre
- Usar CamelCase para clases: MiClase
- Nombres descriptivos y claros
- Comentarios en español (para claridad del equipo)
- Máximo 79 caracteres por línea (PEP 8)

# ❌ NO HACER
- Nombres genéricos: x, y, temp, data
- CamelCase para variables: MiVariable
- Nombres en español para variables del dataset: precio, kilometraje
- Líneas de más de 100 caracteres
```

### Estilo de Código

```python
# ✅ Espaciado correcto
df_clean = df[df['price'] > 0]
resultado = funcion(parametro1, parametro2)

# ❌ Sin espacios o mal espaciado
df_clean=df[df['price']>0]
resultado = funcion( parametro1,parametro2 )
```

---

<a id="nombres-de-variables"></a>
## Nombres de Variables

### 1. DataFrame Principal

```python
# ✅ USAR SIEMPRE
df                  # DataFrame original después de la carga
df_clean            # DataFrame después de limpieza completa
df_encoded          # DataFrame después de encoding
df_scaled           # DataFrame después de scaling
df_final            # DataFrame listo para guardar

# ❌ NO USAR
datos, data, bmw_data, dataset, df_limpio, clean_df
```

### 2. DataFrames Temporales

```python
# ✅ Para operaciones intermedias
df_temp             # DataFrame temporal
df_no_duplicates    # Después de eliminar duplicados
df_no_nulls         # Después de eliminar nulos
df_no_outliers      # Después de eliminar outliers

# ❌ NO USAR
temp, tmp, df1, df2, df3
```

### 3. Variables de Columnas

```python
# ✅ Usar los nombres originales del dataset
'price'             # No 'precio'
'mileage'           # No 'kilometraje'
'year'              # No 'ano' o 'anio'
'model'             # No 'modelo'
'brand'             # No 'marca'
'fuel_type'         # No 'tipo_combustible'

# ✅ Para listas de columnas
numeric_cols        # Columnas numéricas
categorical_cols    # Columnas categóricas
cols_with_nulls     # Columnas con valores nulos
cols_to_drop        # Columnas a eliminar

# ❌ NO USAR
numericas, categoricas, columnas_numericas
```

### 4. Variables Numéricas

```python
# ✅ Nombres descriptivos
n_rows              # Número de filas
n_cols              # Número de columnas
n_duplicates        # Número de duplicados
n_nulls             # Número de valores nulos
retention_rate      # Tasa de retención (%)
missing_threshold   # Umbral de valores faltantes

# ❌ NO USAR
num, cantidad, total, x, n
```

### 5. Variables de Umbral/Threshold

```python
# ✅ Para umbrales y límites
outlier_threshold = 1.5        # Factor IQR para outliers
null_threshold = 0.5           # Máximo % de nulos permitido
correlation_threshold = 0.8    # Correlación alta

# ❌ NO USAR
umbral, limite, threshold_val, th
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="estructura-del-notebook"></a>
## Estructura del Notebook

### Plantilla Obligatoria

Todos los notebooks individuales DEBEN seguir esta estructura:

```python
"""
====================================================================
LIMPIEZA Y PREPROCESAMIENTO - DATASET BMW PRICING
====================================================================
Autor: [TU NOMBRE COMPLETO]
Fecha: [FECHA]
Descripción: Proceso completo de limpieza de datos para preparar
             el dataset BMW para modelado predictivo de precios.
====================================================================
"""

# ========================================
# 1. IMPORTS Y CONFIGURACIÓN
# ========================================

# ========================================
# 2. CARGA DE DATOS
# ========================================

# ========================================
# 3. ANÁLISIS EXPLORATORIO INICIAL
# ========================================
# 3.1 Información General
# 3.2 Estadísticas Descriptivas
# 3.3 Análisis de Tipos de Datos

# ========================================
# 4. ANÁLISIS DE CALIDAD DE DATOS
# ========================================
# 4.1 Duplicados
# 4.2 Valores Nulos
# 4.3 Valores Inconsistentes

# ========================================
# 5. LIMPIEZA DE DUPLICADOS
# ========================================

# ========================================
# 6. TRATAMIENTO DE VALORES NULOS
# ========================================
# 6.1 Análisis de Patrones
# 6.2 Estrategia de Imputación
# 6.3 Implementación

# ========================================
# 7. DETECCIÓN Y TRATAMIENTO DE OUTLIERS
# ========================================
# 7.1 Variables Numéricas
# 7.2 Visualización
# 7.3 Tratamiento

# ========================================
# 8. TRANSFORMACIÓN DE VARIABLES
# ========================================
# 8.1 Variables Categóricas
# 8.2 Variables Numéricas

# ========================================
# 9. FEATURE ENGINEERING
# ========================================

# ========================================
# 10. VALIDACIÓN FINAL
# ========================================

# ========================================
# 11. EXPORTACIÓN DE DATOS LIMPIOS
# ========================================

# ========================================
# 12. RESUMEN Y CONCLUSIONES
# ========================================
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="librerías-y-imports"></a>
## Librerías y Imports

### 1. Orden y Agrupación

```python
# ========================================
# 1. IMPORTS Y CONFIGURACIÓN
# ========================================

# Librerías estándar de Python
import os
import sys
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Librerías de análisis de datos
import pandas as pd
import numpy as np

# Librerías de visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Librerías de machine learning
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from scipy import stats
from scipy.stats import zscore

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

# Configuración de reproducibilidad
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
```

### 2. Configuración de Gráficos

```python
# ✅ Configuración estándar para todos
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="carga-de-datos"></a>
## Carga de Datos

### 1. Código Estándar

```python
# ========================================
# 2. CARGA DE DATOS
# ========================================

# Ruta al archivo de datos
DATA_PATH = 'data/raw/bmw_pricing_v3.csv'

# Cargar dataset
print("Cargando dataset...")
df = pd.read_csv(DATA_PATH)

# Información básica
print(f"✓ Dataset cargado exitosamente")
print(f"  - Filas: {df.shape[0]:,}")
print(f"  - Columnas: {df.shape[1]}")
print(f"  - Memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
```

### 2. Crear Copia de Seguridad

```python
# ✅ SIEMPRE crear backup del original
df_original = df.copy()
print(f"✓ Backup creado: {df_original.shape[0]:,} registros")
```

---

<a id="análisis-exploratorio"></a>
## Análisis Exploratorio

### 1. Información General
```python
# ========================================
# 3. ANÁLISIS EXPLORATORIO INICIAL
# ========================================

# 3.1 Información General
print("=" * 60)
print("INFORMACIÓN GENERAL DEL DATASET")
print("=" * 60)

print("\n📊 Estructura del Dataset:")
df.info()

print("\n📈 Primeras 5 filas:")
display(df.head())

print("\n📉 Últimas 5 filas:")
display(df.tail())
```

### 2. Estadísticas Descriptivas
```python
# 3.2 Estadísticas Descriptivas
print("\n" + "=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 60)

print("\n🔢 Variables Numéricas:")
display(df.describe())

print("\n📝 Variables Categóricas:")
display(df.describe(include='object'))
```

### 3. Análisis de Tipos
```python
# 3.3 Análisis de Tipos de Datos
print("\n" + "=" * 60)
print("ANÁLISIS DE TIPOS DE DATOS")
print("=" * 60)

# Identificar tipos de columnas
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print(f"\n✓ Variables numéricas ({len(numeric_cols)}):")
for col in numeric_cols:
    print(f"  - {col}: {df[col].dtype}")

print(f"\n✓ Variables categóricas ({len(categorical_cols)}):")
for col in categorical_cols:
    n_unique = df[col].nunique()
    print(f"  - {col}: {n_unique} valores únicos")
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="limpieza-de-duplicados"></a>
## Limpieza de Duplicados

### 1. Código Estándar
```python
# ========================================
# 5. LIMPIEZA DE DUPLICADOS
# ========================================

print("=" * 60)
print("ANÁLISIS Y ELIMINACIÓN DE DUPLICADOS")
print("=" * 60)

# Análisis de duplicados
n_duplicates = df.duplicated().sum()
print(f"\n📊 Duplicados completos: {n_duplicates} ({n_duplicates/len(df)*100:.2f}%)")

if n_duplicates > 0:
    print("\nEjemplos de duplicados:")
    display(df[df.duplicated(keep=False)].head(10))

    # Eliminar duplicados
    df_clean = df.drop_duplicates(keep='first')

    # Reporte
    n_removed = len(df) - len(df_clean)
    print(f"\n✓ Duplicados eliminados: {n_removed}")
    print(f"  - Registros antes: {len(df):,}")
    print(f"  - Registros después: {len(df_clean):,}")
    print(f"  - Retención: {len(df_clean)/len(df)*100:.2f}%")

    df = df_clean
else:
    print("\n✓ No se encontraron duplicados completos")

# Duplicados por columnas clave (si aplica)
key_cols = ['model', 'year', 'price', 'mileage']
n_duplicates_key = df.duplicated(subset=key_cols).sum()

print(f"\n📊 Duplicados por columnas clave {key_cols}: {n_duplicates_key}")

if n_duplicates_key > 0:
    print(f"\n⚠️ Encontrados {n_duplicates_key} duplicados potenciales")
    print("Análisis manual requerido")
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="tratamiento-de-valores-nulos"></a>
## Tratamiento de Valores Nulos

### 1. Análisis de Nulos
```python
# ========================================
# 6. TRATAMIENTO DE VALORES NULOS
# ========================================

print("=" * 60)
print("ANÁLISIS DE VALORES NULOS")
print("=" * 60)

# 6.1 Análisis de Patrones
# Contar nulos por columna
null_counts = df.isnull().sum()
null_percentages = (null_counts / len(df) * 100).round(2)

# DataFrame de resumen
null_summary = pd.DataFrame({
    'Columna': null_counts.index,
    'Valores_Nulos': null_counts.values,
    'Porcentaje': null_percentages.values
}).sort_values('Valores_Nulos', ascending=False)

# Filtrar solo columnas con nulos
null_summary = null_summary[null_summary['Valores_Nulos'] > 0]

if len(null_summary) > 0:
    print(f"\n📊 Columnas con valores nulos ({len(null_summary)}):")
    display(null_summary)

    # Visualización
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='viridis')
    plt.title('Mapa de Valores Nulos')
    plt.xlabel('Columnas')
    plt.tight_layout()
    plt.show()
else:
    print("\n✓ No se encontraron valores nulos")
```

### 2. Estrategia de Imputación
```python
# 6.2 Estrategia de Imputación

print("\n" + "=" * 60)
print("ESTRATEGIA DE IMPUTACIÓN")
print("=" * 60)

# Definir umbrales
null_threshold_drop = 50  # % de nulos para eliminar columna
null_threshold_impute = 50  # % de nulos para imputar

# Columnas a eliminar (>50% nulos)
cols_to_drop = null_summary[
    null_summary['Porcentaje'] > null_threshold_drop
]['Columna'].tolist()

# Columnas a imputar (<50% nulos)
cols_to_impute = null_summary[
    null_summary['Porcentaje'] <= null_threshold_impute
]['Columna'].tolist()

print(f"\n📉 Columnas a eliminar (>{null_threshold_drop}% nulos): {len(cols_to_drop)}")
for col in cols_to_drop:
    pct = null_summary[null_summary['Columna'] == col]['Porcentaje'].values[0]
    print(f"  - {col}: {pct}% nulos")

print(f"\n🔧 Columnas a imputar (<={null_threshold_impute}% nulos): {len(cols_to_impute)}")
for col in cols_to_impute:
    pct = null_summary[null_summary['Columna'] == col]['Porcentaje'].values[0]
    print(f"  - {col}: {pct}% nulos")
```

### 3. Implementación
```python
# 6.3 Implementación

# Eliminar columnas con muchos nulos
if len(cols_to_drop) > 0:
    df = df.drop(columns=cols_to_drop)
    print(f"\n✓ Eliminadas {len(cols_to_drop)} columnas")

# Imputar valores nulos
for col in cols_to_impute:
    if col in numeric_cols:
        # Variables numéricas: mediana
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)
        print(f"✓ {col}: imputado con mediana ({median_value:.2f})")
    else:
        # Variables categóricas: moda
        mode_value = df[col].mode()[0]
        df[col].fillna(mode_value, inplace=True)
        print(f"✓ {col}: imputado con moda ('{mode_value}')")

# Verificar que no quedan nulos
remaining_nulls = df.isnull().sum().sum()
print(f"\n✓ Valores nulos restantes: {remaining_nulls}")
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="detección-de-outliers"></a>
## Detección de Outliers

### 1. Método IQR
```python
# ========================================
# 7. DETECCIÓN Y TRATAMIENTO DE OUTLIERS
# ========================================

print("=" * 60)
print("DETECCIÓN DE OUTLIERS")
print("=" * 60)

# 7.1 Variables Numéricas

# Función para detectar outliers con IQR
def detect_outliers_iqr(df: pd.DataFrame, column: str, factor: float = 1.5) -> tuple:
    """
    Detecta outliers usando el método IQR.

    Args:
    -----------
    df : DataFrame con los datos
    column : Nombre de la columna
    factor : Factor multiplicador de IQR (default=1.5)

    Returns:
    --------
        (lower_bound, upper_bound, n_outliers, outlier_indices)
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR

    outlier_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
    n_outliers = outlier_mask.sum()
    outlier_indices = df[outlier_mask].index

    return lower_bound, upper_bound, n_outliers, outlier_indices

# Analizar cada variable numérica
outlier_summary = []

for col in numeric_cols:
    lower, upper, n_outliers, _ = detect_outliers_iqr(df, col)
    pct_outliers = (n_outliers / len(df) * 100)

    outlier_summary.append({
        'Columna': col,
        'Limite_Inferior': lower,
        'Limite_Superior': upper,
        'N_Outliers': n_outliers,
        'Porcentaje': pct_outliers
    })

outlier_df = pd.DataFrame(outlier_summary)
outlier_df = outlier_df[outlier_df['N_Outliers'] > 0]

print(f"\n📊 Variables con outliers:")
display(outlier_df)
```

### 2. Visualización
```python
# 7.2 Visualización

# Boxplots para variables con outliers
if len(outlier_df) > 0:
    n_plots = len(outlier_df)
    n_cols = 3
    n_rows = (n_plots + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    axes = axes.flatten() if n_plots > 1 else [axes]

    for idx, col in enumerate(outlier_df['Columna']):
        ax = axes[idx]
        df.boxplot(column=col, ax=ax)
        ax.set_title(f'Boxplot: {col}')
        ax.set_ylabel('Valor')

    # Ocultar subplots vacíos
    for idx in range(n_plots, len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    plt.show()
```

### 3. Tratamiento
```python
# 7.3 Tratamiento

print("\n" + "=" * 60)
print("TRATAMIENTO DE OUTLIERS")
print("=" * 60)

# Estrategia: Eliminar outliers extremos en price
col_to_treat = 'price'

if col_to_treat in df.columns:
    lower, upper, n_outliers, outlier_idx = detect_outliers_iqr(df, col_to_treat, factor=1.5)

    print(f"\n📊 Variable: {col_to_treat}")
    print(f"  - Límite inferior: {lower:.2f}")
    print(f"  - Límite superior: {upper:.2f}")
    print(f"  - Outliers detectados: {n_outliers} ({n_outliers/len(df)*100:.2f}%)")

    # Eliminar outliers
    df_no_outliers = df[(df[col_to_treat] >= lower) & (df[col_to_treat] <= upper)]

    n_removed = len(df) - len(df_no_outliers)
    print(f"\n✓ Outliers eliminados: {n_removed}")
    print(f"  - Registros antes: {len(df):,}")
    print(f"  - Registros después: {len(df_no_outliers):,}")
    print(f"  - Retención: {len(df_no_outliers)/len(df)*100:.2f}%")

    df = df_no_outliers
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="feature-engineering"></a>
## Feature Engineering

### 1. Encoding de Variables Categóricas
```python
# ========================================
# 9. FEATURE ENGINEERING
# ========================================

print("=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

# 9.1 Encoding de Variables Categóricas

# Identificar variables categóricas
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

print(f"\n📝 Variables categóricas a codificar: {len(categorical_cols)}")

# One-Hot Encoding
df_encoded = pd.get_dummies(
    df, 
    columns=categorical_cols, 
    drop_first=True,  # Evitar multicolinealidad
    dtype=int
)

print(f"\n✓ Encoding completado")
print(f"  - Columnas antes: {df.shape[1]}")
print(f"  - Columnas después: {df_encoded.shape[1]}")
print(f"  - Nuevas columnas: {df_encoded.shape[1] - df.shape[1]}")

df = df_encoded
```

### 2. Scaling de Variables Numéricas
```python
# 9.2 Scaling de Variables Numéricas

# Identificar columnas numéricas (sin las dummies)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Excluir columnas dummy (valores 0 y 1)
numeric_cols_to_scale = [
    col for col in numeric_cols 
    if not df[col].isin([0, 1]).all()
]

print(f"\n🔢 Variables numéricas a escalar: {len(numeric_cols_to_scale)}")
for col in numeric_cols_to_scale:
    print(f"  - {col}")

# MinMaxScaler (0-1)
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[numeric_cols_to_scale] = scaler.fit_transform(df[numeric_cols_to_scale])

print(f"\n✓ Scaling completado (MinMaxScaler)")
print(f"  - Rango: [0, 1]")

df = df_scaled
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="documentación-y-comentarios"></a>
## Documentación y Comentarios

### 1. Estilo de Comentarios
```python
# ✅ Comentarios claros y descriptivos

# Análisis de distribución de precios
# Se observa sesgo positivo, con concentración en rango medio

# ❌ Comentarios vagos
# Haciendo cosas
# Análisis
```

### 2. Docstrings para Funciones
```python
# ✅ Docstring completo
def eliminar_outliers(df: pd.DataFrame, column: str, factor: float = 1.5) -> pd.DataFrame:
    """
    Elimina outliers de una columna usando el método IQR.

    Args:
    -----------
    df : DataFrame con los datos
    column : Nombre de la columna a procesar
    factor : Factor multiplicador del IQR para definir límites

    Returns:
    --------
        DataFrame sin los outliers de la columna especificada

    Example:
    --------
    >>> df_clean = eliminar_outliers(df, 'price', factor=1.5)
    >>> print(f"Registros removidos: {len(df) - len(df_clean)}")
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - factor * IQR
    upper = Q3 + factor * IQR

    return df[(df[column] >= lower) & (df[column] <= upper)]
```

### 3. Markdown en Celdas
```markdown
# ✅ Celdas markdown bien estructuradas

## 🔍 Análisis de Duplicados

**Objetivo:** Identificar y eliminar registros duplicados

**Estrategia:**
1. Detectar duplicados completos (todas las columnas)
2. Detectar duplicados por columnas clave (model, year, price)
3. Eliminar manteniendo el primer registro

**Criterios:**
- Duplicado completo: todas las columnas iguales
- Duplicado clave: model + year + price iguales
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="visualizaciones"></a>
## Visualizaciones

### 1. Estilo Estándar
```python
# ✅ Configuración estándar para gráficos

plt.figure(figsize=(12, 6))

# Tu gráfico aquí
plt.plot(x, y)

# Elementos obligatorios
plt.title('Título Descriptivo del Gráfico', fontsize=14, fontweight='bold')
plt.xlabel('Etiqueta Eje X', fontsize=12)
plt.ylabel('Etiqueta Eje Y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 2. Paleta de Colores
```python
# ✅ Usar paletas predefinidas
sns.set_palette("husl")
# O
sns.color_palette("viridis")

# ❌ Evitar colores arbitrarios
colors = ['#FF5733', '#123456', '#ABCDEF']
```

### 3. Ejemplos de Gráficos Estándar
```python
# Histograma
plt.figure(figsize=(12, 6))
plt.hist(df['price'], bins=50, edgecolor='black', alpha=0.7)
plt.title('Distribución de Precios', fontsize=14)
plt.xlabel('Precio (€)', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(12, 6))
df.boxplot(column='mileage')
plt.title('Boxplot: Kilometraje', fontsize=14)
plt.ylabel('Kilometraje (km)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Heatmap de correlación
plt.figure(figsize=(12, 10))
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
            square=True, linewidths=0.5)
plt.title('Matriz de Correlación', fontsize=14)
plt.tight_layout()
plt.show()
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="funciones-reutilizables"></a>
## Funciones Reutilizables

### Librería de Funciones Comunes
```python
# ========================================
# FUNCIONES AUXILIARES
# ========================================

def print_section(title: str):
    """
        Imprime un separador visual para secciones
    """
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def analyze_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza valores nulos en el DataFrame

    Args:
    -----------
    df : DataFrame a analizar

    Returns:
    --------
        Resumen de valores nulos por columna
    """
    null_counts = df.isnull().sum()
    null_percentages = (null_counts / len(df) * 100).round(2)

    null_summary = pd.DataFrame({
        'Columna': null_counts.index,
        'Valores_Nulos': null_counts.values,
        'Porcentaje': null_percentages.values
    }).sort_values('Valores_Nulos', ascending=False)

    return null_summary[null_summary['Valores_Nulos'] > 0]


def detect_outliers_iqr(df: pd.DataFrame, column: str, factor: float = 1.5) -> tuple:
    """
    Detecta outliers usando el método IQR

    Args:
    -----------
    df : DataFrame con los datos
    column : Nombre de la columna
    factor : Factor multiplicador de IQR

    Returns:
    --------
        (lower_bound, upper_bound, n_outliers, outlier_indices)
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - factor * IQR
    upper_bound = Q3 + factor * IQR

    outlier_mask = (df[column] < lower_bound) | (df[column] > upper_bound)
    n_outliers = outlier_mask.sum()
    outlier_indices = df[outlier_mask].index

    return lower_bound, upper_bound, n_outliers, outlier_indices


def remove_outliers(df: pd.DataFrame, column: str, factor: float = 1.5) -> pd.DataFrame:
    """
    Elimina outliers de una columna usando IQR

    Args:
    -----------
    df : DataFrame con los datos
    column : Nombre de la columna
    factor : Factor multiplicador de IQR

    Returns:
    --------
        DataFrame sin outliers en la columna especificada
    """
    lower, upper, _, _ = detect_outliers_iqr(df, column, factor)
    return df[(df[column] >= lower) & (df[column] <= upper)]


def compare_distributions(df_before: pd.DataFrame, df_after: pd.DataFrame, column: str) -> None:
    """
    Compara distribuciones antes y después de limpieza

    Args:
    -----------
    df_before : DataFrame original
    df_after : DataFrame después de limpieza
    column : Columna a comparar
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Antes
    axes[0].hist(df_before[column], bins=50, edgecolor='black', alpha=0.7)
    axes[0].set_title(f'Antes: {column}')
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Frecuencia')
    axes[0].grid(True, alpha=0.3)

    # Después
    axes[1].hist(df_after[column], bins=50, edgecolor='black', alpha=0.7, color='green')
    axes[1].set_title(f'Después: {column}')
    axes[1].set_xlabel(column)
    axes[1].set_ylabel('Frecuencia')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def calculate_retention_rate(df_original: pd.DataFrame, df_clean: pd.DataFrame) -> float:
    """
    Calcula tasa de retención de datos

    Args:
    -----------
    df_original : DataFrame original
    df_clean : DataFrame limpio

    Returns:
    --------
        Tasa de retención en porcentaje
    """
    return (len(df_clean) / len(df_original)) * 100


def generate_summary_report(df_original: pd.DataFrame, df_final: pd.DataFrame) -> None:
    """
    Genera reporte resumen del proceso de limpieza

    ParametArgsers:
    -----------
    df_original : DataFrame original
    df_final : DataFrame final limpio
    """
    print_section("RESUMEN DEL PROCESO DE LIMPIEZA")

    print(f"\n📊 MÉTRICAS GENERALES")
    print(f"  • Registros iniciales: {len(df_original):,}")
    print(f"  • Registros finales: {len(df_final):,}")
    print(f"  • Registros eliminados: {len(df_original) - len(df_final):,}")
    print(f"  • Tasa de retención: {calculate_retention_rate(df_original, df_final):.2f}%")

    print(f"\n📊 ESTRUCTURA")
    print(f"  • Columnas iniciales: {df_original.shape[1]}")
    print(f"  • Columnas finales: {df_final.shape[1]}")
    print(f"  • Columnas añadidas: {df_final.shape[1] - df_original.shape[1]}")

    print(f"\n📊 CALIDAD DE DATOS")
    print(f"  • Valores nulos iniciales: {df_original.isnull().sum().sum():,}")
    print(f"  • Valores nulos finales: {df_final.isnull().sum().sum():,}")
    print(f"  • Duplicados iniciales: {df_original.duplicated().sum():,}")
    print(f"  • Duplicados finales: {df_final.duplicated().sum():,}")
```

**[⬆ back to top](#tabla-de-contenidos)**

---

<a id="checklist-final"></a>
## Checklist Final

### ✅ Antes de Crear tu Pull Request

```markdown
## 📋 Checklist de Calidad

### Estructura
- [ ] Notebook sigue la plantilla de secciones
- [ ] Todas las secciones tienen título en mayúsculas
- [ ] Celdas markdown entre secciones de código

### Código
- [ ] Nombres de variables según estándares (df, df_clean, etc.)
- [ ] Nombres de columnas en inglés
- [ ] Funciones tienen docstrings
- [ ] Código comentado en español
- [ ] Sin variables genéricas (x, y, temp, data)

### Análisis
- [ ] Análisis exploratorio completo
- [ ] Detección de duplicados
- [ ] Análisis de valores nulos
- [ ] Detección de outliers
- [ ] Feature engineering implementado

### Visualizaciones
- [ ] Todas las gráficas tienen título
- [ ] Ejes etiquetados correctamente
- [ ] Uso de paletas de colores estándar
- [ ] Grid habilitado (alpha=0.3)

### Documentación
- [ ] Celdas markdown explicativas
- [ ] Comentarios claros en código complejo
- [ ] Resumen al final del notebook
- [ ] Métricas de retención calculadas

### Resultados
- [ ] Dataset final sin nulos
- [ ] Dataset final sin duplicados
- [ ] Variables codificadas correctamente
- [ ] Variables escaladas (si aplica)
- [ ] CSV final generado

### Git
- [ ] Commits con mensajes descriptivos
- [ ] Solo tu notebook en tu rama
- [ ] No modificaste archivos de otros
- [ ] No modificaste data/raw/bmw_pricing_v3.csv
```

---

## 📞 Contacto y Soporte

Si tienes dudas sobre estos estándares:

1. **Revisar ejemplos** en este documento
2. **Consultar en el grupo** de WhatsApp
3. **Crear issue** en GitHub con tag `[STANDARDS]`
4. **Discutir en reunión** de equipo

---

## 🔄 Actualizaciones

Este documento puede ser actualizado por consenso del equipo.

**Última actualización:** Noviembre 2025  
**Versión:** 1.0

---

**[⬆ back to top](#tabla-de-contenidos)**

<div align="center">

**¡Sigamos estos estándares para un código limpio y profesional!**

🚗 BMW Pricing Project - Data Engineering 🚗

</div>