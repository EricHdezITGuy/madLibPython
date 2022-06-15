# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Este proyecto es para aprender a concatenar cadenas de caracteres.
#Supongamos que queremos crear una cadena que diga:
#Aprende a programa con __________.

#Ejemplo:

# organizacion = "freeCodeCamp"
#
# print("Aprende a programar con "+ organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #F-string

#Mad Libs inicia aqui.

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madLib = f"Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madLib)