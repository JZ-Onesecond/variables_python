# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número decimal a operar:')
francotirador_beta = int(input())

print('Ingrese por consola el segundo número decimal a operar:')
francotirador_omega = int(input())

# Alumno: Imprima en pantalla los dos números decimales solicitados
# print(....)

print('la cantidad de objetivos eliminados por el francotirador_beta es:', francotirador_beta)
print('la cantidad de objetivos eliminados por el francotirador_omega es:',francotirador_omega)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma

objetivos_eliminados = francotirador_beta + francotirador_omega
print('total de objetivos eliminados por ambos francotiradores es:', objetivos_eliminados )

# Resta

objetivos_fallidos = francotirador_beta - francotirador_omega
print('total de enemigos fallidos por ambos francotiradores es:', objetivos_fallidos)

# División

objetivos_capturados = francotirador_beta / francotirador_omega
print('los objetivos capturados por ambos francotiradores son:', objetivos_capturados)

# Multiplicación

objetivos_localizados = francotirador_beta * francotirador_omega
print('objetivos localizados por ambos francotiradores son:', objetivos_localizados)

# total de objetivos divisados 

objetivos_divisados = objetivos_localizados + objetivos_capturados + objetivos_eliminados + objetivos_fallidos
print('el total de objetivos divisados por nuestros francotiradores es:', objetivos_divisados)

print('gracias')