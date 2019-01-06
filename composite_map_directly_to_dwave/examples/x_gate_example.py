from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr1 = QuantumRegister(1)
qr2 = QuantumRegister(1)
cr1 = ClassicalRegister(1)
cr2 = ClassicalRegister(1)

qc = QuantumCircuit(qr1, qr2, cr1, cr2)

qc.x(qr1)
qc.x(qr2)
qc.x(qr2)
qc.x(qr2)
qc.x(qr2)
qc.x(qr1)

qc.measure(qr1, cr1)

execute(qc)
