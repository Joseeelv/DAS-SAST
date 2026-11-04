/* J09 Consulta HTTPS de una pasarela. Variante b.
La URL es HTTPS y está fijada por un administrador. Se usa el almacén de CA del sistema. El ejemplo no realiza peticiones mientras se analiza.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const https = require("node:https");
function consultar(url, callback) {
    if (new URL(url).protocol !== "https:") throw new Error("HTTPS requerido");
    return https.get(url, { rejectUnauthorized: true }, callback);
}
module.exports = { consultar };
