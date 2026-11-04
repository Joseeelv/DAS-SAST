/* J01 Lectura de una configuración numérica. Variante b.
El usuario envía JSON con una propiedad umbral entera entre 0 y 100. No se admiten expresiones JavaScript.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function cargar(texto) {
    if (typeof texto !== "string" || texto.length > 256) throw new Error("Tamaño");
    const datos = JSON.parse(texto);
    if (!datos || Array.isArray(datos) || typeof datos !== "object" ||
        Object.keys(datos).length !== 1 || !Object.hasOwn(datos, "umbral") ||
        !Number.isInteger(datos.umbral) || datos.umbral < 0 || datos.umbral > 100) {
        throw new Error("Esquema");
    }
    return datos;
}
module.exports = { cargar };
