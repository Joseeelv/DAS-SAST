/* J03 Lectura de un informe del dispositivo. Variante a.
El usuario escoge informe por nombre. El directorio es confiable, no contiene enlaces simbólicos controlados por el usuario y no cambia durante la lectura.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const fs = require("node:fs");
const path = require("node:path");
function leer(base, nombre) {
    const raiz = path.resolve(base);
    const destino = path.resolve(raiz, nombre);
    const relativa = path.relative(raiz, destino);
    if (!relativa || relativa === ".." || relativa.startsWith(".." + path.sep) ||
        path.isAbsolute(relativa)) throw new Error("Fuera del directorio");
    return fs.readFileSync(destino, "utf8");
}
module.exports = { leer };
