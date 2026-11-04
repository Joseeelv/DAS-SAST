/* J08 Conversión de una etiqueta a bytes. Variante b.
La entrada debe ser una cadena UTF-8 de hasta 64 caracteres. No se admite que un número indique una reserva de memoria.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function convertir(entrada) {
    return new Buffer(entrada);
}
module.exports = { convertir };
