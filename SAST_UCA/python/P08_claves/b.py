"""P08 Almacenamiento de contraseñas. Variante b.
El atacante obtiene una copia de los valores almacenados, no las contraseñas originales. Debe evaluarse el coste de probar candidatos y el uso de una sal por contraseña. Las credenciales de la demostración son ficticias.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import hashlib
import hmac


def guardar(clave):
    return hashlib.md5(clave.encode("utf-8")).hexdigest()


def comprobar(clave, almacenado):
    return hmac.compare_digest(guardar(clave), almacenado)
