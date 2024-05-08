## PROGRAMA DE TEST DE LA FUNCIÓN DE GENERACIÓN DE PRIMOS (con 512 bits compartidos)
import sympy
import random

def generate_prime_with_shared_bits(shared_bits_length, total_bits_length):
    assert shared_bits_length * 2 <= total_bits_length, "La longitud de bits compartidos debe ser la mitad o menos de la longitud total de bits."

    # Generar los bits compartidos
    shared_bits = 1 << (shared_bits_length - 1) | random.getrandbits(shared_bits_length - 1)

    # Crear máscaras para los bits restantes
    remaining_bits_mask = (1 << (total_bits_length - shared_bits_length)) - 1

    # Generar los números primos con los bits compartidos
    prime1 = prime2 = None
    while prime1 is None or prime2 is None:
        # Generar los bits restantes aleatoriamente
        remaining_bits = random.getrandbits(total_bits_length - shared_bits_length)
        candidate = (shared_bits << (total_bits_length - shared_bits_length)) | remaining_bits

        # Verificar si el candidato es primo
        if sympy.isprime(candidate):
            if prime1 is None:
                prime1 = candidate
            else:
                prime2 = candidate

    return prime1, prime2

# Ejemplo de uso:
shared_bits_length = 512
total_bits_length = 1024
prime1, prime2 = generate_prime_with_shared_bits(shared_bits_length, total_bits_length)

print(f"Primo 1:\n{prime1}\n")
print(f"Primo 2:\n{prime2}\n")