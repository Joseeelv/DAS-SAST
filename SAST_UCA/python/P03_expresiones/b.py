"""P03 Cálculo de una consigna. Variante b.
La consigna se calcula a partir de una expresión recibida de un operador. El contrato admite números y operaciones +, -, *, /, con paréntesis; no admite llamadas a funciones.
Analiza el archivo con SAST; no es necesario ejecutarlo. Compara las dos variantes."""

import ast
import math
import operator

OPERACIONES = {ast.Add: operator.add, ast.Sub: operator.sub,
               ast.Mult: operator.mul, ast.Div: operator.truediv}


def calcular(expresion):
    if not isinstance(expresion, str) or len(expresion) > 120:
        raise ValueError("Expresión fuera del contrato")
    try:
        arbol = ast.parse(expresion, mode="eval")
    except (SyntaxError, RecursionError) as error:
        raise ValueError("Expresión inválida") from error
    if sum(1 for _ in ast.walk(arbol)) > 32:
        raise ValueError("Expresión demasiado compleja")

    def resolver(nodo):
        if isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
            valor = nodo.value
        elif isinstance(nodo, ast.BinOp) and type(nodo.op) in OPERACIONES:
            valor = OPERACIONES[type(nodo.op)](resolver(nodo.left), resolver(nodo.right))
        elif isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, (ast.USub, ast.UAdd)):
            valor = resolver(nodo.operand) * (-1 if isinstance(nodo.op, ast.USub) else 1)
        else:
            raise ValueError("Operación no admitida")
        if not math.isfinite(valor) or abs(valor) > 1_000_000:
            raise ValueError("Resultado fuera de rango")
        return valor

    try:
        return resolver(arbol.body)
    except (ZeroDivisionError, OverflowError) as error:
        raise ValueError("Operación inválida") from error
