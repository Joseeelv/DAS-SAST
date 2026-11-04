/* C06 Lectura opcional de una medida. Variante a.
El llamador puede pasar NULL para representar una medida ausente. El contrato exige devolver -1 en ese caso.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stddef.h>
int medida(const int *p) {
    if (p == NULL) return -1;
    return *p;
}
