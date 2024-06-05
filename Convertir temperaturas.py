#Programa que pueda convertir de centígrados a farenheit y viceversa.


temperatura = float(input("\n Por favor, ingrese una temperatura: "))
variabledeclasificacion = input("\n Ingrese si su temperatura es Celsius (C) o Farenheit (F): ")

#Función para convertir de Farenheit a Centígrados
def convertir_de_Farenheit_a_Centigrados(temperatura):
    temperatura_convertida= (temperatura-32)/1.8
    return temperatura_convertida

#Función para convertir de Centígrados a Farenheit.
def convetir_de_Centigrados_a_Farenheit(temperatura):
    temperatura_convertida = (1.8*temperatura)+32
    return temperatura_convertida

#Procesamiento
if variabledeclasificacion == "C":
    farenheit = convertir_de_Farenheit_a_Centigrados(temperatura)
    print("\n La temperatura es de ",farenheit,"°F.")
elif variabledeclasificacion == "F":
    celsius = convetir_de_Centigrados_a_Farenheit(temperatura)
    print("\n La temperatura es de ",celsius,"°C.")
else:
    print("\n Parámetro no válido, intente de nuevo.")