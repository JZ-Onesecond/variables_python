# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
soldado_1 = str(input())

print('Ingrese palabra 2:')
soldado_2 = str(input())

print('Ingrese palabra 3:')
soldado_3 = str(input())

codigo_enigma = soldado_1[0]
codigo_neutral = soldado_2[0]
codigo_pangea = soldado_3[0]

codigo_universal = codigo_enigma + codigo_neutral + codigo_pangea

print(codigo_universal)


# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
