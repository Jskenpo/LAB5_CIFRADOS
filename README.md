
# Laboratorio 5: QKD

## 📘 Descripción

Este laboratorio implementa una simulación del protocolo de distribución de claves cuánticas **BB84**. El objetivo es comprender cómo dos partes (Alice y Bob) pueden generar una clave secreta compartida mediante el uso de qubits y bases aleatorias, así como observar los efectos de la presencia de un espía (Eve) en el canal de comunicación.

## 🧪 Objetivos

- Simular el comportamiento de Alice, Bob y Eve en un canal cuántico.
- Visualizar cómo las bases de medición afectan la clave final compartida.
- Detectar la presencia de un espía a través de la tasa de error.
- Calcular métricas relevantes como la tasa de error entre claves.

---

## 🧠 Fundamento teórico

El protocolo **BB84** se basa en el uso de qubits enviados en distintas bases (rectilínea `+` y diagonal `x`). Cuando Alice y Bob usan la misma base para un bit dado, la medición de Bob debe coincidir con el bit enviado por Alice. Si un espía (Eve) intercepta el canal, su medición colapsa el estado cuántico, introduciendo errores detectables.

---

## ⚙️ Requisitos

- Python 3.7+


## 🚀 Ejecución

```bash
python main.py
```



## 📊 Ejemplo de salida

```
Pos A_Bit  A_Base  B_Base  B_Bit
0   0      x       +       0
1   0      x       +       1
2   0      +       +       1
...
Clave secreta (Alice): [0, 1, 1, 1, 0, 0, 0, 0, 1, 0]
Clave secreta (Bob):    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
Tasa de error        : 60.00%
```

---

## 📈 Resultados

* Sin Eve: tasa de error cercana a **0%**
* Con Eve: tasa de error significativamente mayor (indicando la presencia de un espía)
* Cuanto mayor sea el número de bits simulados (`n`), más estable es la detección de errores.

---

## 🔍 Funcionalidades principales

* Simulación de envío y recepción de bits con bases aleatorias.
* Visualización tabular de todos los pasos.
* Detección de coincidencia de bases.
* Generación de clave secreta compartida.
* Cálculo de tasa de error (Bit Error Rate).

---

## 📁 Archivos

* `main.py`: código principal con la lógica del protocolo.
* `README.md`: este documento.


---

## ✍️ Autores

* Nombre: Jose santisteban, Mark Albrand
* Curso: Cifrado de información
* Fecha: 29/05/2025

