/* J01 Lectura de una configuración numérica. Variante a.
El usuario envía JSON con una propiedad umbral entera entre 0 y 100. No se admiten expresiones JavaScript.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function cargar(texto) {
    return eval(texto);
}
module.exports = { cargar };
