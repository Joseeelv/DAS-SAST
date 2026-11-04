/* J04 Filtro de nombres de sensores. Variante b.
El requisito es buscar un fragmento literal, con un máximo de 64 caracteres. El usuario no debe aportar una expresión regular.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function coincide(nombre, filtro) {
    if (typeof nombre !== "string" || nombre.length > 256 ||
        typeof filtro !== "string" || filtro.length > 64) throw new Error("Límite");
    return nombre.includes(filtro);
}
module.exports = { coincide };
