"""P02 Diagnóstico de un dispositivo. Variante a.
El usuario introduce el nombre del dispositivo. El servicio muestra ese nombre mediante un proceso auxiliar. El directorio de trabajo pertenece al laboratorio.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import subprocess
import sys


def diagnosticar(nombre, directorio):
    return subprocess.run(
        [sys.executable, "-c", "import sys; print(sys.argv[1])", nombre],
        shell=False, cwd=directorio, capture_output=True,
        text=True, timeout=5, check=True,
    ).stdout.strip()
