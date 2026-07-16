# Mejorador de Imagenes

## Trabajo Práctico para la materia
# Técnicas de Procesamiento Digital de Imágenes

# Descripción del TP:
A través de la implementación de distintas técnicas de procesamiento de imágenes, este proyecto busca mejorar una imagen antigua o de mala calidad, aumentando brillo, pasando a escala de grises, obteniendo los bordes, eliminando el fondo, etc.

# 🖼️ Mejorador de Imágenes

Aplicación web desarrollada con **Astro** y **Flask** que permite aplicar distintos filtros y transformaciones sobre imágenes de forma sencilla desde el navegador.

## ✨ Funcionalidades

Actualmente la aplicación permite:

- 📈 Mejorar la calidad de la imagen.
- 🖤 Convertir imágenes a escala de grises.
- 🟤 Aplicar efecto sepia.
- ✂️ Eliminar el fondo de una imagen.
- 📐 Detectar bordes.

## 🛠️ Tecnologías utilizadas

### Frontend
- Astro
- HTML
- CSS
- JavaScript
- Node.js 22 o superior

### Backend
- Python 3.10 o superior
- Flask
- OpenCV
- NumPy
- Pillow
- rembg (para eliminación de fondo)

---

# 📁 Estructura del proyecto

```
tp_proc_img2/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── astro.config.mjs
│
└── README.md
```

---

# ⚙️ Instalación

## 1. Clonar el proyecto

```bash
git clone <URL_DEL_REPOSITORIO>

cd tp_proc_img2
```

---

## 2. Instalar el Backend

Ingresar a la carpeta:

```bash
cd backend
```

### Crear un entorno virtual

Windows

```bash
python -m venv venv
```

Activarlo

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, instalar manualmente:

```bash
pip install flask
pip install flask-cors
pip install opencv-python
pip install numpy
pip install pillow
pip install rembg
pip install pillow-avif-plugin
```
ó
```bash
pip install flask flask-cors opencv-python pillow rembg pillow-avif-plugin
```
---

## Ejecutar el servidor Flask

```bash
python app.py
```

El servidor quedará disponible en:

```
http://localhost:5000
```

---

# Instalar el Frontend

Abrir una nueva terminal.

Ingresar a la carpeta del frontend:

```bash
cd frontend
```

Instalar las dependencias:

```bash
npm install
```

Iniciar Astro:

```bash
npm run dev
```

La aplicación estará disponible en:

```
http://localhost:4321
```

---

# 🚀 Uso de la aplicación

1. Abrir el navegador en:

```
http://localhost:4321
```

2. En la pantalla principal se mostrarán las herramientas disponibles.

3. Seleccionar el filtro que se desea aplicar.

4. Presionar **Seleccionar imagen** y elegir una imagen desde el equipo.

5. Esperar a que finalice el procesamiento.

6. Visualizar el resultado obtenido.

7. Descargar la imagen procesada (si la funcionalidad está habilitada).

---

# 📸 Procesamientos disponibles

| Herramienta | Descripción |
|-------------|-------------|
| Mejorar calidad | Incrementa la nitidez y mejora la apariencia de la imagen. |
| Escala de grises | Convierte la imagen a tonos de gris. |
| Sepia | Aplica un efecto fotográfico antiguo. |
| Detección de bordes | Detecta los contornos principales de la imagen mediante visión artificial. |
| Eliminar fondo | Remueve automáticamente el fondo de la imagen. |

---

# 👨‍💻 Autores

Proyecto desarrollado como trabajo práctico de la materia Técnicas de Procesamiento Digital de Imágenes.

Alumnas:
- Natalia Barrón | Cecilia Campos
---

# 📄 Licencia

Proyecto desarrollado únicamente con fines educativos.