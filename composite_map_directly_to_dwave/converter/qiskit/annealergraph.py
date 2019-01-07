from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit._classicalregister import ClassicalRegister
from dwave.system.samplers import DWaveSampler
from math import floor, copysign

                
class annealer_graph():
    def __init__(self, regs):
        self.qubits = self.getqubitnames(regs)
        self.qubitweights = {}
        self.couplerweights = {}
        self.gatenum = 0     
        self.topleftofgatecells = [136, 392, 408, 152, 168, 424, 440, 184, 200, 456, 472, 216, 232, 488, 504, 248]  
                                  # ^^ just set up for first two rows for now to test. Max of 16 gates.
    def getqubitnames(self, regs):
        qubits = {}
        for reg in regs:
            for i in range(regs[reg].size):
                qubits['{}_{}'.format(regs[reg].name,i)] = {'components': list(), 'measured': False}
        
        qubits['annealer_ancillas'] = list()

        return qubits

    def add_X(self, targ):
        topleft = self.topleftofgatecells[self.gatenum]
        
        if self.gatenum % 2 == 0:
            outname = 0 + topleft
            inname = 4 + topleft

        else:
            outname = 4 + topleft
            inname = 0 + topleft

        inval = -4
        outval = -4
        
        inoutcouplerval = 10

        if len(self.qubits[targ]['components']) > 0:
            injoin = self.qubits[targ]['components'][-1]
            injointopleft = injoin - injoin % 8
            injoincell = self.topleftofgatecells.index(injointopleft) 
            # if coming from last cell
            if self.gatenum - injoincell == 1:
                #find row
                injoinrow = injoin % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname
                inname = inname + injoinrow
                outname = outname + injoinrow

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if injoincell % 4 == 0:
                    newqubit = injoin + 128
                elif injoincell % 2 == 0:
                    newqubit = injoin - 128
                else:
                    newqubit = injoin + 8
               
                # add new qubit chain with injoin
                self.qubitweights[injoin] = self.qubitweights[injoin] + 5
                self.qubits[targ]['components'].append(newqubit) 
                self.qubitweights[newqubit] = 10
                self.couplerweights[(min(injoin, newqubit), max(injoin, newqubit))] = -10
                
                # chain inname with newqubit
                inval = inval + 5
            
                self.couplerweights[(min(newqubit, inname), max(newqubit,inname))] = -10

            else:
                inname, outname, inval, outval = self.make_chain(inname, outname, inval, outval, injoin, targ)
                
        inoutcouplername = (min(inname,outname), max(inname, outname))

        self.qubits[targ]['components'].append(inname)
        self.qubits[targ]['components'].append(outname)

        self.qubitweights[inname] = inval
        self.qubitweights[outname] = outval

        self.couplerweights[inoutcouplername] = inoutcouplerval

        self.gatenum = self.gatenum + 1

    def add_CNOT(self, ctl, targ):
        topleft = self.topleftofgatecells[self.gatenum]

        if self.gatenum % 2 == 0:
            # out side left
            ancout_name = topleft
            out_name = 1 + topleft
            ctlout_name = 2 + topleft
            
            # in side right
            ancin_name = 4 + topleft
            targ_name = 5 + topleft
            ctlin_name = 6 + topleft
        else:
            # out side right 
            ancout_name = 4 + topleft
            out_name = 5 + topleft
            ctlout_name = 6 + topleft
            
            # in side left
            ancin_name = topleft
            targ_name = 1 + topleft
            ctlin_name = 2 + topleft
        
        #qubitweights
        ctlin_val = 6
        ancin_val = 9
        targ_val = 1
            
        ctlout_val = 6
        ancout_val = 9
        out_val = 1
        
        #couplerweights
        ancin_ancout_couplerval = -14
        ancin_ctlout_couplerval = -4
        ancout_targ_couplerval = -4
        ancin_out_couplerval = 4
        ctlin_ctlout_couplerval = -11
        ctlin_out_couplerval = -2
        ctlout_targ_couplerval = 2
        targ_out_couplerval = -2
 
        assignedins = {}
        
        if len(self.qubits[targ]['components']) > 0:
            targjoin = self.qubits[targ]['components'][-1]
            targjointopleft = targjoin - targjoin % 8
            targjoincell = self.topleftofgatecells.index(targjointopleft)
            # if coming from last cell
            if self.gatenum - targjoincell == 1:
                #find row
                rowoffset = targjoin % 4 - targ_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ_name = targ_name + rowoffset
                out_name = out_name + rowoffset

                for row in [[ctlin_name, ctlout_name], [ancin_name, ancout_name]]:
                    if row[0] == targ_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targjoincell % 4 == 0:
                    newqubit = targjoin + 128
                elif targjoincell % 2 == 0:
                    newqubit = targjoin - 128
                else:
                    newqubit = targjoin + 8

                # add new qubit chain with injoin
                self.qubitweights[targjoin] = self.qubitweights[targjoin] + 5
                self.qubits[targ]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10 
                self.couplerweights[(min(targjoin, newqubit), max(targjoin, newqubit))] = -10

                # chain inname with newqubit
                targ_val = targ_val + 5

                self.couplerweights[(min(newqubit, targ_name), max(newqubit,targ_name))] = -10

                self.qubits[targ]['components'].append(targ_name)
                self.qubitweights[targ_name] = targ_val

                assignedins['targ'] = targ_name

        if len(self.qubits[ctl]['components']) > 0:
            ctlinjoin = self.qubits[ctl]['components'][-1]
            ctlinjointopleft = ctlinjoin - ctlinjoin % 8
            ctlinjoincell = self.topleftofgatecells.index(ctlinjointopleft)
            # if coming from last cell
            if self.gatenum - ctlinjoincell == 1:
                #find row
                rowoffset = ctlinjoin % 4 - ctlin_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctlin_name = ctlin_name + rowoffset
                ctlout_name = ctlout_name + rowoffset

                for row in [[targ_name, out_name], [ancin_name, ancout_name]]:
                    if row[0] == ctlin_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset


                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctlinjoincell % 4 == 0:
                    newqubit = ctlinjoin + 128
                elif ctlinjoincell % 2 == 0:
                    newqubit = ctlinjoin - 128
                else:
                    newqubit = ctlinjoin + 8

                # add new qubit chain with injoin
                self.qubitweights[ctlinjoin] = self.qubitweights[ctlinjoin] + 5
                self.qubits[ctl]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10 
                self.couplerweights[(min(ctlinjoin, newqubit), max(ctlinjoin, newqubit))] = -10

                # chain inname with newqubit
                ctlin_val = ctlin_val + 5

                self.couplerweights[(min(newqubit, ctlin_name), max(newqubit, ctlin_name))] = -10

                self.qubits[ctl]['components'].append(ctlin_name)
                self.qubitweights[ctlin_name] = ctlin_val

                assignedins['ctlin'] = ctlin_name

        if len(self.qubits[targ]['components']) > 0:
            if self.gatenum - targjoincell > 1:
                targjoin = self.qubits[targ]['components'][-1]
                targ_name, out_name, targ_val, out_val = self.make_chain(targ_name, out_name, targ_val, out_val, targjoin, targ)
                
                self.qubits[targ]['components'].append(targ_name)
                self.qubitweights[targ_name] = targ_val

                assignedins['targ'] = targ_name

        if len(self.qubits[ctl]['components']) > 0:
            if self.gatenum - ctlinjoincell > 1:
                ctlinjoin = self.qubits[ctl]['components'][-1]
                ctlin_name, ctlout_name, ctlin_val, ctlout_val = self.make_chain(ctlin_name, ctlout_name, ctlin_val, ctlout_val, ctlinjoin, ctl)
                
                self.qubits[ctl]['components'].append(ctlin_name)
                self.qubitweights[ctlin_name] = ctlin_val

                assignedins['ctlin'] = ctlin_name

        availablerows = [0,1,2,3]
        for key in assignedins.keys():
            availablerows.pop(availablerows.index(assignedins[key]%4))
        
        if 'targ' not in assignedins:
            if targ_name % 4 not in availablerows:
                rowoffset = availablerows[0] - targ_name % 4
                targ_name = targ_name + rowoffset
                out_name = out_name + rowoffset
                availablerows.pop(availablerows.index(targ_name%4))
            else:
                availablerows.pop(availablerows.index(targ_name%4))

        if 'ctlin' not in assignedins:
            if ctlin_name % 4 not in availablerows:
                rowoffset = availablerows[0] - ctlin_name % 4
                ctlin_name = ctlin_name + rowoffset
                ctlout_name = ctlout_name + rowoffset
                availablerows.pop(availablerows.index(ctlin_name%4))
            else:
                availablerows.pop(availablerows.index(ctlin_name%4))

        if 'ancin' not in assignedins:
            if ancin_name %4 not in availablerows:
                rowoffset = availablerows[0] - ancin_name % 4
                ancin_name = ancin_name + rowoffset
                ancout_name = ancout_name + rowoffset
                availablerows.pop(availablerows.index(ancin_name%4))
            else:
                availablerows.pop(availablerows.index(ancin_name%4))


        #couplernames
        ancin_ancout_couplername = (min(ancin_name, ancout_name), max(ancin_name, ancout_name))
        ancin_ctlout_couplername = (min(ancin_name, ctlout_name), max(ancin_name, ctlout_name))
        ancout_targ_couplername = (min(ancout_name, targ_name), max(ancout_name, targ_name))
        ancin_out_couplername = (min(ancin_name, out_name), max(ancin_name, out_name))
        ctlin_ctlout_couplername = (min(ctlin_name, ctlout_name), max(ctlin_name, ctlout_name))
        ctlin_out_couplername = (min(ctlin_name, out_name), max(ctlin_name, out_name))
        ctlout_targ_couplername = (min(ctlout_name, targ_name), max(ctlout_name, targ_name))
        targ_out_couplername = (min(targ_name, out_name), max(targ_name, out_name))

        if 'ctlin' not in assignedins:
            self.qubits[ctl]['components'].append(ctlin_name)
            self.qubitweights[ctlin_name] = ctlin_val
        self.qubits[ctl]['components'].append(ctlout_name)
        self.qubitweights[ctlout_name] = ctlout_val

        if 'targ' not in assignedins:
            self.qubits[targ]['components'].append(targ_name)
            self.qubitweights[targ_name] = targ_val
        self.qubits[targ]['components'].append(out_name)
        self.qubitweights[out_name] = out_val

        self.qubits['annealer_ancillas'].append(ancin_name)
        self.qubits['annealer_ancillas'].append(ancout_name)
        self.qubitweights[ancin_name] = ancin_val
        self.qubitweights[ancout_name] = ancout_val

        self.couplerweights[ancin_ancout_couplername] = ancin_ancout_couplerval
        self.couplerweights[ancin_ctlout_couplername] = ancin_ctlout_couplerval
        self.couplerweights[ancout_targ_couplername] = ancout_targ_couplerval
        self.couplerweights[ancin_out_couplername] = ancin_out_couplerval
        self.couplerweights[ctlin_ctlout_couplername] = ctlin_ctlout_couplerval
        self.couplerweights[ctlin_out_couplername] = ctlin_out_couplerval
        self.couplerweights[ctlout_targ_couplername] = ctlout_targ_couplerval
        self.couplerweights[targ_out_couplername] = targ_out_couplerval

        self.gatenum = self.gatenum + 1
    
        print("gate", self.gatenum-1)
        print("\ttarg",targ_name)
        print("\tctlin", ctlin_name)
        print("\tancin", ancin_name)
        print("\tout", out_name)
        print("\tctlout",ctlout_name)
        print("\tancout",ancout_name)

    def add_Toffoli(self, ctl1, ctl2, targ):
        topleft = self.topleftofgatecells[self.gatenum]

        if self.gatenum % 2 == 0:
            # out side left
            outout_name = topleft
            ctl1out_name = 1 + topleft
            ctl2out_name = 2 + topleft
            anc_name = 3 + topleft

            # in side right
            targ_name = 4 + topleft
            ctl1in_name = 5 + topleft
            ctl2in_name = 6 + topleft
            outin_name = 7 + topleft

        else:
            # out side right
            outout_name = 4 + topleft
            ctl1out_name = 5 + topleft
            ctl2out_name = 6 + topleft
            anc_name = 7 + topleft

            # in side left
            targ_name = topleft
            ctl1in_name = 1 + topleft
            ctl2in_name = 2 + topleft
            outin_name = 3 + topleft


        #qubitweights
        targ_val = 4
        ctl1in_val = 5
        ctl2in_val = 5
        outin_val = 8

        outout_val = 8 
        ctl1out_val = 5
        ctl2out_val = 5 
        anc_val = 9

        #couplerweights
        clt1in_ctl1out_couplerval = -10
        ctl2in_ctl2out_couplerval = -10
        outin_outout_couplerval = -13

        anc_targ_couplerval = -9
        anc_ctl1in_couplerval = -4
        anc_ctl2in_couplerval = -5
        anc_outin_couplerval = 9

        outout_targ_couplerval = -7
        outin_ctl1out_couplerval = -2
        outin_ctl2out_couplerval = -2

        targ_ctl1out_couplerval = 2
        targ_ctl2out_couplerval = 2

        ctl1in_ctl2out_couplerval = 1

        assignedins = {}

        if len(self.qubits[targ]['components']) > 0:
            targjoin = self.qubits[targ]['components'][-1]
            targjointopleft = targjoin - targjoin % 8
            targjoincell = self.topleftofgatecells.index(targjointopleft)
            # if coming from last cell
            if self.gatenum - targjoincell == 1:
                #find row
                rowoffset = targjoin % 4 - targ_name % 4

                # change position of row being connected
                # if there were more rows occupied in this 
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                targ_name = targ_name + rowoffset
                outout_name = outout_name + rowoffset

                for row in [[ctl1in_name, ctl1out_name], [ctl2in_name, ctl2out_name], [outin_name, anc_name]]:
                    if row[0] == targ_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if targjoincell % 4 == 0:
                    newqubit = targjoin + 128
                elif targjoincell % 2 == 0:
                    newqubit = targjoin - 128
                else:
                    newqubit = targjoin + 8

                # add new qubit chain with injoin
                self.qubitweights[targjoin] = self.qubitweights[targjoin] + 5
                self.qubits[targ]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10 
                self.couplerweights[(min(targjoin, newqubit), max(targjoin, newqubit))] = -10

                # chain inname with newqubit
                targ_val = targ_val + 5

                self.couplerweights[(min(newqubit, targ_name), max(newqubit,targ_name))] = -10

                self.qubits[targ]['components'].append(targ_name)
                self.qubitweights[targ_name] = targ_val
            
                assignedins['targ'] = targ_name

        if len(self.qubits[ctl1]['components']) > 0:
            ctl1injoin = self.qubits[ctl1]['components'][-1]
            ctl1injointopleft = ctl1injoin - ctl1injoin % 8
            ctl1injoincell = self.topleftofgatecells.index(ctl1injointopleft)
            # if coming from last cell
            if self.gatenum - ctl1injoincell == 1:
                #find row
                rowoffset = ctl1injoin % 4 - ctl1in_name % 4

                # change position of row being connected
                # if there were more rows occupied in this
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctl1in_name = ctl1in_name + rowoffset
                ctl1out_name = ctl1out_name + rowoffset

                for row in [[targ_name, outout_name], [ctl2in_name, ctl2out_name], [outin_name, anc_name]]:
                    if row[0] == ctl1in_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctl1injoincell % 4 == 0:
                    newqubit = ctl1injoin + 128
                elif ctl1injoincell % 2 == 0:
                    newqubit = ctl1injoin - 128
                else:
                    newqubit = ctl1injoin + 8

                # add new qubit chain with injoin
                self.qubitweights[ctl1injoin] = self.qubitweights[ctl1injoin] + 5
                self.qubits[ctl1]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10 
                self.couplerweights[(min(ctl1injoin, newqubit), max(ctl1injoin, newqubit))] = -10

                # chain inname with newqubit
                ctl1in_val = ctl1in_val + 5

                self.couplerweights[(min(newqubit, ctl1in_name), max(newqubit, ctl1in_name))] = -10

                self.qubits[ctl1]['components'].append(ctl1in_name)
                self.qubitweights[ctl1in_name] = ctl1in_val
                
                assignedins['ctl1in'] = ctl1in_name

        if len(self.qubits[ctl2]['components']) > 0:
            ctl2injoin = self.qubits[ctl2]['components'][-1]
            ctl2injointopleft = ctl2injoin - ctl2injoin % 8
            ctl2injoincell = self.topleftofgatecells.index(ctl2injointopleft)
            # if coming from last cell
            if self.gatenum - ctl2injoincell == 1:
                #find row
                rowoffset = ctl2injoin % 4 - ctl2in_name % 4

                # change position of row being connected
                # if there were more rows occupied in this
                # gate the qubits previously in this row
                # would have to be switched with inname and outname

                ctl2in_name = ctl2in_name + rowoffset
                ctl2out_name = ctl2out_name + rowoffset

                for row in [[targ_name, outout_name], [ctl1in_name, ctl1out_name], [outin_name, anc_name]]:
                    if row[0] == ctl1in_name:
                        row[0] = row[0] - rowoffset
                        row[1] = row[1] - rowoffset

                # connect injoin to gate through input assembly cell
                # these if statements will have to be modified
                # when more if the chimera graph if included
                if ctl2injoincell % 4 == 0:
                    newqubit = ctl2injoin + 128
                elif ctl2injoincell % 2 == 0:
                    newqubit = ctl2injoin - 128
                else:
                    newqubit = ctl2injoin + 8

                # add new qubit chain with injoin
                self.qubitweights[ctl2injoin] = self.qubitweights[ctl2injoin] + 5
                self.qubits[ctl2]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10
                self.couplerweights[(min(ctl2injoin, newqubit), max(ctl2injoin, newqubit))] = -10

                # chain inname with newqubit
                ctl2in_val = ctl2in_val + 5

                self.couplerweights[(min(newqubit, ctl2in_name), max(newqubit, ctl2in_name))] = -10

                self.qubits[ctl2]['components'].append(ctl2in_name)
                self.qubitweights[ctl2in_name] = ctl2in_val

                assignedins['ctl2in'] = ctl2in_name

        if len(self.qubits[targ]['components']) > 0:
            if self.gatenum - targjoincell > 1:
                targjoin = self.qubits[targ]['components'][-1]
                targ_name, outout_name, targ_val, outout_val = self.make_chain(targ_name, outout_name, targ_val, outout_val, targjoin, targ)
                self.qubits[targ]['components'].append(targ_name)
                self.qubitweights[targ_name] = targ_val
                assignedins['targ'] = targ_name

        if len(self.qubits[ctl1]['components']) > 0:
            if self.gatenum - ctl1injoincell > 1:
                ctl1injoin = self.qubits[ctl1]['components'][-1]
                ctl1in_name, ctl1out_name, ctl1in_val, ctl1out_val = self.make_chain(ctl1in_name, ctl1out_name, ctl1in_val, ctl1out_val, ctl1injoin, ctl1)
                self.qubits[ctl1]['components'].append(ctl1in_name)
                self.qubitweights[ctl1in_name] = ctl1in_val
                assignedins['ctl1in'] = ctl1in_name

        if len(self.qubits[ctl2]['components']) > 0:
            if self.gatenum - ctl2injoincell > 1:
                ctl2injoin = self.qubits[ctl2]['components'][-1]
                ctl2in_name, ctl2out_name, ctl2in_val, ctl2out_val = self.make_chain(ctl2in_name, ctl2out_name, ctl2in_val, ctl2out_val, ctl2injoin, ctl2)
                self.qubits[ctl2]['components'].append(ctl2in_name)
                self.qubitweights[ctl2in_name] = ctl2in_val
                assignedins['ctl2in'] = ctl2in_name    

        availablerows = [0,1,2,3]
        for key in assignedins.keys():
            availablerows.pop(availablerows.index(assignedins[key]%4))
        
        if 'outin' not in assignedins:
            if outin_name % 4 not in availablerows:
                rowoffset = availablerows[0] - outin_name % 4
                outin_name = outin_name + rowoffset
                anc_name = anc_name + rowoffset
                availablerows.pop(availablerows.index(outin_name%4))
            else:
                availablerows.pop(availablerows.index(outin_name%4))
         
        if 'ctl1in' not in assignedins:
            if ctl1in_name % 4 not in availablerows:
                rowoffset = availablerows[0] - ctl1in_name % 4
                ctl1in_name = ctl1in_name + rowoffset
                ctl1out_name = ctl1out_name + rowoffset
                availablerows.pop(availablerows.index(ctl1in_name%4))
            else:
                availablerows.pop(availablerows.index(ctl1in_name%4))
        
        print(ctl2out_name)
        if 'ctl2in' not in assignedins:
            if ctl2in_name %4 not in availablerows:
                rowoffset = availablerows[0] - ctl2in_name % 4
                ctl2in_name = ctl2in_name + rowoffset
                ctl2out_name = ctl2out_name + rowoffset
                availablerows.pop(availablerows.index(ctl2in_name%4))
            else:
                availablerows.pop(availablerows.index(ctl2in_name%4))
        if 'targ' not in assignedins:
            if targ_name %4 not in availablerows:
                rowoffset = availablerows[0] - targ_name % 4
                targ_name = targ_name + rowoffset
                outout_name = outout_name + rowoffset
                availablerows.pop(availablerows.index(targ_name%4))
            else:
                availablerows.pop(availablerows.index(targ_name%4))

        # coupler names
        clt1in_ctl1out_couplername = (min(ctl1in_name, ctl1out_name), max(ctl1in_name, ctl1out_name))
        ctl2in_ctl2out_couplername = (min(ctl2in_name, ctl2out_name), max(ctl2in_name, ctl2out_name))
        outin_outout_couplername = (min(outin_name, outout_name), max(outin_name, outout_name))
        anc_targ_couplername = (min(anc_name, targ_name), max(anc_name, targ_name))
        anc_ctl1in_couplername = (min(anc_name, ctl1in_name), max(anc_name, ctl1in_name))
        anc_ctl2in_couplername = (min(anc_name, ctl2in_name), max(anc_name, ctl2in_name))
        anc_outin_couplername = (min(anc_name, outin_name), max(anc_name, outin_name))
        outout_targ_couplername = (min(outout_name, targ_name), max(outout_name, targ_name))
        outin_ctl1out_couplername = (min(outin_name, ctl1out_name), max(outin_name, ctl1out_name))
        outin_ctl2out_couplername = (min(outin_name, ctl2out_name), max(outin_name, ctl2out_name))
        targ_ctl1out_couplername = (min(targ_name, ctl1out_name), max(targ_name, ctl1out_name))
        targ_ctl2out_couplername = (min(targ_name, ctl2out_name), max(targ_name, ctl2out_name))
        ctl1in_ctl2out_couplername = (min(ctl1in_name, ctl2out_name), max(ctl1in_name, ctl2out_name))

        if 'ctl1in' not in assignedins:
            self.qubits[ctl1]['components'].append(ctl1in_name)
            self.qubitweights[ctl1in_name] = ctl1in_val
        self.qubits[ctl1]['components'].append(ctl1out_name)
        self.qubitweights[ctl1in_name] = ctl1in_val
        self.qubitweights[ctl1out_name] = ctl1out_val
        
        if 'ctl2in' not in assignedins:
            self.qubits[ctl2]['components'].append(ctl2in_name)
            self.qubitweights[ctl2in_name] = ctl2in_val
        self.qubits[ctl2]['components'].append(ctl2out_name)
        self.qubitweights[ctl2out_name] = ctl2out_val
        
        if 'targ' not in assignedins:
            self.qubits[targ]['components'].append(targ_name)
            self.qubitweights[targ_name] = targ_val
        self.qubits[targ]['components'].append(outin_name)
        self.qubits[targ]['components'].append(outout_name)
        self.qubitweights[outin_name] = outin_val
        self.qubitweights[outout_name] = outout_val

        self.qubits['annealer_ancillas'].append(anc_name)
        self.qubitweights[anc_name] = anc_val

        self.couplerweights[clt1in_ctl1out_couplername] = clt1in_ctl1out_couplerval
        self.couplerweights[ctl2in_ctl2out_couplername] = ctl2in_ctl2out_couplerval
        self.couplerweights[outin_outout_couplername] = outin_outout_couplerval
        self.couplerweights[anc_targ_couplername] = anc_targ_couplerval
        self.couplerweights[anc_ctl1in_couplername] = anc_ctl1in_couplerval
        self.couplerweights[anc_ctl2in_couplername] = anc_ctl2in_couplerval
        self.couplerweights[anc_outin_couplername] = anc_outin_couplerval
        self.couplerweights[outout_targ_couplername] = outout_targ_couplerval
        self.couplerweights[outin_ctl1out_couplername] = outin_ctl1out_couplerval
        self.couplerweights[outin_ctl2out_couplername] = outin_ctl2out_couplerval
        self.couplerweights[targ_ctl1out_couplername] = targ_ctl1out_couplerval
        self.couplerweights[targ_ctl2out_couplername] = targ_ctl2out_couplerval
        self.couplerweights[ctl1in_ctl2out_couplername] = ctl1in_ctl2out_couplerval

        self.gatenum = self.gatenum + 1
        print("gate", self.gatenum)
        print("\ttarg",targ_name)
        print("\tctl1",ctl1in_name)
        print("\tctl2",ctl2in_name)
        print("\tout",outin_name)

        self.print_chimera_graph_to_file()
    def add_swap(self, targ1, targ2):
        pass

    def add_Fredkin(self, ctl, targ1, targ2):
        pass  

    def join(self, q1, q2, circ_qubit):
        if q1 not in self.qubitweights:
            self.qubits[circ_qubit]['components'].append(q1)
            self.qubitweights[q1] = 5 
        else:
            self.qubitweights[q1] = self.qubitweights[q1] + 5
        if q2 not in self.qubitweights:
            self.qubits[circ_qubit]['components'].append(q2)
            self.qubitweights[q2] = 5      
        else:
            self.qubitweights[q2] = self.qubitweights[q2] + 5
            
        self.couplerweights[(min(q1, q2), max(q1, q2))] = -10
        
    def check_and_get_row_offset(self, checkqubit, dependency = None, otherdependency = None):
        row = checkqubit % 4
        if dependency is None and otherdependency is None:
            if checkqubit in self.qubitweights:
                first = checkqubit-row
                for i in range(4):
                    if first + i not in self.qubitweights:
                        row = i
        elif dependency is not None and otherdependency is None:
            if checkqubit in self.qubitweights or dependency in self.qubitweights:
                first = checkqubit-row
                for i in range(4):
                    if first + i not in self.qubitweights and first + i not in self.qubitweights:
                        row = i

        else:
            if checkqubit in self.qubitweights or dependency in self.qubitweights or otherdependency in self.qubitweights:
                first = checkqubit-row
                for i in range(4):
                    if first + i not in self.qubitweights and first + i not in self.qubitweights and first + i not in self.qubitweights:
                        row = i
        
        rowoffset = row - checkqubit % 4
    
        return int(rowoffset)

    def make_chain(self, inname, outname, inval, outval, lastinstance, circ_qubit):
        topleft = self.topleftofgatecells[self.gatenum]
        lastinstancetopleft = lastinstance - lastinstance % 8
        lastinstancecell = self.topleftofgatecells.index(lastinstancetopleft)
         
        # move out of cell
        if lastinstancecell % 4 == 0:
            newqubit = lastinstance - 128
        elif lastinstancecell % 2 == 0:
            newqubit = lastinstance + 128
        else:
            newqubit = lastinstance - 8

        newqubittopleft = newqubit - newqubit % 8
        horizontaldist = floor(topleft/8)%16 - floor(newqubittopleft/8)%16
        if horizontaldist == 0:
            horizontaldist = -2 # this just makes it work right for this case
        verticaldist = floor(topleft/128) - floor(newqubittopleft/128)

        # join with newqubit
        self.join(lastinstance, newqubit, circ_qubit)

        # if exiting on horizontally connected couplers
        # do certain things
        if lastinstancecell % 2 == 1:
            # if cell number is 3, 7, 11 etc. move up
            if lastinstancecell % 4 == 3:
                # see if ideal move is good if not find move
                offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit-4-128)
                
                #position to move vertically
                newqubit = newqubit - 4 + offset
                #connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                # move up once
                newqubit = newqubit - 128
                # connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # if cell number is 1, 5, 9 etc. move down
            else:
                # see if ideal move is good if not find move
                offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit-4+128)
                #position to move vertically
                newqubit = newqubit - 4 + offset
                #connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                
                # move down once
                newqubit = newqubit + 128
                # connect
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # see if ideal move is good if not find move
        offset = self.check_and_get_row_offset(newqubit+4, dependency = newqubit+4 + int(8*copysign(1, horizontaldist)))
        # position to move horizontally
        newqubit = newqubit + 4 + offset
        # connect
        self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # move horizontally toward new gate
        for i in range(abs(horizontaldist)-1):

            offset = self.check_and_get_row_offset(newqubit + int(8*copysign(1, horizontaldist)))
            if offset is not 0:
                # find a row that will work and change to it
                offset = self.check_and_get_row_offset(newqubit, dependency = newqubit-4, otherdependency = newqubit + int(8*copysign(1, horizontaldist)))
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                newqubit = newqubit + 4
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            newqubit = newqubit + int(8*copysign(1, horizontaldist))
            # connect 
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        # position to move vertically
        offset = self.check_and_get_row_offset(newqubit-4, dependency = newqubit - 4 + int(128*copysign(1, verticaldist)))
        newqubit = newqubit - 4 + offset
        # connect
        self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

        #recalculate vertical distance to simplify things
        newqubittopleft = newqubit - newqubit % 8
        verticaldist = floor(topleft/128) - floor(newqubittopleft/128)
    
        # move vertically to input assembly cell
        # if destination even, move verticaldist 
        if self.gatenum % 2 == 0:
            for i in range(abs(verticaldist)):
                offset = self.check_and_get_row_offset(newqubit + int(128*copysign(1, verticaldist)))
                if offset is not 0:
                    #find a row that works and change to it
                    offset = self.check_and_get_row_offset(newqubit, dependency = newqubit+4, otherdependency = newqubit + int(128*copysign(1, verticaldist)))
                    newqubit = newqubit + 4 + offset
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                    newqubit = newqubit - 4
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                newqubit = newqubit + int(128*copysign(1, verticaldist))
            
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            
            # check if row available in gate cell and move there
            offset = self.check_and_get_row_offset(newqubit + 4, dependency = newqubit + 4 + 8)
            newqubit = newqubit + 4 + offset
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
        
            # place inname and outname according to newqubit row
            rowoffset = newqubit % 4 - inname % 4
            
            inname = inname + rowoffset
            outname = outname + rowoffset

            # connect newqubit and inname
            self.qubitweights[newqubit] = self.qubitweights[newqubit] + 5
            inval = inval + 5
            self.couplerweights[(min(inname, newqubit), max(inname, newqubit))] =-10
            
        # if destination odd 
        else:
            # one more if input cell above gate
            # one less if input cell below gate
            # these numbers dont say that but they do it
            # im tired
            if abs(verticaldist) == 1:
                adjust = 1
            else: 
                adjust = -1
            for i in range(abs(verticaldist)+int(adjust)):
                offset = self.check_and_get_row_offset(newqubit + 128*copysign(1, verticaldist))
                if offset is not 0:
                    #find a row that works and change to it
                    offset = self.check_and_get_row_offset(newqubit, dependency = newqubit+4, otherdependency = newqubit + int(128*copysign(1,verticaldist)))
                    newqubit = newqubit + 4 + offset
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
                    newqubit = newqubit - 4
                    self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)        
                newqubit = newqubit + int(128*copysign(1, verticaldist))
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # position to move horizontally
            offset = self.check_and_get_row_offset(newqubit+4)
            newqubit = newqubit + 4 + offset
            # connect
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)

            # move horizontally into input assembly cell
            newqubit = newqubit + 8 
            # connect
            self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            
            if self.gatenum % 4 == 3:
                offset = self.check_and_get_row_offset(newqubit - 4, dependency = newqubit - 4 - 128)
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
            else:
                offset = self.check_and_get_row_offset(newqubit - 4, dependency = newqubit - 4 + 128)
                newqubit = newqubit - 4 + offset
                self.join(newqubit, self.qubits[circ_qubit]['components'][-1], circ_qubit)
 
            # place inname and outname according to newqubit row
            rowoffset = newqubit % 4 - inname % 4
            inname = inname + rowoffset
            outname = outname + rowoffset

            # connect newqubit and inname
            self.qubitweights[newqubit] = self.qubitweights[newqubit] + 5
            inval = inval + 5
            self.couplerweights[(min(inname, newqubit), max(inname, newqubit))] = -10               
            
        return inname, outname, inval, outval

    def print_chimera_graph_to_file(self):
        filename = 'debug.txt'
        f = open(filename, 'w')

        for graphrow in range(16):
            if graphrow is not 0:
                f.write("\n\n\n")
            for cellrow in range(4):
                if cellrow is not 0:
                    f.write("\n")
                for graphcolumn in range(16):
                    if graphcolumn is not 0:
                        f.write("   ")
                    for cellcolumn in range(2):
                        if cellcolumn*4+cellrow+graphcolumn*8+graphrow*128 not in self.qubitweights.keys():
                            f.write('-')
                        else:
                            f.write('X')
                        f.write("   ")
        f.close()
