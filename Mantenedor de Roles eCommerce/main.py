import time
from dotenv import load_dotenv
from pageObjects.interaccionWeb import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from pageObjects.config import *
from pageObjects.interaccionWeb import *
from pageObjects import registroProceso
from pageObjects.registroProceso import registroProceso
from pageObjects.envioCorreo import EnvioCorreo
from pageObjects.descargaArchivo import *

def main():

# INICIALIZAR EL DRIVER
    load_dotenv()

    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    CONTAINER_NAME = os.getenv('CONTAINER_NAME')
    DIRECTORIO_LOCAL = directorio_local
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    descargaArchivo = DescargaArchivo(CONNECTION_STRING, CONTAINER_NAME, DIRECTORIO_LOCAL)
    blob_mas_reciente = descargaArchivo.obtener_blob_mas_reciente()    
    if blob_mas_reciente:
        descargaArchivo.descargar_blob(blob_mas_reciente)
        nombreArchivo = os.path.basename(blob_mas_reciente)
        print(nombreArchivo)  

    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url_qa_login)
    user = os.getenv('USUARIO_LOGIN')
    password = os.getenv('CONTRASEÑA_LOGIN')
    file_path = rf'{DIRECTORIO_LOCAL}/{nombreArchivo}'
    registroP = registroProceso(DIRECTORIO_LOCAL, f"Resultado_{nombreArchivo}", f"Mantencion_ejecutivos.xlsx")
    interaccionW = InteraccionWeb(driver, registroP)
    driver.maximize_window()
    interaccionW.login(user, password)
    driver.get(url_qa_mantenedor)
    time.sleep(5)

    interaccionW.crear_rol(file_path)
    interaccionW.modificar_rol(file_path)
    interaccionW.desactivar_activar_rol(file_path)

    html_body = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .container {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #4CAF50;
        }
        p {
            color: #333;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Mantención de Roles Completada!</h1>
        <p>La ejecución del <strong>Mantenedor de Roles</strong> se ha completado exitosamente.</p>
        <p>Adjuntamos el archivo con el resultado para su revisión y seguimiento.</p>
        <p>Gracias.</p>
        <p>Equipo Sonnix.</p>
    </div>
</body>
</html>
"""

    EnvioCorreo.enviar_mail(
    "Resultado mantención de roles e-commerce",  # subject
    html_body,  # body
    ["nicolas.cristino@bupa.cl", "florencia.otero@bupa.cl"],  # to_emails
    SMTP_SERVER,  # smtp_server
    SMTP_PORT,  # smtp_port
    SMTP_USERNAME,  # smtp_username
    SMTP_PASSWORD,  # smtp_password
    rf'{DIRECTORIO_LOCAL}\Resultado_{nombreArchivo}', # filePath
    html=True  
)
    EnvioCorreo.enviar_mail(
        "Mantencion de ejecutivos eCommerce", #subject
        "Correo automatico para poder ingresar los roles creados a sus respectivos usuarios", # body
        ["robot.funding@bupa.cl"], # to_emails
        SMTP_SERVER,  # smtp_server
        SMTP_PORT,  # smtp_port
        SMTP_USERNAME,  # smtp_username
        SMTP_PASSWORD,  # smtp_password
        rf'{DIRECTORIO_LOCAL}\Mantencion_ejecutivos.xlsx', # filePath
        html=False
    )

if __name__ == "__main__":
    main()