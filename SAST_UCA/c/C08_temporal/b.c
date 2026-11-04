/* C08 Creación de un archivo de mantenimiento. Variante b.
El programa crea y elimina un archivo temporal vacío. Se plantea para Linux y un directorio temporal compartido.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#define _DEFAULT_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
int main(void) {
    char nombre[] = "/tmp/uca-XXXXXX";
    if (mktemp(nombre) == NULL || nombre[0] == '\0') return 1;
    FILE *f = fopen(nombre, "w");
    if (f == NULL) return 1;
    fclose(f);
    return unlink(nombre) != 0;
}
