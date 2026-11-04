"""P09 Importación de telemetría. Variante b.
Se importa un mensaje de hasta 4096 bytes enviado por un sensor no confiable. Solo se necesita un objeto con un valor numérico. La alternativa usa JSON codificado en UTF-8.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import json
def importar(datos):
    if not isinstance(datos, bytes) or len(datos) > 4096:
        raise ValueError("Mensaje inválido")
    obj = json.loads(datos)
    if not isinstance(obj, dict) or set(obj) != {"valor"}:
        raise ValueError("Esquema inválido")
    if type(obj["valor"]) not in (int, float) or not -100 <= obj["valor"] <= 100:
        raise ValueError("Valor fuera de rango")
    return obj
