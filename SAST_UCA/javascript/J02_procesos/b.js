/* J02 Diagnóstico de una etiqueta. Variante b.
El servidor muestra una etiqueta mediante un proceso auxiliar. La etiqueta viene de una petición; el ejecutable y el código auxiliar son confiables.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const childProcess = require("node:child_process");
function mostrar(etiqueta, callback) {
    childProcess.execFile(process.execPath,
        ["-e", "console.log(process.argv[1])", "--", etiqueta], callback);
}
module.exports = { mostrar };
