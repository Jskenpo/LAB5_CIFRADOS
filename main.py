import streamlit as st
import random

st.title("🔐 Simulación de Criptografía Cuántica: BB84")
st.markdown("Explora cómo Alice y Bob crean una clave secreta con seguridad cuántica (BB84).")

# Parámetros
n = st.slider("Número de bits (n)", min_value=4, max_value=50, value=20)
eve_present = st.checkbox("¿Eve intercepta la comunicación?", value=False)

# Funciones
def generate_random_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_random_bases(n):
    return [random.choice(['+', 'x']) for _ in range(n)]

def encode_photons(bits, bases):
    return list(zip(bits, bases))

def measure_photons(photons, bob_bases, eve=False):
    measured_bits = []
    for i, ((bit, alice_base), bob_base) in enumerate(zip(photons, bob_bases)):
        if eve:
            eve_base = random.choice(['+', 'x'])
            intercepted_bit = bit if eve_base == alice_base else random.randint(0, 1)
            measured_bit = intercepted_bit if bob_base == eve_base else random.randint(0, 1)
        else:
            measured_bit = bit if bob_base == alice_base else random.randint(0, 1)
        measured_bits.append(measured_bit)
    return measured_bits

def extract_key(bits, alice_bases, bob_bases):
    return [bit for bit, ab, bb in zip(bits, alice_bases, bob_bases) if ab == bb]

# Simulación
alice_bits = generate_random_bits(n)
alice_bases = generate_random_bases(n)
bob_bases = generate_random_bases(n)
photons = encode_photons(alice_bits, alice_bases)
bob_results = measure_photons(photons, bob_bases, eve=eve_present)
key_alice = extract_key(alice_bits, alice_bases, bob_bases)
key_bob = extract_key(bob_results, alice_bases, bob_bases)

# Resultados
st.subheader("📊 Resultado de la transmisión")
data = []
for i in range(n):
    match = "✅" if alice_bases[i] == bob_bases[i] else "❌"
    data.append({
        "Pos": i,
        "Bit de Alice": alice_bits[i],
        "Base de Alice": alice_bases[i],
        "Base de Bob": bob_bases[i],
        "Resultado de Bob": bob_results[i],
        "Coincidencia": match
    })

st.dataframe(data, use_container_width=True)

st.subheader("🔑 Claves secretas")
st.text(f"Clave de Alice: {key_alice}")
st.text(f"Clave de Bob:   {key_bob}")

if eve_present:
    st.warning("⚠️ Eve interceptó la comunicación. Las claves podrían no coincidir.")
else:
    st.success("✅ Comunicación segura. Las claves coinciden.")
