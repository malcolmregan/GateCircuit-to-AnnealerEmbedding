from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit._classicalregister import ClassicalRegister
from dwave.system.samplers import DWaveSampler
from math import floor

class annealer_graph():
    def __init__(self, regs):
        self.qubits = self.getqubitnames(regs)
        self.qubitweights = {}
        self.couplerweights = {}
        self.unitcellsused = 0
        
    def getqubitnames(self, regs):
        qubits = {}
        for reg in regs:
            for i in range(regs[reg].size):
                qubits['{}_{}'.format(regs[reg].name,i)] = {'components': list(), 'measured': False}
        return qubits

    

    def add_X(self, targ):
        vec1 = [0,1,1,0,0,1,1,0,0,1,1,0,0,1,2,3,3,2,2,3,3,2,2,3,3,2,2,3] 
        vec2 = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,6,6,5,5,4,4,3,3,2,2,1,1,0,0]
        idx = self.unitcellsused % 28
        num = floor(self.unitcellsused/28)

        topleft = 256*(vec1[idx]+3*num)+16*vec2[idx]

        if self.unitcellsused % 2 == 0:
            targinname = topleft + 4
            targoutname = topleft 
            inside = 'right'
            outside = 'left'
        else:
            targinname = topleft 
            targout = topleft + 4 
            inside = 'left'
            outside = 'right'

        targinval = -4
        targoutval = -4

        targintargoutcoupler = 10

        # check for connections from previous gates
        if len(self.qubits[targ]['components']) > 0:
            targinconnection = self.qubits[targ]['components'][-1]
            
            # find where in the graph the connection is
            targconnection_dwave_unit_cell_row = floor(targinconnection/128)
            targconnection_dwave_unit_cell_col = floor(targinconnection/8) % 16
            
            targ_dwave_unit_cell_row = floor(targinname/128)
            targ_dwave_unit_cell_col = floor(targinname/8) % 16

            row_dist = targconnection_dwave_unit_cell_row - targ_dwave_unit_cell_row
            col_dist = targconnection_dwave_unit_cell_col - targ_dwave_unit_cell_col
            
            targconnection_unit_cell =
            targ_unit_cell = self.numunitcellsused

            # if connected with last gate
            if targ_unit_cell - targconnection_unit_cell == 1:
                # find row of connection
                row = targinconnection % 4
                

                # find if connection on left or right
                # sides should match if the gate modules are designed
                # correctly but just to be safe
                if targin % 8 < 4:
                    connectionside = 'left'
                else:
                    connectionside = 'right'
                
                
            # link it with qubits until it has a node 
            # connectable with targin
            

            # permute gate so that targin is on the correct
            # row to make the connection


        '''
        # inname is on the same side as where 
        # lasttarg has been moved to
        # and on the same row
        if lasttarginstance % 8 < 4:
            # on left
            inname = startqubit + lasttargrow
            outname = startqubit + 4 + lasttargrow
        else:
            # on right
            inname = startqubit + 4 + lasttargrow
            outname = startqubit + lasttargrow

        if len(self.qubits[targ]['components']) > 0:
            inval = inval + 5
            joinedqubitname = self.qubits[targ]['components'][-1]
            self.qubitweights[joinedqubitname] = self.qubitweights[joinedqubitname] + 5
            self.couplerweights[(min(joinedqubitname, inname), max(joinedqubitname, inname))] = -10

        self.qubits[targ]['components'].append(inname)
        self.qubitweights[inname] = inval
        self.qubits[targ]['components'].append(outname)
        self.qubitweights[outname] = outval
        self.couplerweights[(min(inname,outname),max(inname,outname))] = inoutcoupler

        sefl.unitcellsused = self.unitcellsused + 1

        print(self.qubits) 
        print(self.qubitweights)
        print(self.couplerweights)
        '''
        '''
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
        '''
    '''
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

        
        #        'anc1' : 4
        #        'anc2' : 4 
        #        'ctl1' : 0
        #        'ctl2' : 0
        #        'tgtout' : 1 
        #        'tgt' : 1
                
        #        ('anc1', 'anc2') : -4 
        #        ('anc1', 'tgtout') : 4
        #        ('anc1','tgt') : -4
        #        ('anc2', 'ctl1') : -2 
        #        ('anc2', 'ctl2') : -2
        #        ('anc2', 'tgtout') : -2 
        #        ('anc2', 'tgt') : 2 
        #        ('ctl1', 'ctl2') : 1 
        #        ('tgtout', 'tgt') : -2
         
        '''
    def add_swap(self, targ1, targ2):
        pass

    def add_Fredkin(self, ctl, targ1, targ2):
        pass  

