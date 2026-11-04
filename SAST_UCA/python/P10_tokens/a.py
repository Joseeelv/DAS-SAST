"""P10 Generación de tokens de recuperación. Variante a.
Un servicio genera un token de recuperación. Se estudia únicamente su generación; el almacenamiento, la expiración y el uso único son responsabilidad del servicio.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import secrets
def crear_token():
    return secrets.token_urlsafe(32)
