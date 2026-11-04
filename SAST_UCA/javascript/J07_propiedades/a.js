/* J07 Actualización de opciones de una pasarela. Variante a.
Se recibe un objeto derivado de JSON. Solo se permite cambiar nombre, una cadena de hasta 64 caracteres, y activo, un booleano.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

function actualizar(config, entrada) {
    for (const clave of Object.keys(entrada)) {
        config[clave] = entrada[clave];
    }
    return config;
}
module.exports = { actualizar };
