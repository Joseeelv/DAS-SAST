/* C08 Creación de un archivo de mantenimiento. Variante a.
El programa crea y elimina un archivo temporal vacío. Se plantea para Linux y un directorio temporal compartido.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#define _DEFAULT_SOURCE
#include <stdlib.h>
#include <unistd.h>
int main(void) {
    char nombre[] = "/tmp/uca-XXXXXX";
    int fd = mkstemp(nombre);
    if (fd == -1) return 1;
    close(fd);
    return unlink(nombre) != 0;
}
