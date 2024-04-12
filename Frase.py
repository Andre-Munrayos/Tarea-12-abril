def contar_palabras(frases):
    
    p = frases.split()
    cantidad_p = len(p)
    return cantidad_p

frase = input("Ingrese una frase o palabra: ")
cantidad_p = contar_palabras(frase)
print("La cantidad de palabras en la frase es de:", cantidad_p)
