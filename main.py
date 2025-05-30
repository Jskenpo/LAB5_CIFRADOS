import random

def generate_random_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_random_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]  # + = ↕ (recta), x = ↗ (diagonal)

def encode_photons(bits, bases):
    # Retorna los fotones codificados como pares (bit, base)
    return list(zip(bits, bases))

def measure_photons(photons, bob_bases, eve=False):
    measured_bits = []
    for i, ((bit, alice_base), bob_base) in enumerate(zip(photons, bob_bases)):
        if eve:
            # Eve intercepta y mide con base aleatoria
            eve_base = random.choice(['+', 'x'])
            if eve_base == alice_base:
                intercepted_bit = bit
            else:
                intercepted_bit = random.randint(0, 1)
            # Bob mide el bit modificado por Eve
            if bob_base == eve_base:
                measured_bit = intercepted_bit
            else:
                measured_bit = random.randint(0, 1)
        else:
            if bob_base == alice_base:
                measured_bit = bit
            else:
                measured_bit = random.randint(0, 1)
        measured_bits.append(measured_bit)
    return measured_bits

def extract_key(bits, alice_bases, bob_bases):
    key = []
    for bit, ab, bb in zip(bits, alice_bases, bob_bases):
        if ab == bb:
            key.append(bit)
    return key

# Parámetros
n = 20  # número de bits

# Paso 1: Alice genera bits y bases
alice_bits = generate_random_bits(n)
alice_bases = generate_random_bases(n)

# Paso 2: Bob genera bases
bob_bases = generate_random_bases(n)

# Paso 3: Codificación de fotones
photons = encode_photons(alice_bits, alice_bases)

# Paso 4: Bob mide (opcional Eve=True para interceptar)
eve_present = True  # Cambia a False para ver sin Eve
bob_results = measure_photons(photons, bob_bases, eve=eve_present)

# Paso 5: Comparar bases y generar clave
key_alice = extract_key(alice_bits, alice_bases, bob_bases)
key_bob = extract_key(bob_results, alice_bases, bob_bases)

# Mostrar resultados
print(f"\n{'Pos':<4}{'A_Bit':<7}{'A_Base':<8}{'B_Base':<8}{'B_Bit':<7}")
for i in range(n):
    print(f"{i:<4}{alice_bits[i]:<7}{alice_bases[i]:<8}{bob_bases[i]:<8}{bob_results[i]:<7}")

print("\nClave secreta (Alice):", key_alice)
print("Clave secreta (Bob):   ", key_bob)

if eve_present:
    print("⚠️ Eve interceptó la comunicación. Las claves podrían no coincidir.")
else:
    print("✅ Comunicación segura. Claves idénticas.")
