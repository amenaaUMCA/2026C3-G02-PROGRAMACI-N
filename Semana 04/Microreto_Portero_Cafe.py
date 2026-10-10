"""Microreto: el portero del café."""

nombre = input("Como te llamas?: ").upper().strip()
energia = int(input("Cuánta energía tienes de 0 a 100?:"))
trae_cafe = input("Traes café (si/no)?: ").lower().strip() == 'si'

mensaje = ''
# Si menos 50% y no tengo cafe: -> Descansar
if energia < 50 and not(trae_cafe):  # trae_cafe == False
    mensaje = "Acceso denegado: necesitas dormir o tomar café."
# Si 50% o mas o tenga café : -> Puede ingresar a la clase
elif energia >= 50 or trae_cafe:
    mensaje = "Acceso permitido: pasa con gusto pero invite al café."
# Cualquier otro ecenario : Portero confundido : revisar respuestas
else:
    mensaje = "Portero confundido : revisar respuestas"

print(f"{nombre} -> {mensaje}")