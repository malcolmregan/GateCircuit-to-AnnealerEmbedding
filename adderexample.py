#!/usr/bin/python3
from converter.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from converter.qiskit import execute

qi = QuantumRegister(3) # a = qi[0]; b = qi[1]; ci = qi[2]
qo = QuantumRegister(2) # so = qo[0]; co = qo[1]
ci = ClassicalRegister(3)
co = ClassicalRegister(2)

circuit = QuantumCircuit(qi,qo,ci,co)

####### a = 1; b = 1; ci = 0 #######
circuit.x(qi[0])
circuit.x(qi[1])
####################################

for idx in range(3):
    circuit.cx(qi[idx], qo[0])
for idx in range(3):
    circuit.ccx(qi[idx], qi[(idx+1)%3], qo[1])

for idx in range(3):
    circuit.measure(qi[idx],ci[idx])
for idx in range(2):
    circuit.measure(qo[idx],co[idx])
