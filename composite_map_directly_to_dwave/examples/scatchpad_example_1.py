from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

qr = QuantumRegister(2)
qr2 = QuantumRegister(1)
cr = ClassicalRegister(2)
cr2 = ClassicalRegister(1)
qc = QuantumCircuit(qr, qr2, cr, cr2)

#qc.ccx(qr[0], qr[1], qr2[0])
#qc.x(qr[0])
#qc.ccx(qr[0], qr[1], qr[2])
#qc.x(qr[1])
#qc.ccx(qr[0], qr[1], qr[2])
#qc.ccx(qr[0], qr[1], qr[2])
#qc.ccx(qr[0], qr[1], qr[2])
#qc.x(qr[0])
#qc.ccx(qr[0], qr[1], qr[2])

for i in range(16):
    qc.ccx(qr[0],qr[1],qr2[0])
'''
qc.ccx(qr[0],qr[1],qr2[0])
qc.ccx(qr[1],qr[2],qr2[0])
qc.ccx(qr[0],qr[1],qr2[0])
qc.ccx(qr[0],qr[1],qr2[0])
qc.ccx(qr[0],qr[2],qr2[0])
'''
qc.measure(qr2, cr2)

execute(qc)
