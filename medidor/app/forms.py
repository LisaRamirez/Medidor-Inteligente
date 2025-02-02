from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuración del servidor de correo Gmail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "tu_correo@gmail.com"  # Reemplaza con tu correo
SMTP_PASSWORD = "tu_contraseña_de_aplicacion"  # Contraseña de aplicación de Google

@app.route('/', methods=['GET'])
def show_form():
    return render_template('contacto.html')

@app.route('/enviar', methods=['POST'])
def enviar_formulario():
    try:
        # Obtener datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        apr = request.form['apr']
        cargo = request.form['cargo']
        comuna = request.form['comuna']
        arranques = request.form['arranques']
        financiamiento = request.form['financiamiento']
        mensaje = request.form['mensaje']

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = "destino@email.com"  # Reemplaza con el correo destino
        msg['Subject'] = f"Nuevo formulario de contacto de {nombre}"

        # Construir el cuerpo del mensaje
        body = f"""
        Nuevo formulario de contacto recibido:

        Nombre: {nombre}
        Email: {email}
        Teléfono: {telefono}
        APR/SSR: {apr}
        Cargo: {cargo}
        Comuna: {comuna}
        Cantidad de Arranques: {arranques}
        Tipo de Financiamiento: {financiamiento}
        
        Mensaje:
        {mensaje}
        """

        msg.attach(MIMEText(body, 'plain'))

        # Conectar al servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)

        # Enviar correo
        server.send_message(msg)
        server.quit()

        return "Formulario enviado exitosamente"
    except Exception as e:
        return f"Error al enviar el formulario: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)