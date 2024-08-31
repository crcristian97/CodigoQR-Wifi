# WiFi QR Code Generator

Este proyecto es una aplicación web sencilla que genera un código QR para una red WiFi a partir del SSID y la contraseña proporcionados. La aplicación utiliza Flask para el backend y HTML, CSS, y JavaScript para el frontend. La biblioteca Toastify se usa para mostrar notificaciones cuando el código QR se genera.

## Requisitos

- Python 3.x
- Flask
- La biblioteca `wifi_qrcode_generator`
- Bibliotecas de frontend: Toastify, etc.

## Instalación

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local:

```bash
git clone (https://github.com/crcristian97/CodigoQR-Wifi.git)
cd your-repository

### 2. Instalar las dependencias:

Crear un entorno virtual 
pip install Flask wifi_qrcode_generator


### 3. Ejecutar la Aplicación

python server.py


### Uso
Introduce el SSID y la contraseña de la red WiFi en el formulario.
Haz clic en el botón "Generate QR Code".
El código QR generado aparecerá en la pantalla y recibirás una notificación indicando que el código ha sido generado.
