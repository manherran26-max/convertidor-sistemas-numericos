mapa_hexadecimal = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

valores_hexadecimales = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def base_a_decimal(numero, base):

    numero = numero.upper()

    decimal = 0

    posicion = 0

    for i in range(len(numero) - 1, -1, -1):

        caracter = numero[i]

        if base == 16:
            digito = valores_hexadecimales.get(caracter)
        else:
            digito = int(caracter)

        if digito is None or digito >= base:
            return None

        decimal += digito * (base ** posicion)

        posicion += 1

    return decimal

def decimal_a_base(decimal, base):

    residuos = []

    numero = decimal

    if numero == 0:
        return "0"

    while numero > 0:

        residuo = numero % base

        if base == 16 and residuo >= 10:
            residuos.append(mapa_hexadecimal[residuo])
        else:
            residuos.append(str(residuo))

        numero = numero // base

    residuos.reverse()

    return "".join(residuos)

def convertir(valor, base, bits):

    decimal = base_a_decimal(valor, base)

    if decimal is None:
        return {
            "error": "El valor ingresado no es válido para la base seleccionada."
        }

    maximo = (2 ** bits) - 1

    if decimal > maximo:
        return {
            "error": "Overflow / Desbordamiento de Registro",
            "maximo": maximo
        }

    binario = decimal_a_base(decimal, 2)
    octal = decimal_a_base(decimal, 8)
    hexadecimal = decimal_a_base(decimal, 16)

    binario = binario.zfill(bits)

    digitos_octal = (bits + 2) // 3
    octal = octal.zfill(digitos_octal)

    digitos_hexadecimal = bits // 4
    hexadecimal = hexadecimal.zfill(digitos_hexadecimal)

    return {
        "binario": binario,
        "octal": octal,
        "decimal": str(decimal),
        "hexadecimal": hexadecimal
    }

def operacion_alu(numero1, numero2, operacion):

    if len(numero1) != len(numero2):
        return {
            "error": "Los operandos deben tener la misma cantidad de bits."
        }

    resultado = ""

    for i in range(len(numero1)):

        bit1 = numero1[i]
        bit2 = numero2[i]

        if bit1 not in ["0", "1"] or bit2 not in ["0", "1"]:
            return {
                "error": "Los operandos deben ser números binarios."
            }

        if operacion == "AND":

            if bit1 == "1" and bit2 == "1":
                resultado += "1"
            else:
                resultado += "0"

        elif operacion == "OR":

            if bit1 == "1" or bit2 == "1":
                resultado += "1"
            else:
                resultado += "0"

        elif operacion == "XOR":

            if bit1 != bit2:
                resultado += "1"
            else:
                resultado += "0"

        else:
            return {
                "error": "Operación no válida."
            }

    return {
        "resultado": resultado
    }