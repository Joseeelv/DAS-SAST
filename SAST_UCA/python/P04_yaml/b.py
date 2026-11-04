"""P04 Importación de configuración. Variante b.
Se recibe un archivo YAML de mantenimiento. Debe contener un mapa de valores simples. No se permite reconstruir objetos ni ejecutar operaciones durante su lectura.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import yaml


def cargar(texto):
    return yaml.load(texto, Loader=yaml.Loader)
