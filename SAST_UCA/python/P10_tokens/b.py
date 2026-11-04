"""P10 Generación de tokens de recuperación. Variante b.
Un servicio genera un token de recuperación. Se estudia únicamente su generación; el almacenamiento, la expiración y el uso único son responsabilidad del servicio.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import random
def crear_token():
    return str(random.randint(100000, 999999))
