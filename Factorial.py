def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(num)

print("El factorial de", num, "es:", resultado)
