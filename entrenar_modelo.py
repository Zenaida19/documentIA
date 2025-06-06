import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento
documentos = [
    "manejo de presupuestos, contabilidad, pagos",     # Tesorería
    "experiencia en liquidación de sueldos",           # Tesorería
    "selección de personal, contratos, clima laboral", # RRHH
    "reclutamiento y gestión del talento",             # RRHH
    "experiencia en aula, metodologías activas",       # Pedagogía
    "docente con experiencia en currículo escolar",    # Pedagogía
]
etiquetas = ["tesoreria", "tesoreria", "rrhh", "rrhh", "pedagogia", "pedagogia"]

# Entrenamiento
vectorizador = TfidfVectorizer()
X = vectorizador.fit_transform(documentos)

modelo = MultinomialNB()
modelo.fit(X, etiquetas)

# Guardado
os.makedirs('modelo', exist_ok=True)
joblib.dump(modelo, 'modelo/clasificador.pkl')
joblib.dump(vectorizador, 'modelo/vectorizador.pkl')

print(" Modelo entrenado y guardado en carpeta /modelo/")
