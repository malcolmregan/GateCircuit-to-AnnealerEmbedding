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
        weightnames = []
        for i in range(6):
            weightnames.append('w{}'.format(i+self.numannealerqubits))
        self.numannealerqubits = self.numannealerqubits + 6


        #Tofqubitvals order: [0]=anc1; [1]=anc2; [2]=ctl1; [3]=ctl2; [4]=targout; [5]=targ
        Tofqubitvals = [4,4,0,0,1,1]

        #Tofcouplervals order: [0]=('anc1', 'anc2')  
        #                      [1]=('anc1', 'targout')
        #                      [2]=('anc1','targ') 
        #                      [3]=('anc2', 'ctl1')
        #                      [4]=('anc2', 'ctl2') 
        #                      [5]=('anc2', 'targout')  
        #                      [6]=('anc2', 'targ')  
        #                      [7]=('ctl1', 'ctl2') 
        #                      [8]=('targout', 'targ')
        Tofcouplervals = [-4,4,-4,-2,-2,-2,2,1,-2]

        if len(self.qubits[ctl1]['components']) > 0:
            Tofqubitvals[2] = Tofqubitvals[2] + 5
            joinedqubitname = self.qubits[ctl1]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[2])] = -10

        if len(self.qubits[ctl2]['components']) > 0:
            Tofqubitvals[3] = Tofqubitvals[3] + 5
            joinedqubitname = self.qubits[ctl2]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[3])] = -10

        if len(self.qubits[targ]['components']) > 0:
            Tofqubitvals[5] = Tofqubitvals[5] + 5
            joinedqubitname = self.qubits[targ]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(joinedqubitname, weightnames[5])] = -10


        #qubit and coupler weights for anc1
        self.qubits['annealerancillas'].append(weightnames[0])
        self.qubitweights[weightnames[0]] = Tofqubitvals[0]
        self.couplerweights[(weightnames[0], weightnames[1])] = Tofcouplervals[0]
        self.couplerweights[(weightnames[0], weightnames[4])] = Tofcouplervals[1]
        self.couplerweights[(weightnames[0], weightnames[5])] = Tofcouplervals[2]

        #qubit and coupler weights for anc2
        self.qubits['annealerancillas'].append(weightnames[1])
        self.qubitweights[weightnames[1]] = Tofqubitvals[1]
        self.couplerweights[(weightnames[1], weightnames[2])] = Tofcouplervals[3]
        self.couplerweights[(weightnames[1], weightnames[3])] = Tofcouplervals[4]
        self.couplerweights[(weightnames[1], weightnames[4])] = Tofcouplervals[5]
        self.couplerweights[(weightnames[1], weightnames[5])] = Tofcouplervals[6]

        #qubit and coupler weights for ctl1
        self.qubits[ctl1]['components'].append(weightnames[2])
        self.qubitweights[weightnames[2]] = Tofqubitvals[2]
        self.couplerweights[(weightnames[2], weightnames[3])] = Tofcouplervals[7]

        #qubit and coupler weights for ctl2
        self.qubits[ctl2]['components'].append(weightnames[3])
        self.qubitweights[weightnames[3]] = Tofqubitvals[3]

        #qubit and coupler weights for targ
        self.qubits[targ]['components'].append(weightnames[5])
        self.qubitweights[weightnames[5]] = Tofqubitvals[5]

        #qubit and coupler weights for targout
        self.qubits[targ]['components'].append(weightnames[4])
        self.qubitweights[weightnames[4]] = Tofqubitvals[4]
        self.couplerweights[(weightnames[4], weightnames[5])] = Tofcouplervals[8]

        '''
                'anc1' : 4
                'anc2' : 4 
                'ctl1' : 0
                'ctl2' : 0
                'tgtout' : 1 
                'tgt' : 1
                
                ('anc1', 'anc2') : -4 
                ('anc1', 'tgtout') : 4
                ('anc1','tgt') : -4
                ('anc2', 'ctl1') : -2 
                ('anc2', 'ctl2') : -2
                ('anc2', 'tgtout') : -2 
                ('anc2', 'tgt') : 2 
                ('ctl1', 'ctl2') : 1 
                ('tgtout', 'tgt') : -2
        ''' 

    def add_swap(self, targ1, targ2):
        pass

    def add_Fredkin(self, ctl, targ1, targ2):
        pass  

    def map_to_Dwave_graph(self, solvernodes, solveredges):
        print("Mapping to Dwave graph")
        qubits = []
        dwavemap = {}
        dwave_qubit_weights = {}
        dwave_coupler_weights = {}
        
        for qubitname in self.qubitweights.keys():
            qubits.append(qubitname)

        for qubitname in qubits:
            print(dwavemap)
            if qubitname not in dwavemap:
                dwavemap[qubitname] = [solvernodes[0]]
                dwave_qubit_weights[solvernodes[0]] = self.qubitweights[qubitname]
                solvernodes.pop(0)
            
            for coupler in self.couplerweights.keys():
                if qubitname in coupler:
                    otherqubit = [qbit for qbit in coupler if qbit is not qubitname][0]
                    if otherqubit not in dwavemap:
                        # try to assign based on available couplers
                        # if there is only one edge left with qubitname as a node then qubitname should be split before a 
                        # the new qubit is assigned.
                        
                        availedges = 0
                        for edge in solveredges:
                            if edge[0] in dwavemap[qubitname] or edge[1] in dwavemap[qubitname]:
                                availedges = availedges + 1         
                                if availedges == 2:
                                    if edge[0] in solvernodes:
                                        dwavemap[otherqubit] = [edge[0]]
                                        dwave_qubit_weights[edge[0]] = self.qubitweights[otherqubit]
                                        try:
                                            dwave_coupler_weights[(edge[0],edge[1])] = self.couplerweights[(otherqubit, qubitname)]
                                        except:
                                            dwave_coupler_weights[(edge[0],edge[1])] = self.couplerweights[(qubitname, otherqubit)]
                                        solvernodes.pop(solvernodes.index(edge[0]))
                                        solveredges.pop(solveredges.index((edge[0],edge[1])))
                                        break

                                    if edge[1] in solvernodes:
                                        dwavemap[otherqubit] = [edge[1]]
                                        dwave_qubit_weights[edge[1]] = self.qubitweights[otherqubit]
                                        try:
                                            dwave_coupler_weights[(edge[0],edge[1])] = self.couplerweights[(qubitname, otherqubit)]
                                        except:
                                            dwave_coupler_weights[(edge[0],edge[1])] = self.couplerweights[(otherqubit, qubitname)]
                                        solvernodes.pop(solvernodes.index(edge[1]))
                                        solveredges.pop(solveredges.index((edge[0],edge[1])))
                                        break
                        
                        if availedges == 1:
                            if edge[0] in solvernodes:
                                oldweight = dwave_qubit_weights[edge[1]]
                                dwave_qubit_weights[edge[1]] = dwave_qubit_weights[edge[1]] + 5
                                dwave_qubit_weights[edge[0]] = dwave_qubit_weights[edge[1]]
                                dwave_coupler_weights[(edge[0], edge[1])] = oldweight - dwave_qubit_weights[edge[1]] - dwave_qubit_weights[edge[0]]
                                solvernodes.pop(solvernodes.index(edge[0]))
                                solveredges.pop(solveredges.index((edge[0], edge[1])))
                                dwavemap[qubitname].append(edge[0])
                            if edge[1] in solvernodes:
                                oldweight = dwave_qubit_weights[edge[1]]
                                dwave_qubit_weights[edge[0]] = dwave_qubit_weights[edge[0]] + 5
                                dwave_qubit_weights[edge[1]] = dwave_qubit_weights[edge[0]]
                                dwave_coupler_weights[(edge[0], edge[1])] = oldweight - dwave_qubit_weights[edge[1]] - dwave_qubit_weights[edge[0]]
                                solvernodes.pop(solvernodes.index(edge[1]))
                                solveredges.pop(solveredges.index((edge[0], edge[1])))
                                dwavemap[qubitname].append(edge[1])


                            # split qubitname (update qubit weights and assign coupler between them)
                            # search for couplers
                            # assign otherqubit based on coupler

                        if availedges == 0:
                            print('map_to_Dwave_graph() doesn''t work right. Need to fix.')

                    else:
                        # see if coupler has already been assigned (is in dwave_coupler_weights) - if so do nothing
                        couplerassigned = False
                        couplerexists = False
                        for q in dwavemap[qubitname]:
                            if couplerassigned == True:
                                break
                            for b in dwavemap[otherqubit]:
                                if (q, b) in dwave_coupler_weights or (b, q) in dwave_coupler_weights:
                                    couplerassigned = True
                                    break

                        # see if coupler exists (is in solveredges) - if so update dwave_coupler_weights
                        if couplerassigned == False:
                            for q in dwavemap[qubitname]:
                                if couplerexists == True:
                                    break
                                for b in dwavemap[otherqubit]:
                                    if (q, b) in solveredges or (b, q) in solveredges:
                                        couplerexists = True
                                        if (q, b) in solveredges:
                                            try:
                                                dwave_coupler_weights[(q, b)] = self.couplerweights[(qubitname, otherqubit)]
                                            except:
                                                dwave_coupler_weights[(q, b)] = self.couplerweights[(otherqubit, qubitname)]
                                            solveredges.pop(solveredges.index((q, b)))
                                        if (b, q) in solveredges:
                                            try:
                                                dwave_coupler_weights[(b, q)] = self.couplerweights[(otherqubit, qubitname)]
                                            except:
                                                dwave_coupler_weights[(b, q)] = self.couplerweights[(qubitname, otherqubit)]
                                            solveredges.pop(solveredges.index((b, q)))
                                        break
        
                        # if neither of these qubitname must be split with another qubit to which the coupling can be made
                        if couplerassigned == False and couplerexists == False:
                            for q in dwavemap[qubitname]:
                                if couplerassigned == True:
                                    break
                                for b in dwavemap[otherqubit]:
                                    if couplerassigned == True:
                                        break
                                    for candidate in solvernodes:
                                        if ((candidate, q) in solveredges and (candidate, b) in solveredges):
                                            dwavemap[qubitname].append(candidate)
                                            oldweight = dwave_qubit_weights[q]
                                            dwave_qubit_weights[q] = dwave_qubit_weights[q] + 5
                                            dwave_qubit_weights[candidate] = dwave_qubit_weights[q]
                                            dwave_coupler_weights[(candidate, q)] = oldweight - dwave_qubit_weights[q] - dwave_qubit_weights[candidate]
                                            try: 
                                                dwave_coupler_weights[(candidate, b)] = self.couplerweights[(qubitname, otherqubit)]
                                            except:
                                                dwave_coupler_weights[(candidate, b)] = self.couplerweights[(otherqubit, qubitname)]
                                            solvernodes.pop(solvernodes.index(candidate))
                                            solveredges.pop(solveredges.index((candidate, q)))
                                            solveredges.pop(solveredges.index((candidate, b)))
                                            break

                                        if ((candidate, q) in solveredges and (b, candidate) in solveredges):
                                            dwavemap[qubitname].append(candidate)
                                            oldweight = dwave_qubit_weights[q]
                                            dwave_qubit_weights[q] = dwave_qubit_weights[q] + 5
                                            dwave_qubit_weights[candidate] = dwave_qubit_weights[q]
                                            dwave_coupler_weights[(candidate, q)] = oldweight - dwave_qubit_weights[q] - dwave_qubit_weights[candidate]

                                            try:
                                                dwave_coupler_weights[(b, candidate)] = self.couplerweights[(qubitname, otherqubit)]
                                            except:
                                                dwave_coupler_weights[(b, candidate)] = self.couplerweights[(otherqubit, qubitname)]
                                            solvernodes.pop(solvernodes.index(candidate))
                                            solveredges.pop(solveredges.index((candidate, q)))
                                            solveredges.pop(solveredges.index((b, candidate)))
                                            break

                                        if ((q, candidate) in solveredges and (candidate, b) in solveredges):
                                            dwavemap[qubitname].append(candidate)
                                            oldweight = dwave_qubit_weights[q]
                                            dwave_qubit_weights[q] = dwave_qubit_weights[q] + 5
                                            dwave_qubit_weights[candidate] = dwave_qubit_weights[q]
                                            dwave_coupler_weights[(q, candidate)] = oldweight - dwave_qubit_weights[q] - dwave_qubit_weights[candidate]
                                            try:
                                                dwave_coupler_weights[(candidate, b)] = self.couplerweights[(qubitname, otherqubit)]
                                            except:
                                                dwave_coupler_weights[(candidate, b)] = self.couplerweights[(otherqubit, qubitname)]
                                            solvernodes.pop(solvernodes.index(candidate))
                                            solveredges.pop(solveredges.index((q, candidate)))
                                            solveredges.pop(solveredges.index((candidate, b)))
                                            break

                                        if ((q, candidate) in solveredges and (b, candidate) in solveredges):
                                            dwavemap[qubitname].append(candidate)
                                            oldweight = dwave_qubit_weights[q]
                                            dwave_qubit_weights[q] = dwave_qubit_weights[q] + 5
                                            dwave_qubit_weights[candidate] = dwave_qubit_weights[q]
                                            dwave_coupler_weights[(q, candidate)] = oldweight - dwave_qubit_weights[q] - dwave_qubit_weights[candidate]
                                            try:
                                                dwave_coupler_weights[(b, candidate)] = self.couplerweights[(qubitname, otherqubit)]
                                            except:
                                                dwave_coupler_weights[(b, candidate)] = self.couplerweights[(otherqubit, qubitname)]
                                            solvernodes.pop(solvernodes.index(candidate))
                                            solveredges.pop(solveredges.index((q, candidate)))
                                            solveredges.pop(solveredges.index((b, candidate)))
                                            break


        print("Done.")
        print(dwavemap)
        print(dwave_qubit_weights)
        print(dwave_coupler_weights)
        return dwave_qubit_weights, dwave_coupler_weights, dwavemap
        
