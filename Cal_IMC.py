def resultado(peso, altura):

    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = resultado(peso, altura)
print("Su masa corporal totla es:", imc)
