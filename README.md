# Entregable 1 | Data Engineering
# 🚗 BMW Pricing - Data Engineering & Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Proyecto completo de **Data Engineering** para limpieza, análisis exploratorio y preparación de datos de precios de vehículos BMW, con el objetivo de construir un modelo predictivo de precios.

<a id="tabla-de-contenidos"></a>
## 📋 Tabla de Contenidos

- [Integrantes](#integrantes)
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación y Setup Inicial](#instalación-y-setup-inicial)
- [Workflow de Trabajo en Equipo](#workflow-de-trabajo-en-equipo)
- [Comandos Git por Integrante](#comandos-git-por-integrante)
- [Estándares de Código](#estándares-de-código)
- [Uso](#uso)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Protección de Ramas](#protección-de-ramas)
- [Licencia](#licencia)
- [Contacto](#contacto)

<a id="integrantes"></a>
## 👥 Integrantes
- **Gabriela Alberico** - [GitHub](https://github.com/albericog) | Rama: `feature/gabriela_dev`
- **Jorge Silva** - [GitHub](https://github.com/jsilvazuniga) | Rama: `feature/jorge_dev`
- **Robert Tunzi** - [GitHub](https://github.com/rtunzi) | Rama: `feature/robert_dev`
- **Matias Lannes** - [GitHub](https://github.com/matilannes) | Rama: `feature/matias_dev`
- **Alexis Labrador** - [GitHub](https://github.com/alexisnlh) | Rama: `feature/alexis_dev`

### Metodología de Trabajo

```
📚 Fase Individual → 👥 Revisión Colectiva → 📝 Integración Final → ✅ Entrega
```

1. **Desarrollo Individual**: Cada integrante implementa el proceso completo de limpieza en su rama.
2. **Notebooks Individuales**: Cada uno trabaja en `notebooks_individuales/nombre_apellido.ipynb`.
3. **Revisión en Equipo**: Reuniones para comparar enfoques y decidir mejores prácticas.
4. **Integración**: Construcción del `entregable_final.ipynb` con el código seleccionado.
5. **Merge a Main**: Pull Request final tras aprobación del equipo.

<a id="descripción-del-proyecto"></a>
## 🎯 Descripción del Proyecto

Este proyecto forma parte del **Entregable 1: Data Engineering** del [Máster en Data Science & AI de Nuclio Digital School](https://nuclio.school/master-data-science/). El objetivo es realizar un proceso completo de limpieza y preprocesado de datos de vehículos BMW para preparar el dataset para modelado predictivo de precios.

### Objetivos

- ✅ Realizar limpieza exhaustiva del dataset
- ✅ Análisis exploratorio de datos (EDA)
- ✅ Tratamiento de valores nulos y outliers
- ✅ Feature engineering
- ✅ Preparación para modelado ML

<a id="estructura-del-proyecto"></a>
## 📁 Estructura del Proyecto

```
entregable_1_data_engineering/
├── .gitignore                                          # Archivos ignorados por Git
├── README.md                                  # Este archivo
├── CODING_STANDARDS.md         # Guía de estándares de código (LEER ANTES DE EMPEZAR)
├── LICENSE                                        # Licencia MIT del proyecto
├── requirements.txt                              # Dependencias Python
├── entregable_final.ipynb                    # ⭐ Notebook final para entregar
├── data/
│   ├── raw/                                           # ⚠️ SOLO LECTURA - NO MODIFICAR
│   │   └── bmw_pricing_v3.csv          # Dataset original
│   └── processed/
│       └── bmw_pricing_cleaned.csv     # Dataset limpio (resultado final)
└── notebooks_individuales/                 # Trabajo individual de cada miembro
    ├── gabriela_alberico.ipynb
    ├── jorge_silva.ipynb
    ├── roberto_tunzi.ipynb
    ├── matias_lannes.ipynb
    └── alexis_labrador.ipynb
```

### ⚠️ Reglas Importantes

- `data/raw/bmw_pricing_v3.csv` es **INMUTABLE** - solo lectura
- Cada integrante trabaja SOLO en su propio notebook individual
- El `entregable_final.ipynb` se construye al final mediante consenso del equipo

**[⬆ back to top](#tabla-de-contenidos)**

<a id="instalación-y-setup-inicial"></a>
## 🔧 Instalación y Setup Inicial

### Requisitos Previos

- Python 3.8 o superior
- Git instalado y configurado
- Cuenta de GitHub
- Acceso al repositorio (haber aceptado la invitación de colaborador)

### Setup Paso a Paso (TODOS los Integrantes)

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/alexisnlh/entregable_1_data_engineering.git

# Entrar al directorio
cd entregable_1_data_engineering
```

#### 2. Verificar Estructura y Ramas
```bash
# Ver en qué rama estás (debería ser main)
git branch

# Ver todas las ramas (remotas y locales)
git branch -a

# Actualizar referencias remotas
git fetch --all
```

#### 3. Crear Entorno Virtual (Recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate

# En Windows:
venv\Scripts\activate
```

#### 4. Instalar Dependencias
```bash
# Instalar todas las librerías necesarias
pip install -r requirements.txt

# Configurar nbdime para notebooks (opcional - ayuda con diffs)
# Si falla, no pasa nada, es opcional
pip install nbdime
nbdime config-git --enable
```

**Nota:** Como trabajaremos en **Google Colab**, las librerías ya están preinstaladas en Colab. Este paso es opcional y solo necesario si quieres ejecutar notebooks localmente.

**[⬆ back to top](#tabla-de-contenidos)**

<a id="workflow-de-trabajo-en-equipo"></a>
## 🔄 Workflow de Trabajo en Equipo

### Estructura de Ramas

```
main (protegida - solo mediante PR con 2 aprobaciones)
├── develop (protegida - solo mediante PR con 1 aprobación)
│   ├── feature/gabriela_dev
│   ├── feature/jorge_dev
│   ├── feature/robert_dev
│   ├── feature/matias_dev
│   └── feature/alexis_dev
└── feature/entregable-final (se crea al final)
```

### Proceso General

```
1. Cada integrante crea su rama personal desde develop
2. Trabaja en su notebook individual de forma independiente
3. Hace commits regulares a su rama
4. Crea Pull Request hacia develop cuando termina
5. El equipo revisa en reunión todos los notebooks
6. Se decide qué código usar para el entregable final
7. Se crea feature/entregable-final con el código unificado
8. PR final hacia main con el entregable completo
```

<a id="comandos-git-por-integrante"></a>
## 💻 Comandos Git por Integrante

### 🟢 Setup Inicial (Primera Vez - TODOS)

Después de clonar el repositorio:
```bash
# 1. Asegurarte de estar en develop
git checkout develop
git pull origin develop

# 2. Crear TU rama personal (usa TU nombre)
# Para Gabriela:
git checkout -b feature/gabriela_dev

# Para Jorge:
git checkout -b feature/jorge_dev

# Para Robert:
git checkout -b feature/robert_dev

# Para Matias:
git checkout -b feature/matias_dev

# Para Alexis:
git checkout -b feature/alexis_dev

# 3. Verificar que estás en tu rama
git branch
# Debe mostrar un * en tu rama
```

### 📝 Crear tu Notebook Individual (Primera Vez)

**Opción A: Google Colab (RECOMENDADO - Lo usaremos)**
```bash
# 1. Ir a Google Colab
# https://colab.research.google.com/

# 2. File → New notebook

# 3. Empezar a programar siguiendo CODING_STANDARDS.md

# 4. Al terminar: File → Download → Download .ipynb

# 5. Guardar el archivo descargado en tu proyecto local:
# entregable_1_data_engineering/notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
# Ejemplos:
#   - gabriela_alberico.ipynb
#   - jorge_silva.ipynb
#   - robert_tunzi.ipynb
#   - matias_lannes.ipynb
#   - alexis_labrador.ipynb

# 6. Hacer commit del notebook
cd entregable_1_data_engineering
git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
git commit -m "Tu nombre: notebook inicial creado"
git push
```

**Opción B: Local con Jupyter (Opcional)**
```bash
# Si prefieres trabajar localmente:
jupyter notebook

# En el navegador:
# 1. Navegar a notebooks_individuales/
# 2. New → Python 3
# 3. Guardar como: TU_NOMBRE_APELLIDO.ipynb
```

**⚠️ Importante para Colab:**
- Cada vez que trabajes, sube el notebook a Colab
- Al terminar, descárgalo y guárdalo en `notebooks_individuales/`
- Haz commit de la versión descargada
- NO dejes el notebook solo en Colab sin guardar localmente

**[⬆ back to top](#tabla-de-contenidos)**

### 💾 Guardar Cambios (Uso Diario con Google Colab)
```bash
# ========================================
# CICLO COMPLETO: COLAB → LOCAL → GITHUB
# ========================================

# 1. Subir tu notebook a Google Colab
# - Ir a https://colab.research.google.com/
# - File → Upload notebook
# - Seleccionar: notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# 2. Trabajar en Colab
# - Programar siguiendo CODING_STANDARDS.md
# - Probar y ejecutar celdas
# - Verificar resultados

# 3. Descargar desde Colab
# - File → Download → Download .ipynb
# - Guardar en: entregable_1_data_engineering/notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
# - (Reemplazar el archivo existente)

# 4. En tu terminal local: Ver cambios
git status

# 5. Añadir tus cambios
git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
# O añadir todo:
git add .

# 6. Hacer commit con mensaje descriptivo
git commit -m "Tu nombre: descripción breve del cambio"
# Ejemplos:
# git commit -m "Gabriela: análisis exploratorio inicial completado"
# git commit -m "Jorge: implementación de limpieza de duplicados"
# git commit -m "Robert: tratamiento de valores nulos finalizado"

# 7. Subir a GitHub (primera vez en la rama)
git push -u origin feature/TU-NOMBRE_dev

# 8. Siguientes veces (ya configurado)
git push
```

**⏱️ Frecuencia recomendada:**
- Commits: Al menos 1-2 por sesión de trabajo
- Push: Al final de cada sesión de trabajo
- No esperes semanas para hacer commit/push

### 🔄 Sincronizar con Develop (Cada Pocos Días)

Para traer cambios que otros hayan hecho:
```bash
# 1. Guardar tu trabajo actual
git add .
git commit -m "Tu nombre: guardando progreso actual"

# 2. Ir a develop
git checkout develop

# 3. Actualizar develop local
git pull origin develop

# 4. Volver a tu rama
git checkout feature/TU-NOMBRE_dev

# 5. Traer cambios de develop a tu rama
git merge develop

# Si hay conflictos (raro en notebooks individuales):
# - Resuelve en VS Code o Jupyter
# - git add .
# - git commit -m "Tu nombre: merge con develop"

# 6. Subir los cambios
git push
```

### 📤 Crear Pull Request (Al Terminar tu Trabajo)
```bash
# 1. Asegurarte de que todo está subido
git status  # Debe decir "nothing to commit, working tree clean"
git push

# 2. Ir a GitHub en el navegador:
# https://github.com/alexisnlh/entregable_1_data_engineering

# 3. Verás un banner amarillo que dice:
# "feature/TU-NOMBRE_dev had recent pushes"
# Click en "Compare & pull request"

# 4. Configurar la PR:
# Base: develop ← Compare: feature/TU-NOMBRE_dev
# Título: "Tu Nombre: Notebook limpieza completo"
# Descripción:
"""
## Resumen
Implementación completa del proceso de limpieza de datos BMW.

## Contenido del Notebook
- [ ] Carga de datos
- [ ] Análisis exploratorio
- [ ] Limpieza de duplicados
- [ ] Tratamiento de valores nulos
- [ ] Detección y tratamiento de outliers
- [ ] Feature engineering
- [ ] Generación de dataset limpio

## Resultados Principales
- Registros iniciales: X
- Registros finales: Y
- Porcentaje de retención: Z%

## Próximos Pasos
Listo para revisión en reunión de equipo.
"""

# 5. Click "Create pull request"
```

**[⬆ back to top](#tabla-de-contenidos)**

### 👀 Revisar Pull Request de un Compañero
```bash
# 1. Descargar todas las actualizaciones
git fetch --all

# 2. Cambiar a la rama del compañero
# Ejemplo: revisar el trabajo de Gabriela
git checkout feature/gabriela_dev
```

**Opción A: Revisar con VS Code (RECOMENDADO)**
```bash
# 4. Abrir el notebook en VS Code
code notebooks_individuales/gabriela_alberico.ipynb

# En VS Code:
# - Se abre automáticamente con el visor de notebooks
# - Click en "Run All" en la parte superior
# - Verificar que corre sin errores
# - Revisar outputs y gráficos
```

**Opción B: Revisar con Google Colab**
```bash
# 4. Subir el notebook a Colab
# - Ir a https://colab.research.google.com/
# - File → Upload notebook
# - Seleccionar: notebooks_individuales/gabriela_alberico.ipynb
# - Runtime → Run all
# - Verificar ejecución
```

**Opción C: Revisar con Jupyter (Si lo tienes instalado)**
```bash
# 4. Abrir con Jupyter
jupyter notebook notebooks_individuales/gabriela_alberico.ipynb
# Cell → Run All
```

**Verificar:**
- ✅ ¿Corre sin errores?
- ✅ ¿Los resultados tienen sentido?
- ✅ ¿El código sigue CODING_STANDARDS.md?
- ✅ ¿Hay comentarios claros?

**5. Dejar feedback en GitHub:**
- Ir a la PR en GitHub
- Files changed → comentar líneas específicas
- Review changes → Approve o Request changes

**6. Volver a tu rama:**
```bash
git checkout feature/TU-NOMBRE_dev
```

**[⬆ back to top](#tabla-de-contenidos)**

### 🎯 Fase Final - Entregable Unificado (UNO del Equipo)

Cuando ya todos terminaron y se decidió qué código usar:
```bash
# 1. Asegurarse de tener todo actualizado
git checkout develop
git pull origin develop

# 2. Crear rama para el entregable final
git checkout -b feature/entregable-final
```

**Opción A: Trabajar en VS Code (RECOMENDADO)**
```bash
# 3. Abrir el notebook final en VS Code
code entregable_final.ipynb

# En VS Code:
# - El notebook se abre automáticamente
# - Ir construyendo celda por celda con el código decidido
# - Ejecutar celdas con Shift+Enter
# - Ver outputs en tiempo real
```

**Opción B: Trabajar en Google Colab**
```bash
# 3. Subir a Colab
# - Ir a https://colab.research.google.com/
# - File → Upload notebook → entregable_final.ipynb
# - Ir construyendo con el código decidido
# - Al terminar: File → Download → Download .ipynb
# - Guardar reemplazando: entregable_final.ipynb
```

**Opción C: Trabajar en Jupyter (Si lo tienes)**
```bash
# 3. Abrir con Jupyter
jupyter notebook entregable_final.ipynb
```

**4. Ir construyendo el notebook con el código decidido:**
```python
# (Ver archivo CODING_STANDARDS.md para convenciones)

# Ejemplo de integración:
# ========================================
# CELDA 2: Carga de Datos
# ========================================
# Código de Gabriela (decidido en reunión)
df = pd.read_csv('data/raw/bmw_pricing_v3.csv', encoding='utf-8')

# ========================================
# CELDA 5: Eliminación de Duplicados
# ========================================
# Código de Robert (decidido en reunión)
df_clean = df.drop_duplicates(subset=['model', 'year', 'price'])
# ...
```

**5. Commits frecuentes:**
```bash
git add entregable_final.ipynb
git commit -m "Entregable: secciones 1-3 completadas"
git push -u origin feature/entregable-final

# Seguir trabajando y commiteando...
git add entregable_final.ipynb
git commit -m "Entregable: secciones 4-6 completadas"
git push
```

**6. Crear PR hacia develop:**
- En GitHub: Base: `develop` ← Compare: `feature/entregable-final`

**7. Todo el equipo revisa y aprueba**

**8. Merge a develop**

**9. Crear PR final hacia main:**
- En GitHub: Base: `main` ← Compare: `develop`

**10. Todos aprueban (mínimo 2 aprobaciones requeridas)**

**11. Merge a main → ¡Entregable listo! 🎉**

### 🚨 Comandos de Emergencia

#### Si te equivocaste de rama:
```bash
# Ver en qué rama estás
git branch

# Cambiar a la correcta
git checkout feature/TU-NOMBRE_dev
```

#### Si quieres descartar cambios no guardados:
```bash
# Ver qué has cambiado
git status

# Descartar cambios en UN archivo
git checkout -- notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# Descartar TODOS los cambios (⚠️ CUIDADO - no se puede deshacer)
git reset --hard HEAD
```

#### Si quieres ver diferencias antes de commit:
```bash
# Ver cambios en notebooks (con nbdime)
nbdiff notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# O ver en formato web
nbdiff-web notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
```

**[⬆ back to top](#tabla-de-contenidos)**

<a id="estándares-de-código"></a>
## 📏 Estándares de Código

**⚠️ IMPORTANTE**: Antes de empezar a programar, **TODOS deben leer el archivo [CODING_STANDARDS.md](CODING_STANDARDS.md)**

Este archivo contiene:
- Convenciones de nombres de variables
- Estructura del notebook
- Funciones estándar a usar
- Ejemplos de código
- Plantillas de documentación

Seguir estos estándares asegura que el código de todos sea similar y fácil de integrar.

<a id="uso"></a>
## 🚀 Uso

### Ejecutar el Notebook Final

**Opción A: VS Code (RECOMENDADO)**
```bash
# 1. Abrir el notebook en VS Code
code entregable_final.ipynb

# En VS Code:
# - El notebook se abre automáticamente con el visor integrado
# - Click en "Run All" en la barra superior
# - O ejecutar celda por celda con Shift+Enter
# - Los outputs se muestran debajo de cada celda
```

**Opción B: Google Colab**
```bash
# 1. Ir a Google Colab
# https://colab.research.google.com/

# 2. File → Upload notebook
# Seleccionar: entregable_final.ipynb

# 3. Runtime → Run all
# O ejecutar celda por celda con Shift+Enter
```

**Opción C: Jupyter Notebook (Si lo tienes instalado)**
```bash
# Activar entorno virtual (si usas uno)
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows

# Abrir Jupyter
jupyter notebook entregable_final.ipynb

# Ejecutar todas las celdas: Cell → Run All
```

Este archivo se crea al ejecutar la última celda del notebook.

### Requisitos para VS Code

Para trabajar con notebooks en VS Code, necesitas:

1. **Extensión de Python** (se instala automáticamente al abrir un .ipynb)
2. **Python 3.8+** instalado en tu sistema

```bash
# Verificar versión de Python
python --version
# o
python3 --version
```

VS Code detectará automáticamente tu instalación de Python y podrás ejecutar los notebooks sin instalar Jupyter por separado.

**[⬆ back to top](#tabla-de-contenidos)**

<a id="tecnologías-utilizadas"></a>
## 🛠️ Tecnologías Utilizadas

### Lenguajes y Frameworks

- **Python 3.8+** - Lenguaje principal
- **Pandas 1.5+** - Manipulación de datos
- **NumPy 1.24+** - Operaciones numéricas
- **Matplotlib 3.7+** - Visualizaciones
- **Seaborn 0.12+** - Visualizaciones estadísticas

### Herramientas de Desarrollo

- **Jupyter Notebook** - Análisis interactivo
- **Git/GitHub** - Control de versiones y colaboración
- **VS Code** - IDE recomendado
- **nbdime** - Diff y merge de notebooks

### Librerías de Machine Learning

```python
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from scipy import stats
```

<a id="protección-de-ramas"></a>
## 🔒 Protección de Ramas

### Rama `main`
- ✅ Requiere Pull Request
- ✅ Mínimo 2 aprobaciones
- ✅ Todas las conversaciones deben estar resueltas
- ✅ Historial lineal
- ❌ No permite push directo
- ❌ No permite force push
- ❌ No permite eliminación

### Rama `develop`
- ✅ Requiere Pull Request
- ✅ Mínimo 1 aprobación
- ✅ Todas las conversaciones deben estar resueltas
- ❌ No permite push directo

### Proceso de Pull Request

1. Crear PR hacia la rama correspondiente
2. Esperar aprobaciones requeridas
3. Resolver todos los comentarios
4. Solo entonces se habilita el botón de merge

**[⬆ back to top](#tabla-de-contenidos)**

<a id="licencia"></a>
## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

**Alexis Labrador** - [@alexisnlh](https://www.linkedin.com/in/alexisnlh/)

**Link del Proyecto:** [https://github.com/alexisnlh/entregable_1_data_engineering.git](https://github.com/alexisnlh/entregable_1_data_engineering.git)

---

## 📚 Referencias y Recursos

### Documentación Oficial
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)

### Guías de Estilo
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### Recursos de Aprendizaje
- [Data Cleaning Best Practices](https://towardsdatascience.com/data-cleaning-in-python-the-ultimate-guide-2020-c63b88bf0a0d)
- [Exploratory Data Analysis Guide](https://www.kaggle.com/code/startupsci/titanic-data-science-solutions)

### Git y GitHub
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

## 🙏 Agradecimientos

- **Nuclio Digital School** por el programa del Máster en Data Science & AI
- **Profesores y mentores** por la guía durante el proyecto
- **Stack Overflow Community** por resolver dudas técnicas
- **Desarrolladores de librerías open source** utilizadas en este proyecto

## 🤝 Contribuciones

Este es un proyecto académico cerrado. Si tienes sugerencias o encuentras errores, por favor:

1. Abre un Issue en GitHub
2. Describe el problema o sugerencia
3. El equipo lo revisará en la próxima reunión

---

## ⭐ Valoración del Proyecto

Si este proyecto te resultó útil para aprender Data Engineering, considera:
- ⭐ Darle una estrella en GitHub
- 🔄 Compartirlo con compañeros
- 💬 Dejar feedback en Issues

---

**[⬆ back to top](#tabla-de-contenidos)**

<div align="center">

**Made with ❤️ and Python**

*Proyecto académico - Máster en Data Science & AI - Nuclio Digital School - 2025*

</div>