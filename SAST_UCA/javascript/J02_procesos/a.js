/* J02 Diagnóstico de una etiqueta. Variante a.
El servidor muestra una etiqueta mediante un proceso auxiliar. La etiqueta viene de una petición; el ejecutable y el código auxiliar son confiables.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const childProcess = require("node:child_process");
function mostrar(etiqueta, callback) {
    childProcess.exec("echo " + etiqueta, callback);
}
module.exports = { mostrar };
