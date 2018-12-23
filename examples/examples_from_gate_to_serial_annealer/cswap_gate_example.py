from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

qr = QuantumRegister(3)
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr, cr)

qc.cswap(qr[0], qr[1], qr[2])
qc.x(qr[0])
qc.cswap(qr[0], qr[1], qr[2])
qc.x(qr[1])
qc.cswap(qr[0], qr[1], qr[2])
qc.cswap(qr[0], qr[1], qr[2])
qc.x(qr[2])
qc.cswap(qr[0], qr[1], qr[2])
qc.x(qr[2])
qc.x(qr[0])
qc.cswap(qr[0], qr[1], qr[2])

qc.measure(qr, cr)
