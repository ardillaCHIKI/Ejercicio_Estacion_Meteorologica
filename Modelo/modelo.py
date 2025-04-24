import gradio as gr

try:
    with open("key.key", "rb") as key_file:
        key = key_file.read()
except FileNotFoundError:
    key = gr.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

cipher_suite = gr(key)

class EstacionMeteorologica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos_encriptados = []

    def registrar_datos(self, datos):
        encrypted_data = cipher_suite.encrypt(datos.encode())
        self.datos_encriptados.append(encrypted_data)

    def obtener_datos(self):
        return [cipher_suite.decrypt(d).decode() for d in self.datos_encriptados]