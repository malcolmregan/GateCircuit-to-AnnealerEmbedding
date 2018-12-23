from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qin1 = QuantumRegister(1)
cin1 = ClassicalRegister(1)
qin2 = QuantumRegister(1)
cin2 = ClassicalRegister(1)

#output bit: function XORed onto this
qz = QuantumRegister(1)
cz = ClassicalRegister(1)

tmpq = QuantumRegister(1)
tmpc = ClassicalRegister(1)
#beginning of the circuit
circuit = QuantumCircuit(qin1,qin2,qz,tmpq,cin1,cin2,cz,tmpc)

#initialize example values
circuit.x(qin1)
circuit.x(qin2)

#initialize temp
circuit.x(tmpq)

circuit.cx(tmpq, qz)
circuit.ccx(qin1, tmpq, qz)
circuit.ccx(qin2, tmpq, qz)

#reversing tmp
circuit.x(tmpq)

#circuit.measure(qin1, cin1)
#circuit.measure(qin2, cin2)

circuit.measure(qz, cz)

execute(circuit)
