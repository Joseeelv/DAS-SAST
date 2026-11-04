/* C03 Registro de una etiqueta. Variante b.
Una etiqueta proporcionada por el usuario debe imprimirse literalmente. El laboratorio usa %% para mostrar la interpretación del formato sin leer memoria ni usar %n.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdio.h>

int main(int argc, char **argv) {
    if (argc != 2) return 2;
    printf("%s", argv[1]);
    return 0;
}
