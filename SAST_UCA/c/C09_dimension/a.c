/* C09 Dimensionado de una tabla. Variante a.
La cantidad de registros procede de una cabecera externa. El servicio permite entre 1 y 4096 registros. Estudia el cálculo antes de reservar memoria.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdlib.h>
unsigned *reservar(size_t cantidad) {
    return malloc(cantidad * sizeof(unsigned));
}
