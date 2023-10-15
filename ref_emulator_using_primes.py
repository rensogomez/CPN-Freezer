import math
from sympy import primerange
import matplotlib.pyplot as plt

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def suma_numeros_no_primos(inicio, fin):
    suma = 0
    for num in range(inicio + 1, fin):
        if not es_primo(num):
            suma += num
    return suma

def compressor():
    primos = list(primerange(1, 101))
    temperaturas = []
    gas_compressed = 2  # Establecemos 2 como el primer número primo como 0 Kelvin
    for i in range(1, len(primos)):
        suma_no_primos = suma_numeros_no_primos(primos[i - 1], primos[i])
        gas_compressed -= suma_no_primos
        temperaturas.append(gas_compressed)
    return temperaturas

def valve(temperaturas, factor_expansion):
    temperaturas_expandidas = [math.exp(t * factor_expansion) for t in temperaturas]
    return temperaturas_expandidas

# Obtiene las temperaturas resultantes antes de la expansión exponencial
temperaturas_resultantes = compressor()

# Factor de expansión exponencial
factor_expansion = 0.05  

# Obtiene las temperaturas expandidas de manera exponencial
temperaturas_expandidas = valve(temperaturas_resultantes, factor_expansion)

# Combina las temperaturas antes y después de la transición
temperaturas_combinadas = temperaturas_resultantes + temperaturas_expandidas


plt.plot(temperaturas_combinadas, marker='o', color='b', label='Curva de Temperatura del Sistema de Refrigeración')
plt.xlabel('Variación de la temperatura entre el compror y la válvula de expansión expresada')
plt.ylabel('Temperatura (Kelvin)')
plt.title('Emulador de sistema de refrigeración utilzando Intervalos de Números Primos')
plt.legend()
plt.grid(True)
plt.show()