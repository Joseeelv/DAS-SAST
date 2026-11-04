/* C01 Inicialización de un identificador. Variante a.
Un componente en C inicializa un buffer de ocho bytes. Se analiza el límite de la escritura. Un fallo en un proceso aislado no demuestra por sí solo ejecución remota en un dispositivo.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdio.h>

int main(void) {
    char identificador[8];
    for (unsigned i = 0; i <= sizeof identificador; i++) {
        identificador[i] = '\0';
    }
    printf("%s", identificador);
    return 0;
}
