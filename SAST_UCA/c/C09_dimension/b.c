/* C09 Dimensionado de una tabla. Variante b.
La cantidad de registros procede de una cabecera externa. El servicio permite entre 1 y 4096 registros. Estudia el cálculo antes de reservar memoria.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdlib.h>
#include <stdint.h>
unsigned *reservar(size_t cantidad) {
    if (cantidad == 0 || cantidad > 4096) return NULL;
    if (cantidad > SIZE_MAX / sizeof(unsigned)) return NULL;
    return calloc(cantidad, sizeof(unsigned));
}
