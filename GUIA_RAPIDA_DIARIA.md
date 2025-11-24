# 🚀 Guía Rápida: Comandos Diarios para Trabajar

**Para usar con Google Colab**

---

## 📋 Antes de Empezar a Trabajar (CADA VEZ)

### Paso 1: Actualizar tu Repositorio Local

```bash
# 1. Ir al directorio del proyecto
cd entregable_1_data_engineering

# 2. Ver en qué rama estás
git branch
# Debe mostrar * en feature/TU-NOMBRE_dev

# 3. Guardar cualquier cambio que tengas (si los hay)
git status  # Ver qué has cambiado
git add .   # Si hay cambios que guardar
git commit -m "Tu nombre: guardando progreso actual"

# 4. Actualizar TODAS las referencias remotas
git fetch --all

# 5. Traer cambios de develop a tu rama local
git checkout develop
git pull origin develop

# 6. Volver a tu rama personal
git checkout feature/TU-NOMBRE_dev
# Ejemplo para Gabriela:
# git checkout feature/gabriela_dev

# 7. Integrar cambios de develop en tu rama
git merge develop
# Si no hay conflictos, dirá "Already up to date" o hará merge automático
```

**⏱️ Tiempo estimado: 1-2 minutos**

---

## 💻 Trabajar en el Código

### Opción A: Google Colab (MÁS COMÚN)

```bash
# 1. Abrir Google Colab en el navegador
# https://colab.research.google.com/

# 2. File → Upload notebook

# 3. Navegar a tu proyecto local:
# entregable_1_data_engineering/notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# 4. Trabajar en Colab normalmente

# 5. Cuando termines: File → Download → Download .ipynb

# 6. Guardar en tu carpeta local:
# entregable_1_data_engineering/notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
# (Reemplazar el archivo existente)
```

### Opción B: VS Code (SI LO TIENES)

```bash
# 1. Abrir el notebook en VS Code
code notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# 2. VS Code abre el notebook automáticamente
# - Ejecutar celdas con Shift+Enter
# - Ver outputs directamente
# - Guardar con Cmd/Ctrl+S

# 3. Los cambios se guardan automáticamente al archivo
```

### Opción C: Jupyter (SI LO TIENES INSTALADO)

```bash
jupyter notebook notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
```

**Recomendación:** Usa Colab si no tienes Jupyter o VS Code configurado.

---

## 💾 Guardar y Subir tus Cambios (AL TERMINAR DE TRABAJAR)

### Paso 4: Hacer Commit y Push

```bash
# 1. Ver qué archivos has modificado
git status
# Debe mostrar: modified: notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# 2. Añadir tus cambios
git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb

# 3. Hacer commit con mensaje descriptivo
git commit -m "Tu nombre: descripción breve"
# Ejemplos:
# git commit -m "Gabriela: análisis exploratorio completado"
# git commit -m "Jorge: limpieza de duplicados implementada"
# git commit -m "Alexis: tratamiento de outliers finalizado"

# 4. Subir a GitHub (primera vez)
git push -u origin feature/TU-NOMBRE_dev

# 5. Siguientes veces (ya configurado)
git push
```

**⏱️ Tiempo estimado: 30 segundos**

---

## 📊 Resumen Visual del Flujo

```
🔄 ANTES DE TRABAJAR:
┌─────────────────────────────────────────┐
│ 1. git fetch --all
│ 2. git checkout develop
│ 3. git pull origin develop
│ 4. git checkout feature/tu-nombre_dev
│ 5. git merge develop
└─────────────────────────────────────────┘
          ↓
💻 DURANTE EL TRABAJO (elige una):
┌─────────────────────────────────────────┐
│ OPCIÓN A: Google Colab
│ 1. Subir .ipynb a Colab
│ 2. Programar en Colab
│ 3. Descargar .ipynb de Colab
│ 4. Guardar en notebooks_individuales/
│
│ OPCIÓN B: VS Code
│ 1. code notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
│ 2. Programar directamente
│ 3. Guardar (Cmd/Ctrl+S)
│
│ OPCIÓN C: Jupyter (si lo tienes)
│ 1. jupyter notebook TU_NOMBRE_APELLIDO.ipynb
│ 2. Programar
│ 3. Guardar
└─────────────────────────────────────────┘
          ↓
💾 AL TERMINAR:
┌─────────────────────────────────────────┐
│ 1. git add .
│ 2. git commit -m "Tu nombre: descripción breve"
│ 3. git push
└─────────────────────────────────────────┘
```

---

## 🆘 Comandos de Emergencia

### Ver en qué rama estás
```bash
git branch
```

### Cambiar a tu rama si te equivocaste
```bash
git checkout feature/TU-NOMBRE_dev
```

### Descartar cambios locales no guardados
```bash
# ⚠️ CUIDADO: Esto borra cambios no commiteados
git checkout -- notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
```

### Ver qué has cambiado
```bash
git status
git diff notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
```

### Ver historial de commits
```bash
git log --oneline -10
```

---

## 📅 Workflow Semanal Recomendado

### Lunes (inicio de semana)
```bash
# Actualizar todo
git fetch --all
git checkout develop
git pull origin develop
git checkout feature/tu-nombre_dev
git merge develop
```

### Martes - Jueves (desarrollo)
```bash
# Al inicio del día:
git fetch --all
git checkout develop
git pull origin develop
git checkout feature/tu-nombre_dev
git merge develop

# Trabajar en Colab...

# Al final del día:
git add .
git commit -m "Tu nombre: progreso del día"
git push
```

### Viernes (revisión)
```bash
# Commit final de la semana
git add .
git commit -m "Tu nombre: avance semanal completado"
git push

# Crear PR si terminaste tu parte
# (Ver guía de PR en README.md)
```

---

## ✅ Checklist Diario

**Antes de empezar:**
- `git fetch --all`
- `git checkout develop`
- `git pull origin develop`
- `git checkout feature/tu-nombre_dev`
- `git merge develop`

**Durante el trabajo:**
- Subir notebook a Colab
- Programar y probar
- Descargar notebook actualizado

**Al terminar:**
- `git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb`
- `git commit -m "Tu nombre: descripción breve"`
- `git push`

---

## 🎯 Comandos por Integrante

### Gabriela Alberico
```bash
git checkout feature/gabriela_dev
git push origin feature/gabriela_dev
# Notebook: notebooks_individuales/gabriela_alberico.ipynb
```

### Jorge Silva
```bash
git checkout feature/jorge_dev
git push origin feature/jorge_dev
# Notebook: notebooks_individuales/jorge_silva.ipynb
```

### Robert Tunzi
```bash
git checkout feature/robert_dev
git push origin feature/robert_dev
# Notebook: notebooks_individuales/robert_tunzi.ipynb
```

### Matias Lannes
```bash
git checkout feature/matias_dev
git push origin feature/matias_dev
# Notebook: notebooks_individuales/matias_lannes.ipynb
```

### Alexis Labrador
```bash
git checkout feature/alexis_dev
git push origin feature/alexis_dev
# Notebook: notebooks_individuales/alexis_labrador.ipynb
```

---

## 📱 Contacto

Si algo falla:
1. **No entrar en pánico** 🧘
2. Captura de pantalla del error
3. Compartir en el grupo
4. Alguien del equipo te ayuda

---

## 🔗 Enlaces Útiles

- **Repo GitHub**: https://github.com/alexisnlh/entregable_1_data_engineering
- **Google Colab**: https://colab.research.google.com/
- **README Completo**: Ver en el repo
- **Estándares de Código**: Ver CODING_STANDARDS.md

---

<div align="center">

**¡Recuerda: git fetch --all antes de trabajar!**

🚗 BMW Pricing Project 🚗

</div>