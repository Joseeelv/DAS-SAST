/* C10 Presentación de una etiqueta. Variante a.
Una utilidad debe mostrar literalmente una etiqueta introducida por el operador. No necesita un intérprete de comandos.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdio.h>
int mostrar(const char *etiqueta) {
    return printf("%s\n", etiqueta) < 0;
}
