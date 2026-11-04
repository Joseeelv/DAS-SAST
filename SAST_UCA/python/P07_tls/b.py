"""P07 Descarga de un manifiesto. Variante b.
Un dispositivo descarga un manifiesto HTTPS desde un destino configurado por el administrador. La CA autorizada se configura localmente. Este paquete revisa la configuración TLS por análisis estático; no levanta servidores.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import requests


def descargar(url, ca_autorizada):
    if not url.startswith("https://"):
        raise ValueError("Se requiere HTTPS")
    respuesta = requests.get(url, verify=str(ca_autorizada), timeout=3)
    respuesta.raise_for_status()
    return respuesta.text
