"""P04 Importación de configuración. Variante a.
Se recibe un archivo YAML de mantenimiento. Debe contener un mapa de valores simples. No se permite reconstruir objetos ni ejecutar operaciones durante su lectura.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import yaml


def cargar(texto):
    if not isinstance(texto, str) or len(texto.encode("utf-8")) > 4096:
        raise ValueError("Configuración demasiado grande")
    datos = yaml.safe_load(texto)
    if not isinstance(datos, dict):
        raise ValueError("Se esperaba un mapa")
    if set(datos) - {"equipo", "umbral"}:
        raise ValueError("Campo no admitido")
    if not isinstance(datos.get("equipo"), str) or len(datos["equipo"]) > 64:
        raise ValueError("Equipo inválido")
    umbral = datos.get("umbral")
    if type(umbral) not in (int, float) or not -100 <= umbral <= 100:
        raise ValueError("Umbral inválido")
    return datos
