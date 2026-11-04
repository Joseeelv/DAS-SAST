/* J08 Conversión de una etiqueta a bytes. Variante a.
La entrada debe ser una cadena UTF-8 de hasta 64 caracteres. No se admite que un número indique una reserva de memoria.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function convertir(entrada) {
    if (typeof entrada !== "string" || entrada.length > 64) throw new Error("Etiqueta");
    return Buffer.from(entrada, "utf8");
}
module.exports = { convertir };
