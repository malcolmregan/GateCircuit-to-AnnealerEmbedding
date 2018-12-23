from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

qc.cx(qr[0], qr[1])
qc.x(qr[1])
qc.cx(qr[0], qr[1])
qc.x(qr[0])
qc.cx(qr[0], qr[1])
qc.cx(qr[0], qr[1])

qc.measure(qr, cr)
