# 📘 Guía: Trabajar con Notebooks en VS Code

**Sin necesidad de instalar Jupyter**

---

## ✅ Ventajas de VS Code para Notebooks

- ✅ No necesitas instalar Jupyter por separado
- ✅ Interfaz integrada con Git
- ✅ Autocompletado inteligente
- ✅ Ver cambios de Git mientras programas
- ✅ Terminal integrada para comandos Git
- ✅ Todo en un solo lugar

---

## 🔧 Setup Inicial (Una Sola Vez)

### 1. Instalar VS Code

**Mac:**
```bash
# Desde terminal
brew install --cask visual-studio-code
```

**Windows:**
Descargar de: https://code.visualstudio.com/

**Linux:**
```bash
# Desde terminal
sudo snap install code --classic
```

### 2. Instalar Python

**Verificar si ya lo tienes:**
```bash
# Desde terminal
python3 --version
```

Si no lo tienes:
- **Mac:** `brew install python`
- **Windows:** https://www.python.org/downloads/
- **Linux:** Ya suele venir instalado

### 3. Abrir tu Proyecto en VS Code

```bash
# Desde terminal
cd entregable_1_data_engineering
code .
```

### 4. Primera Vez Abriendo un Notebook

Cuando abras tu primer `.ipynb`:

1. VS Code detectará que es un notebook
2. Te pedirá instalar la extensión de Python → **Instalar**
3. Esperará a que se instale (30 segundos)
4. El notebook se abrirá automáticamente

---

## 💻 Trabajar con Notebooks en VS Code

### Abrir un Notebook

```bash
# Desde terminal
code notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# O en VS Code:
# File → Open → navegar a tu .ipynb
```

### Interfaz del Notebook

```
┌─────────────────────────────────────────────────────┐
│ archivo.ipynb                         [X] Run All                 ← Barra superior
├─────────────────────────────────────────────────────┤
│
│ [ ] # Celda 1: Imports                         [▶]                   ← Celda de código
│     import pandas as pd
│     import numpy as np
│
│ ✓ Executed in 0.5s                                                        ← Status
│ ┌──────────────────────────────────────────────┐
│ │ (output aquí)                                                            ← Output
│ └──────────────────────────────────────────────┘
│
│ [ ] # Celda 2: Carga de datos                 [▶]
│     df = pd.read_csv('data/raw/bmw_pricing_v3.csv')
│
└─────────────────────────────────────────────────────┘
```

### Ejecutar Celdas

**Método 1: Click en el botón ▶**
- Cada celda tiene un botón ▶ a la izquierda
- Click para ejecutar esa celda

**Método 2: Atajos de teclado (RECOMENDADO)**
```
Shift + Enter  →  Ejecutar celda y pasar a la siguiente
Ctrl/Cmd + Enter  →  Ejecutar celda sin moverte
```

**Método 3: Run All**
- Click en "Run All" en la barra superior
- Ejecuta todas las celdas en orden

### Ver Outputs

Los outputs aparecen **directamente debajo de cada celda**:
- Tablas de pandas se ven bien formateadas
- Gráficos de matplotlib/seaborn se muestran inline
- Print statements aparecen como texto

### Añadir Nuevas Celdas

**Botones entre celdas:**
- Hover entre dos celdas
- Aparecen botones: `+ Code` y `+ Markdown`
- Click para añadir nueva celda

**Atajos de teclado:**
```
A  →  Añadir celda arriba (Above)
B  →  Añadir celda abajo (Below)
```

### Tipo de Celda

**Code:** Para código Python
```python
import pandas as pd
df = pd.read_csv('file.csv')
```

**Markdown:** Para documentación
```markdown
# Título
## Subtítulo
- Lista
**Negrita**
```

Cambiar tipo: Click en el selector en la celda

---

## 🔄 Workflow Completo en VS Code

### 1. Actualizar Repo (Antes de Trabajar)

**Opción A: Usar terminal integrada en VS Code**
```bash
# Abrir terminal: Ctrl/Cmd + `
git fetch --all
git checkout develop
git pull origin develop
git checkout feature/tu-nombre_dev
git merge develop
```

**Opción B: Usar Git integrado de VS Code**
1. Click en icono de Source Control (lateral izquierdo)
2. Click en los 3 puntos (···)
3. Pull → Fetch → Merge

### 2. Trabajar en tu Notebook

```bash
# Abrir notebook
code notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# Programar:
# - Ejecutar celdas con Shift+Enter
# - Añadir nuevas celdas con A/B
# - Ver outputs inmediatamente
# - Guardar con Cmd/Ctrl+S
```

### 3. Ver Cambios (Git Diff)

VS Code muestra cambios en tiempo real:

```
┌─────────────────────────────────────────┐
│ TU_NOMBRE_APELLIDO.ipynb         M                  ← M = Modified
├─────────────────────────────────────────┤
│ Source Control
│   Changes (1)
│   └─ notebooks_individuales/
│      └─ TU_NOMBRE_APELLIDO.ipynb  M
└─────────────────────────────────────────┘
```

Click en el archivo para ver el diff.

### 4. Guardar y Hacer Commit

**Opción A: Terminal integrada**
```bash
git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
git commit -m "Tu nombre: descripción breve"
git push
```

**Opción B: Source Control UI**
1. Click en Source Control (icono lateral)
2. Stage Changes (+ en el archivo)
3. Escribir mensaje de commit arriba
4. Click en ✓ Commit
5. Click en ··· → Push

---

## 🆚 VS Code vs Colab vs Jupyter

| Característica | VS Code | Colab | Jupyter |
|----------------|---------|-------|---------|
| Instalación | Fácil | No requiere | Media |
| Trabajo offline | ✅ Sí | ❌ No | ✅ Sí |
| Git integrado | ✅ Sí | ❌ No | ❌ No |
| Gratis | ✅ Sí | ✅ Sí | ✅ Sí |
| GPU gratis | ❌ No | ✅ Sí | ❌ No |
| Curva aprendizaje | Baja | Baja | Media |

**Recomendación:**
- **Colab:** Si no quieres instalar nada o necesitas GPU
- **VS Code:** Si quieres todo integrado y trabajar offline
- **Jupyter:** Si ya lo tienes instalado y estás cómodo

---

## 🚨 Troubleshooting

### "No Kernel Found"

**Solución:**
```bash
# En terminal:
pip install ipykernel

# Luego en VS Code:
# Ctrl/Cmd+Shift+P → "Python: Select Interpreter"
# Elegir tu versión de Python
```

### "Import Error: No module named pandas"

**Solución:**
```bash
# En terminal y con el entorno virtual activado:
# Instalar dependencias
pip install pandas numpy matplotlib seaborn scikit-learn

# O usar requirements.txt:
pip install -r requirements.txt
```

### Las Celdas No se Ejecutan

**Solución:**
1. Verificar que hay un kernel seleccionado (arriba a la derecha)
2. Click en el selector de kernel
3. Elegir Python 3.x
4. Esperar a que se conecte
5. Intentar ejecutar de nuevo

### No Aparecen los Gráficos

**Solución:**
Añadir al inicio del notebook:
```python
%matplotlib inline
```

---

## 📝 Tips y Atajos

### Atajos de Teclado Esenciales

```
Shift + Enter    →  Ejecutar celda y pasar a siguiente
Ctrl/Cmd + Enter →  Ejecutar celda sin moverte
A                →  Nueva celda arriba
B                →  Nueva celda abajo
DD               →  Eliminar celda (presionar D dos veces)
Z                →  Deshacer eliminación
M                →  Convertir a Markdown
Y                →  Convertir a Code
Ctrl/Cmd + /     →  Comentar/descomentar línea
Ctrl/Cmd + S     →  Guardar
```

### Comandos Útiles

```python
# Ver todas las variables
%whos

# Limpiar outputs
# Click derecho en celda → Clear Cell Output

# Ver documentación
?función
# Ejemplo: ?pd.read_csv

# Medir tiempo de ejecución
%timeit función()
```

---

## 🎯 Ventajas para el Proyecto

1. **Git integrado:** Ves cambios en tiempo real
2. **Terminal integrada:** No cambias de ventana para git
3. **Mismo editor:** Código y notebooks en un lugar
4. **Más rápido:** No subir/bajar de Colab
5. **Trabajo offline:** No necesitas internet

---

## 🔗 Enlaces Útiles

- [VS Code Docs: Jupyter Notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [VS Code Tips and Tricks](https://code.visualstudio.com/docs/getstarted/tips-and-tricks)

---

<div align="center">

**¿Prefieres VS Code o Colab?**

Ambos funcionan perfectamente. Elige el que más te guste.

🚗 BMW Pricing Project 🚗

</div>