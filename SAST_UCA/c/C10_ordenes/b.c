/* C10 Presentación de una etiqueta. Variante b.
Una utilidad debe mostrar literalmente una etiqueta introducida por el operador. No necesita un intérprete de comandos.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdio.h>
#include <stdlib.h>
int mostrar(const char *etiqueta) {
    char comando[256];
    int n = snprintf(comando, sizeof comando, "echo %s", etiqueta);
    if (n < 0 || (size_t)n >= sizeof comando) return 1;
    return system(comando);
}
