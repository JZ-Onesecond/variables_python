# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
mision_1 = str(input())

print('Ingrese palabra 2:')
mision_2 = str(input())

operacion_cerro = mision_1[0:3]
print(operacion_cerro)

operacion_rio = mision_2[0:2]
print(operacion_rio)

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados

operacion_reconocimiento = operacion_cerro + operacion_rio
print(operacion_reconocimiento)