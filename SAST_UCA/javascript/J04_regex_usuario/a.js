/* J04 Filtro de nombres de sensores. Variante a.
El requisito es buscar un fragmento literal, con un máximo de 64 caracteres. El usuario no debe aportar una expresión regular.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function coincide(nombre, filtro) {
    return new RegExp(filtro).test(nombre);
}
module.exports = { coincide };
