"""P05 Descarga de informes. Variante a.
El usuario selecciona un nombre de archivo dentro de su directorio de informes. El sistema de archivos no puede ser modificado concurrentemente por ese usuario. Los informes de otros clientes están fuera de la carpeta autorizada.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

from pathlib import Path


def leer(base, nombre):
    return (Path(base) / nombre).read_text(encoding="utf-8")
