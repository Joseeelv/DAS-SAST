"""P08 Almacenamiento de contraseñas. Variante a.
El atacante obtiene una copia de los valores almacenados, no las contraseñas originales. Debe evaluarse el coste de probar candidatos y el uso de una sal por contraseña. Las credenciales de la demostración son ficticias.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import hashlib
import hmac
import secrets

ITERACIONES = 600_000


def derivar(clave, sal):
    datos = clave.encode("utf-8")
    if len(datos) > 1024:
        raise ValueError("Contraseña demasiado larga")
    return hashlib.pbkdf2_hmac("sha256", datos, sal, ITERACIONES)


def guardar(clave):
    sal = secrets.token_bytes(16)
    return sal.hex() + ":" + derivar(clave, sal).hex()


def comprobar(clave, almacenado):
    try:
        sal_hex, huella_hex = almacenado.split(":")
        sal, huella = bytes.fromhex(sal_hex), bytes.fromhex(huella_hex)
        if len(sal) != 16 or len(huella) != 32:
            return False
        return hmac.compare_digest(derivar(clave, sal), huella)
    except (ValueError, TypeError):
        return False
