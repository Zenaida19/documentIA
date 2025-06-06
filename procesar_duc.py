import os
import PyPDF2
import docx

def extraer_texto(ruta):
    if ruta.endswith('.pdf'):
        with open(ruta, 'rb') as f:
            lector = PyPDF2.PdfReader(f)
            texto = ""
            for pagina in lector.pages:
                texto += pagina.extract_text() or ""
            return texto
    elif ruta.endswith('.docx'):
        doc = docx.Document(ruta)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""
