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
                self.qubitweights[newqubit] = 10 # 10 bc connected to two qubits?
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

        #couplernames
        ancin_ancout_couplername = (min(ancin_name, ancout_name), max(ancin_name, ancout_name))
        ancin_ctlout_couplername = (min(ancin_name, ctlout_name), max(ancin_name, ctlout_name))
        ancout_targ_couplername = (min(ancout_name, targ_name), max(ancout_name, targ_name))
        ancin_out_couplername = (min(ancin_name, out_name), max(ancin_name, out_name))
        ctlin_ctlout_couplername = (min(ctlin_name, ctlout_name), max(ctlin_name, ctlout_name))
        ctlin_out_couplername = (min(ctlin_name, out_name), max(ctlin_name, out_name))
        ctlout_targ_couplername = (min(ctlout_name, targ_name), max(ctlout_name, targ_name))
        targ_out_couplername = (min(targ_name, out_name), max(targ_name, out_name))

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
                self.qubitweights[newqubit] = 10 # 10 bc connected to two qubits?
                self.couplerweights[(min(targjoin, newqubit), max(targjoin, newqubit))] = -10

                # chain inname with newqubit
                targ_val = targ_val + 5

                self.couplerweights[(min(newqubit, targ_name), max(newqubit,targ_name))] = -10

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
                elif ctlibjoincell % 2 == 0:
                    newqubit = ctlinjoin - 128
                else:
                    newqubit = ctlinjoin + 8

                # add new qubit chain with injoin
                self.qubitweights[ctlinjoin] = self.qubitweights[ctlinjoin] + 5
                self.qubits[ctlin]['components'].append(newqubit)
                self.qubitweights[newqubit] = 10 # 10 bc connected to two qubits?
                self.couplerweights[(min(ctlinjoin, newqubit), max(ctlinjoin, newqubit))] = -10

                # chain inname with newqubit
                ctlin_val = ctlin_val + 5

                self.couplerweights[(min(newqubit, ctlin_name), max(newqubit, ctlin_name))] = -10

        if len(self.qubits[targ]['components']) > 0:
            if self.gatenum - targjoincell > 1:
                targjoin = self.qubits[targ]['components'][-1]
                targ_name, out_name, targ_val, out_val = self.make_chain(targ_name, out_name, targ_val, out_val, targjoin, targ)
            

        if len(self.qubits[ctl]['components']) > 0:
            if self.gatenum - ctlinjoincell > 1:
                ctlinjoin = self.qubits[ctl]['components'][-1]
                ctlin_name, ctlout_name, ctlin_val, ctlout_val = self.make_chain(ctlin_name, ctlout_name, ctlin_val, ctlout_val, ctlinjoin, ctl)


        # place rows that are never dependent on gates previous gates
        availablerows = [0,1,2,3]
        availablerows.pop(availablerows.index(ctlin_name%4))
        availablerows.pop(availablerows.index(targ_name%4))
        if ancin_name%4 not in availablerows:
            rowoffset = availablerows[0] - ancin_name%4
            ancin_name = ancin_name + rowoffset
            ancout_name = ancout_name + rowoffset

        #couplernames
        ancin_ancout_couplername = (min(ancin_name, ancout_name), max(ancin_name, ancout_name))
        ancin_ctlout_couplername = (min(ancin_name, ctlout_name), max(ancin_name, ctlout_name))
        ancout_targ_couplername = (min(ancout_name, targ_name), max(ancout_name, targ_name))
        ancin_out_couplername = (min(ancin_name, out_name), max(ancin_name, out_name))
        ctlin_ctlout_couplername = (min(ctlin_name, ctlout_name), max(ctlin_name, ctlout_name))
        ctlin_out_couplername = (min(ctlin_name, out_name), max(ctlin_name, out_name))
        ctlout_targ_couplername = (min(ctlout_name, targ_name), max(ctlout_name, targ_name))
        targ_out_couplername = (min(targ_name, out_name), max(targ_name, out_name))

        self.qubits[ctl]['components'].append(ctlin_name)
        self.qubits[ctl]['components'].append(ctlout_name)
        self.qubitweights[ctlin_name] = ctlin_val
        self.qubitweights[ctlout_name] = ctlout_val

        self.qubits[targ]['components'].append(targ_name)
        self.qubits[targ]['components'].append(out_name)
        self.qubitweights[targ_name] = targ_val
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
        
        print('ctl', ctlin_name)
        print('targ', targ_name)
        print('anc', ancin_name)


    def add_Toffoli(self, ctl1, ctl2, targ):
        pass 

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
        # if destination even, move verticaldist + 1
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
            newqubitrow = newqubit % 4
            inname = inname + newqubitrow
            outname = outname + newqubitrow

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
            newqubitrow = newqubit % 4
            inname = inname + newqubitrow
            outname = outname + newqubitrow

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
