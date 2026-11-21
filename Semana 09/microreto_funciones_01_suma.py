"""Microreto independiente: sumar tiempos con una función y un acumulador."""
print("Hola Munco")
ESPERAS = [12, 20, 18]


def sumar_esperas(minutos, total = 0):
    """Devuelve la suma de los minutos recibidos en horas."""
    #total = 0
    
    #total_sum = sum(minutos)

    for minuto in minutos:
        # TODO: acumule cada minuto en total.
        pass

    return total

#TODO: llame a la función sumar_esperas y guarde el resultado en una variable. Luego, imprima el resultado en horas.

#sumar_esperas([12, 18, 20])
total = sumar_esperas(ESPERAS)
print(sumar_esperas(ESPERAS))

totales = []
totales.append(sumar_esperas([20,60,20,30,]))
totales.append(sumar_esperas([10,60,180,20]))
#sumar_esperas(12, 18, 20)