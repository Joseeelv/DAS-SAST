/* J10 Comprobación de un token. Variante a.
El servidor guarda un token aleatorio de 64 caracteres hexadecimales. La entrada llega de una petición. Solo se estudia la comparación, no el flujo de autenticación completo.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function verificar(password, esperado) {
    if (password === esperado) return true;
    return false;
}
module.exports = { verificar };
