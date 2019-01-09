from converter.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute

a = QuantumRegister(2)
b = QuantumRegister(2)
ci = QuantumRegister(1)
s = QuantumRegister(2)
co = QuantumRegister(1)

a_ = ClassicalRegister(2)
b_ = ClassicalRegister(2)
ci_ = ClassicalRegister(1)
s_ = ClassicalRegister(2)
co_ = ClassicalRegister(1)


circuit = QuantumCircuit(a,b,ci,s,co,a_,b_,ci_,s_,co_)


circuit.ccx(a[0],b[0],ci[0])
circuit.cx(a[0],s[0])
circuit.cx(b[0],s[0])

circuit.ccx(ci[0], a[1], co[0])
circuit.ccx(ci[0], b[1], co[0])
circuit.ccx(a[1], b[1], co[0])
circuit.cx(ci[0], s[1])
circuit.cx(a[1], s[1])
circuit.cx(b[1], s[1])


circuit.measure(ci, ci_)
circuit.measure(s, s_)
circuit.measure(co, co_)

execute(circuit)
