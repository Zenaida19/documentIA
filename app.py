from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

# Configuración general
app = Flask(__name__)
app.secret_key = 'clave_secreta_dre'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear carpeta de subida si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Función auxiliar para validar extensión
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#rutassss
# Ruta principal (index)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de la página de carga
@app.route('/cargar')
def cargar():
    return render_template('cargar.html')

# Ruta que recibe y procesa el archivo
@app.route('/procesar_documento', methods=['POST'])
def procesar_documento():
    if 'documento' not in request.files:
        flash('No se ha enviado ningún archivo')
        return redirect(url_for('cargar'))

    archivo = request.files['documento']

    if archivo.filename == '':
        flash('Nombre de archivo vacío')
        return redirect(url_for('cargar'))

    if archivo and allowed_file(archivo.filename):
        filename = secure_filename(archivo.filename)
        ruta_completa = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        archivo.save(ruta_completa)

        # Aquí se procesa con el modelo de IA
        resultado = clasificar_documento(ruta_completa)

        flash(f'Resultado del análisis: {resultado}')
        return redirect(url_for('cargar'))
    else:
        flash('Formato de archivo no permitido. Solo PDF o Word.')
        return redirect(url_for('cargar'))

# Simulación del modelo de clasificación
def clasificar_documento(filepath):
    # Aquí podrías leer el archivo y usar un modelo real
    return "Clasificado como Pedagogía - Aprobado"

#inicio del servidorr
if __name__ == '__main__':
    app.run(debug=True)
