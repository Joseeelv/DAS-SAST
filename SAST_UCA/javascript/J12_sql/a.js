/* J12 Búsqueda de equipos en SQLite. Variante a.
db implementa prepare().all() de SQLite. clienteSesion es confiable; serial viene de la petición. No se requiere instalar la biblioteca para el análisis estático.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function buscar(db, clienteSesion, serial) {
    const sql = "SELECT * FROM equipos WHERE cliente = " + clienteSesion +
        " AND serial = '" + serial + "'";
    return db.prepare(sql).all();
}
module.exports = { buscar };
