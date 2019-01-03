from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr1 = QuantumRegister(3)
cr1 = ClassicalRegister(3)
qr2 = QuantumRegister(1)
cr2 = ClassicalRegister(1)
qc = QuantumCircuit(qr1, cr1, qr2, cr2)

qc.cx(qr1[0], qr2[0])
qc.cx(qr1[1], qr2[0])
qc.cx(qr1[2], qr2[0])


qc.measure(qr2, cr2)

execute(qc)
