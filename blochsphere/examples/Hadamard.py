from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr1 = QuantumRegister(1)
cr1 = ClassicalRegister(1)
qc = QuantumCircuit(qr1, cr1)

qc.h(qr1[0])
qc.measure(qr1, cr1)

execute(qc)
