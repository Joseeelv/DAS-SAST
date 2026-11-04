/* C05 Vida útil de una lectura. Variante a.
Una lectura se almacena en memoria dinámica. La función devuelve el valor y después deja de necesitar la reserva.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdlib.h>
int leer(void) {
    int *p = malloc(sizeof *p);
    if (p == NULL) return -1;
    *p = 42;
    free(p);
    return *p;
}
