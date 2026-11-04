/* J03 Lectura de un informe del dispositivo. Variante b.
El usuario escoge informe por nombre. El directorio es confiable, no contiene enlaces simbólicos controlados por el usuario y no cambia durante la lectura.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const fs = require("node:fs");
const path = require("node:path");
function leer(base, nombre) {
    return fs.readFileSync(path.resolve(base, nombre), "utf8");
}
module.exports = { leer };
