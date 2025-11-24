# ⚡ Git Cheat Sheet - Comandos Esenciales
**Proyecto BMW - Data Engineering**

---

## 🔄 ANTES DE TRABAJAR (Cada día)

```bash
cd entregable_1_data_engineering
git fetch --all
git checkout develop
git pull origin develop
git checkout feature/TU-NOMBRE_dev
git merge develop
```

---

## 💻 TRABAJAR EN EL CÓDIGO

**Opción A: Google Colab**
1. https://colab.research.google.com/
2. **File → Upload** tu `.ipynb`
3. Programar
4. **File → Download**
5. Guardar en `notebooks_individuales/`

**Opción B: VS Code**
1. `code notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb`
2. Programar (se guarda automático)

**Opción C: Jupyter** (si lo tienes)
1. `jupyter notebook TU_NOMBRE_APELLIDO.ipynb`

---

## 💾 GUARDAR CAMBIOS (Al terminar)

```bash
git status
git add notebooks_individuales/TU_NOMBRE_APELLIDO.ipynb
git commit -m "Tu nombre: descripción breve"
git push
```

---

## 🚨 SOS - Comandos de Emergencia

| Problema | Solución |
|----------|----------|
| ¿En qué rama estoy? | `git branch` |
| Cambiar a mi rama | `git checkout feature/TU-NOMBRE_dev` |
| ¿Qué he cambiado? | `git status` |
| Descartar cambios | `git checkout -- TU_NOMBRE_APELLIDO.ipynb` |
| Error al push | `git pull` primero |

---

## 🎯 Reglas de Oro

1. **NUNCA** trabajes en `main` directamente
2. **SIEMPRE** haz `git fetch --all` antes de trabajar
3. **SIEMPRE** commitea con `"tu nombre: mensajes descriptivos"`
4. **NUNCA** modifiques `data/raw/bmw_pricing_v3.csv`
5. **SOLO** edita tu propio notebook

---

**Repo:** https://github.com/alexisnlh/entregable_1_data_engineering

**Ayuda:** Preguntar en el grupo de WhatsApp