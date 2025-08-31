# asistente/utils.py
import PyPDF2

def extraer_texto_pdf(ruta_pdf):
    texto = ""
    with open(ruta_pdf, "rb") as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            texto += pagina.extract_text() + "\n"
    return texto
