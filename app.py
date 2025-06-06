from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'clave_secreta_dre'

# Configuración de carga
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar', methods=['GET', 'POST'])
def cargar():
    if request.method == 'POST':
        if 'archivo' not in request.files:
            flash('No se ha seleccionado ningún archivo')
            return redirect(request.url)

        archivo = request.files['archivo']

        if archivo.filename == '':
            flash('Nombre de archivo vacío')
            return redirect(request.url)

        if archivo and allowed_file(archivo.filename):
            nombre_archivo = secure_filename(archivo.filename)
            archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo))
            flash('Archivo cargado correctamente')
            return redirect(url_for('cargar'))

        else:
            flash('Formato de archivo no permitido')
            return redirect(request.url)

    return render_template('cargar.html')

if __name__ == '__main__':
    app.run(debug=True)
