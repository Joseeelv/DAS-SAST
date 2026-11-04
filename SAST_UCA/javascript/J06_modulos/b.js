/* J06 Selección de un módulo de cálculo. Variante b.
El usuario elige la operación suma o máximo. La aplicación solo necesita esas dos operaciones, nunca cargar código elegido por el usuario.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function operar(nombre, valores) {
    if (!Array.isArray(valores) || valores.length === 0 || valores.length > 64 ||
        !valores.every(Number.isFinite)) throw new Error("Valores");
    if (nombre === "suma") return valores.reduce((a, b) => a + b, 0);
    if (nombre === "maximo") return Math.max(...valores);
    throw new Error("Operación no admitida");
}
module.exports = { operar };
