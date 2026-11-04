/* J06 Selección de un módulo de cálculo. Variante a.
El usuario elige la operación suma o máximo. La aplicación solo necesita esas dos operaciones, nunca cargar código elegido por el usuario.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function operar(modulo, valores) {
    const operacion = require(modulo);
    return operacion(valores);
}
module.exports = { operar };
