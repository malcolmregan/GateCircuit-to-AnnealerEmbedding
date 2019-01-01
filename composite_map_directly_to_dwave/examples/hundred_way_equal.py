from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from sys import argv

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



if(len(argv) != 3):
    print("Choose two hundred-bit numbers to compare as cli args")
    quit()

#100 inputs with  n-bits each : to be compared
n = 100
qin1 = QuantumRegister(n)
cin1 = ClassicalRegister(n)
qin2 = QuantumRegister(n)
cin2 = ClassicalRegister(n)

#output bit: function XORed onto this
qz = QuantumRegister(1)
cz = ClassicalRegister(1)

#output bit: function XORed onto this
tmp = QuantumRegister(1)

#beginning of the circuit
circuit = QuantumCircuit(qin1,qin2,qz,tmp,cin1,cin2,cz)

a = int(argv[1])
b = int(argv[2])
for i in range(100):
    if((a & 1) == 1):
        circuit.x(qin1[99 - i])
    if((b & 1) == 1):
        circuit.x(qin2[99 - i])
    a >>= 1
    b >>= 1

#initialize temp
circuit.x(tmp)

equal_nway(qin1, qin2, tmp, qz, n, circuit)
#reversing tmp
circuit.x(tmp)

circuit.measure(qin1, cin1)
circuit.measure(qin2, cin2)

circuit.measure(qz, cz)
