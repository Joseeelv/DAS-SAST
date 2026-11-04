"""P09 Importación de telemetría. Variante a.
Se importa un mensaje de hasta 4096 bytes enviado por un sensor no confiable. Solo se necesita un objeto con un valor numérico. La alternativa usa JSON codificado en UTF-8.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import pickle
def importar(datos):
    return pickle.loads(datos)
