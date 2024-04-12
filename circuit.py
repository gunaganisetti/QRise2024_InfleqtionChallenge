import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import RealAmplitudes, MSGate  

# Create quantum and classical registers
qr = QuantumRegister(3)
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr, cr)

# Apply Ry rotations with pi/2 phase on all qubits
for i in range(3):
    qc.ry(np.pi/2, i)

# Add RealAmplitudes ansatz
ansatz = RealAmplitudes(num_qubits=3, entanglement='linear', reps=2, insert_barriers=True)
qc.compose(ansatz, inplace=True)

# Incorporate Molmer-Sorensen gate
qc.append(MSGate(num_qubits=3, theta=np.pi/4), [0, 1, 2])

# Add reversed ansatz for decoding
reversed_ansatz = ansatz.inverse()
qc.compose(reversed_ansatz, inplace=True)

# Apply Rx rotations with pi/2 phase on all qubits
for i in range(3):
    qc.rx(np.pi/2, i)

# Measure all qubits
qc.measure(qr, cr)

# Visualize the final circuit
qc.draw()
