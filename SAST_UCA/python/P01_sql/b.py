"""P01 Consulta de equipos. Variante b.
El identificador de cliente procede de la sesión autenticada. El filtro serial lo escribe el usuario. Solo deben devolverse equipos de su cliente.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

def consultar(db, cliente, serial):
    consulta = (
        "SELECT serial, cliente, informe FROM equipos "
        "WHERE cliente = ? AND serial = ?"
    )
    return db.execute(consulta, (cliente, serial)).fetchall()
