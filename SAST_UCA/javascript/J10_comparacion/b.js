/* J10 Comprobación de un token. Variante b.
El servidor guarda un token aleatorio de 64 caracteres hexadecimales. La entrada llega de una petición. Solo se estudia la comparación, no el flujo de autenticación completo.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

const crypto = require("node:crypto");
function verificar(password, esperado) {
    if (typeof password !== "string" || typeof esperado !== "string" ||
        !/^[0-9a-f]{64}$/.test(password) || !/^[0-9a-f]{64}$/.test(esperado)) return false;
    return crypto.timingSafeEqual(Buffer.from(password, "hex"), Buffer.from(esperado, "hex"));
}
module.exports = { verificar };
