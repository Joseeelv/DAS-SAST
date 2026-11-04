"""P12 Archivo temporal de diagnóstico. Variante a.
Se escribe un informe temporal de un dispositivo en un sistema multiusuario. El archivo se elimina al terminar de procesarlo.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import tempfile
def procesar(texto):
    with tempfile.NamedTemporaryFile(mode="w+", encoding="utf-8") as f:
        f.write(texto)
        f.flush()
        f.seek(0)
        return f.read()
