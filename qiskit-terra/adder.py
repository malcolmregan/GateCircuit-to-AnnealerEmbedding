#!/usr/bin/python3
# Homework 3:
#  Brody Eastwood - baeastwo
#  Mahita Nagabhiru - mnagabh
#  Malcolm Regan - mjregan2

from converter.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from converter.qiskit import execute, available_backends
from converter.qiskit import Aer

def toffoli(circuit, ctrl1, ctrl2, targ):
    circuit.h(targ)
    circuit.cx(ctrl1, targ) 
    circuit.tdg(targ)
    circuit.cx(ctrl2, targ)
    circuit.t(targ)
    circuit.cx(ctrl1, targ)
    circuit.tdg(targ)
    circuit.cx(ctrl2, targ)
    circuit.t(targ)
    circuit.tdg(ctrl1)
    circuit.h(targ)
    circuit.cx(ctrl2,ctrl1)
    circuit.tdg(ctrl1)
    circuit.cx(ctrl2,ctrl1)
    circuit.s(ctrl1)
    circuit.t(ctrl2)

qi = QuantumRegister(3)
ci = ClassicalRegister(3)
qo = QuantumRegister(2)
co = ClassicalRegister(2)

qc = QuantumCircuit(qi,qo,ci,co)

# qi[0] (c) --o--o-----o-------- (c)
#             |  |     |
# qi[1] (x) --|--o--o--|--o----- (x)
#             |  |  |  |  |
# qi[2] (y) --o--|--o--|--|--o-- (y)
#             |  |  |  |  |  |
# qo[0] (0) --|--|--|--X--X--X-- (s)
#             |  |  |
# qo[1] (0) --X--X--X----------- (c')

qc.x(qi[0])
qc.x(qi[2])

for idx in range(3):
    toffoli(qc,qi[idx],qi[(idx-1) % len(qi)],qo[1])
for idx in range(3):
    qc.cx(qi[idx], qo[0])

qc.measure(qi,ci)
qc.measure(qo,co)

print(qc.qasm())

backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend)
result=job.result()
print(result.get_counts())
