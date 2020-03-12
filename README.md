# Bienvenido a PubliBOT!

PubliBOT es la herramienta de apoyo para la generación para la unidad de Publicidad Chile.

La herramienta está basada en el lenguaje de programación Python (v 3.7), bajo sistema operativo Windows 10 Pro. De la misma manera, se utilizan las siguientes herramientas, extensiones y librerías en el código.

- QtDesigner : Herramienta para generar el diseño de la interfaz gráfica.
- PyQt5: Librería para implementar interfaces gráficas.
- Pdf2image: Librería para convertir archivos .pdf en archivo de imagen. Necesario para hacer la conversión del dashboard de DataStudio.
- cv2: Librería para hacer recorte de imágenes.
- tableauserverclient: Librería para hacer una conexión a un servidor en Tableau.
- requests: Librería que hace las solicitudes REST API.
- pptx: Hace el manejo de presentaciones en Power Point.
- poppler: Hace posible la exportación de pdf2image sin instalación.

### Generación de ejecutable

Es necesario tener instalado *pyinstaller*

- pyinstaller main.py -F --onedir --add-data  "./poppler/*;./poppler" --noupx --noconsole --icon=roboticon.ico
