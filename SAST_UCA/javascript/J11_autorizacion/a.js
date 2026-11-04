/* J11 Consulta de un parte de mantenimiento. Variante a.
clienteSesion proviene de una sesión autenticada; id procede del usuario. partes es un Map mantenido por el servidor. Cada parte pertenece a un cliente.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function obtener(partes, clienteSesion, id) {
    const parte = partes.get(id);
    if (!parte || parte.cliente !== clienteSesion) throw new Error("No disponible");
    return { ...parte };
}
module.exports = { obtener };
