/* J05 Validación de una cadena de símbolos. Variante a.
Una petición solo debe contener de 1 a 64 letras a. Analiza el coste del patrón sin realizar pruebas con cadenas largas.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function validar(texto) {
    return typeof texto === "string" && texto.length <= 64 && /^a+$/.test(texto);
}
module.exports = { validar };
