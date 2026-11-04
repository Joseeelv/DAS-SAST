/* C02 Liberación de un mensaje. Variante a.
Un componente reserva memoria para un mensaje y la libera al finalizar. La presencia de un argumento adicional activa un segundo camino de limpieza. El contrato exige liberar una vez cada reserva.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdlib.h>

int main(int argc, char **argv) {
    (void)argc;
    (void)argv;
    char *mensaje = malloc(32);
    if (mensaje == NULL) return 1;
    free(mensaje);
    return 0;
}
