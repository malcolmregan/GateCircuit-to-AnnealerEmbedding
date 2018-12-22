from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr1 = QuantumRegister(1)
qr2 = QuantumRegister(1)
cr1 = ClassicalRegister(1)
cr2 = ClassicalRegister(1)
qc = QuantumCircuit(qr1, qr2, cr1, cr2)

qc.cx(qr1, qr2)

qc.measure(qr2, cr2)

execute(qc)
