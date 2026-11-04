/* C04 Copia de un identificador de sensor. Variante a.
El destino tiene ocho bytes. El literal de entrada representa una etiqueta demasiado larga. La variante alternativa debe rechazarla sin truncarla silenciosamente.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <string.h>
int main(void) {
    char destino[8];
    strcpy(destino, "entrada_demasiado_larga");
    return destino[0];
}
