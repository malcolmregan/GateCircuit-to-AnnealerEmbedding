#!/usr/bin/python3
# Homework 3:
#  Brody Eastwood - baeastwo
#  Mahita Nagabhiru - mnagabh
#  Malcolm Regan - mjregan2


from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from converter.qiskit import  execute #, available_backends
#from qiskit import Aer

#2 inputs with  n-bits each : to be compared
n = 2
qin1 = QuantumRegister(n)
cin1 = ClassicalRegister(n)
qin2 = QuantumRegister(n)
cin2 = ClassicalRegister(n)

#output bit: function XORed onto this
qz = QuantumRegister(1)
cz = ClassicalRegister(1)
qthing_to_be_swapped_into = QuantumRegister(1)
#output bit: function XORed onto this
tmp = QuantumRegister(1)
tmpc = ClassicalRegister(1)

#beginning of the circuit
circuit = QuantumCircuit(qin1,qin2,qz,tmp,cin1,cin2,cz,tmpc, qthing_to_be_swapped_into)

#for all possible combinations of the inputs, just hadamard them:
circuit.x(qin1[1]) # problem caused here -> qin1[1] gets named q0_0 instead of q0_1
circuit.x(qin1[0])
circuit.x(qin2)
circuit.cswap(qin2[0],qin1[0],qin1[1])

#initialize temp
circuit.x(tmp)

##borrowing from N-way AND from Dr. Byrd's example
def equal_nway(qx, qy, temp, qz, n, qc):
  if n == 1:
    #if n is 1, we directly do the comparison onto qz without any temporary bits
    qc.cx(temp[0],qz[0])
    qc.ccx(qx[0],temp[0],qz[0])
    qc.ccx(qy[0],temp[0],qz[0])

  else:
    #comparing the MSB
    t = QuantumRegister(1)
    qc.add(t)
    qc.cx(temp[0],t[0])
    qc.ccx(qx[n-1],temp[0],t[0])
    qc.ccx(qy[n-1],temp[0],t[0])
    equal_nway(qx,qy,t,qz,n-1,qc)

    #reversing t
    qc.ccx(qy[n-1],temp[0],t[0])
    qc.ccx(qx[n-1],temp[0],t[0])
    qc.cx(temp[0],t[0])
  return qc

equal_nway(qin1, qin2, tmp, qz, n, circuit)
circuit.swap(qz, qthing_to_be_swapped_into)
#reversing tmp
circuit.x(tmp)

circuit.measure(qin1,cin1)
circuit.measure(qin2,cin2)

circuit.measure(qz,cz)
circuit.measure(qthing_to_be_swapped_into, cz)
