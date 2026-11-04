"""P03 Cálculo de una consigna. Variante a.
La consigna se calcula a partir de una expresión recibida de un operador. El contrato admite números y operaciones +, -, *, /, con paréntesis; no admite llamadas a funciones.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

def calcular(expresion):
    return eval(expresion)
