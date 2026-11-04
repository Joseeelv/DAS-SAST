"""P05 Descarga de informes. Variante b.
El usuario selecciona un nombre de archivo dentro de su directorio de informes. El sistema de archivos no puede ser modificado concurrentemente por ese usuario. Los informes de otros clientes están fuera de la carpeta autorizada.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

from pathlib import Path


def leer(base, nombre):
    raiz = Path(base).resolve(strict=True)
    destino = (raiz / nombre).resolve(strict=True)
    if not destino.is_relative_to(raiz) or not destino.is_file():
        raise PermissionError("Archivo fuera del directorio autorizado")
    return destino.read_text(encoding="utf-8")
