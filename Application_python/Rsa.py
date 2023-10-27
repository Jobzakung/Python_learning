import math


def find_prime_factors(n):
    k = 1
    lambda_value = n

    while True:
        d = (1 + lambda_value * k) // 3
        if d * 3 == 1 + lambda_value * k:
            return d
        k += 1


def calculate_lambda(p, q):
    return (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Fixed prime numbers
p = 17
q = 11
n = p * q
phi_n = (p - 1) * (q - 1)

# Choose a public exponent (e), usually 65537 in practice
e = 3  # Commonly used public exponent

# Calculate the private exponent (d)
d = mod_inverse(e, phi_n)

value_Lambda = calculate_lambda(p, q)
value_D = find_prime_factors(value_Lambda)

# Encryption
message = 99
ciphertext = pow(message, e, n)

# Decryption
decrypted_message = pow(ciphertext, d, n)

print("Public Key (n, e):", n, e)
print("Private Key (n, d):", n, value_D)
print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
print("Lambda:", value_Lambda)
