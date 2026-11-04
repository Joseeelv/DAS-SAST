"""P11 Credenciales de una pasarela. Variante b.
Una pasarela necesita una contraseña de servicio. Todas las cadenas incluidas son ficticias. El proceso recibe su entorno de un administrador confiable.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import os
def autenticar(cliente):
    password = os.environ["PASARELA_PASSWORD"]
    if not password:
        raise ValueError("Falta configurar la credencial")
    return cliente.login("servicio", password)
