from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

qr = QuantumRegister(1)
cr = ClassicalRegister(1)
qc = QuantumCircuit(qr, cr)

qc.x(qr)

qc.measure(qr, cr)
