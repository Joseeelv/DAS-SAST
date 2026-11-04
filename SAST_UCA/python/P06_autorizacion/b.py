"""P06 Acceso a partes de mantenimiento. Variante b.
cliente_sesion lo establece el servidor tras autenticar al usuario. El usuario puede modificar parte_id. Cada parte pertenece a un único cliente. Cambiar un identificador no concede acceso a los datos de otro cliente.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

def obtener(partes, cliente_sesion, parte_id):
    parte = partes.get(parte_id)
    if parte is None:
        raise LookupError("Parte no disponible")
    return dict(parte)
