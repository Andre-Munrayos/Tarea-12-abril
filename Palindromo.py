def palindromo(texto):
    
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

p = input("Ingrese una palabra o frase: ")

if palindromo(p):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
