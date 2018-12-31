from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit._classicalregister import ClassicalRegister

class annealer_graph():
    def __init__(self, regs):
        self.qubits = self.getqubitnames(regs)
        self.numannealerqubits = 0
        self.qubitweights = {}
        self.couplerweights = {}
    
    def getqubitnames(self, regs):
        qubits = {}
        for reg in regs:
            for i in range(regs[reg].size):
                qubits['{}_{}'.format(regs[reg].name,i)] = {'components': list(), 'measured': False}
        qubits['annealerancillas'] = list()

        return qubits

    def add_X(self, targ):
        weightnames = []
        for i in range(2):
            weightnames.append('w{}'.format(i+self.numannealerqubits))
        self.numannealerqubits = self.numannealerqubits + 2

        # Xqubitvals[0] = in; Xqubitvals[1] = out        
        Xqubitvals = [-4,-4]
        Xcouplervals = [10]

        if len(self.qubits[targ]['components']) > 0:
            Xqubitvals[0] = Xqubitvals[0] + 5
            joinedqubitname = self.qubits[targ]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[0])] = -10

        count = 0
        for i, name in enumerate(weightnames):
            self.qubits[targ]['components'].append(name)
            self.qubitweights[name] = Xqubitvals[i]
            for j in range(i+1, len(weightnames)):
                self.couplerweights[(name, weightnames[j])] = Xcouplervals[count]
                count = count + 1

        #print(self.qubitweights)
        #print(self.couplerweights)

    def add_CNOT(self, ctl, targ):
        weightnames = []
        for i in range(4):
            weightnames.append('w{}'.format(i+self.numannealerqubits))
        self.numannealerqubits = self.numannealerqubits + 4

        # Xqubitvals[0] = ancilla; Xqubitvals[1] = out; Xqubitvals[2] = targ Xqubitvals[3] = ctl       
        CNOTqubitvals = [4,1,1,1]
        CNOTcouplervals = [4,-4,-4,-2,-2,2]

        if len(self.qubits[targ]['components']) > 0:
            CNOTqubitvals[2] = CNOTqubitvals[2] + 5
            joinedqubitname = self.qubits[targ]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[2])] = -10

        if len(self.qubits[ctl]['components']) > 0:
            CNOTqubitvals[3] = CNOTqubitvals[3] + 5
            joinedqubitname = self.qubits[ctl]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[3])] = -10

        self.qubits['annealerancillas'].append(weightnames[0])
        self.qubitweights[weightnames[0]] = CNOTqubitvals[0]
        for i in range(3):
            self.couplerweights[(weightnames[0], weightnames[1+i])] = CNOTcouplervals[i] 
           
        self.qubits[targ]['components'].append(weightnames[2])
        self.qubitweights[weightnames[2]] = CNOTqubitvals[2]
        self.couplerweights[(weightnames[2],weightnames[3])] = CNOTcouplervals[5] 

        self.qubits[targ]['components'].append(weightnames[1])
        self.qubitweights[weightnames[1]] = CNOTqubitvals[1]
        self.couplerweights[(weightnames[1], weightnames[2])] = CNOTcouplervals[3]
        self.couplerweights[(weightnames[1], weightnames[3])] = CNOTcouplervals[4]

        self.qubits[ctl]['components'].append(weightnames[3])
        self.qubitweights[weightnames[3]] = CNOTqubitvals[3]

    def add_Toffoli(self, ctl1, ctl2, targ):
        pass

    def add_swap(self, targ1, targ2):
        pass

    def add_Fredkin(self, ctl, targ1, targ2):
        pass    
