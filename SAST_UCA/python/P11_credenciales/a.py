"""P11 Credenciales de una pasarela. Variante a.
Una pasarela necesita una contraseña de servicio. Todas las cadenas incluidas son ficticias. El proceso recibe su entorno de un administrador confiable.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

PASSWORD = "clave_ficticia_del_laboratorio"
def autenticar(cliente):
    return cliente.login("servicio", PASSWORD)
