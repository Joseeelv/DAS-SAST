/* C04 Copia de un identificador de sensor. Variante b.
El destino tiene ocho bytes. El literal de entrada representa una etiqueta demasiado larga. La variante alternativa debe rechazarla sin truncarla silenciosamente.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <stdio.h>
#include <string.h>
int main(void) {
    char destino[8];
    const char *origen = "entrada_demasiado_larga";
    if (strlen(origen) >= sizeof destino) return 1;
    int n = snprintf(destino, sizeof destino, "%s", origen);
    if (n < 0 || (size_t)n >= sizeof destino) return 1;
    return destino[0];
}
