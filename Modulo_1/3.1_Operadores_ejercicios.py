"""
Escribir un programa que solicite dos números y luego imprima:
    1. La suma de los dos números
    2. La resta del primer número menos el segundo 
    3. El producto de los números 
    4. El cubo de la suma de los números
    5. El cociente de la división del primer número por el segundo 
"""
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

Suma = num1 + num2
Resta = num1 - num2
Producto = num1 * num2
Cubo = Suma**3
Cociente = num1/num2 

print("Suma:", Suma)
print("Resta:", Resta)
print("Producto:", Producto)
print("Cubo:", Cubo)
print("Cociente:", Cociente)
