/* C07 Copia de una carga de protocolo. Variante a.
Un paquete de entrada contiene 16 bytes. El buffer del componente solo admite ocho; debe rechazarse una carga mayor.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes. */

#include <string.h>
int main(void) {
    unsigned char paquete[16] = {1};
    unsigned char destino[8];
    memcpy(destino, paquete, sizeof paquete);
    return destino[0];
}
