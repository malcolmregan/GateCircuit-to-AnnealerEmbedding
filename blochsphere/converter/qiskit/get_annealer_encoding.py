import numpy as np
from random import randint
from converter.qiskit.solve_sys_multivar_ineq import *
from math import sqrt

class truth_table:
    def __init__(self, numinputs=None, outputs=None, inputnames=None, inputtypes=None):
        if numinputs is not None and outputs is None:
            self.numinputs = numinputs
            self.outputs = np.zeros(shape = (2 ** self.numinputs), dtype = np.int)
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)
            
        if numinputs is not None and outputs is 'Manual':
            self.numinputs = numinputs
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)
            self.manually_define_truth_table(self.numinputs)

        if numinputs is not None and outputs is not None and not outputs is 'Manual':
            self.numinputs = numinputs
            self.outputs = outputs
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)

        if numinputs is None and outputs is not None and not outputs is 'Manual':
            self.outputs = outputs
            self.numinputs = int(sqrt(len(outputs)))
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)

        if numinputs is None and outputs is None:
            numinputs = input("How many inputs? ")
            self.numinputs = int(numinputs)
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)
            self.manually_define_truth_table(self.numinputs)            

        if numinputs is None and outputs is 'Manual':
            numinputs = input("How many inputs? ")
            self.numinputs = int(numinputs)
            self.generategraycode(self.numinputs)
            self.get_input_attr(inputnames, inputtypes)
            self.manually_define_truth_table(self.numinputs)

        self.ancillasadded = 0    
    
    def get_input_attr(self, inputnames, inputtypes):
        self.inputnames = list()
        if inputnames is not None:
            if isinstance(inputnames, list) and len(inputnames)==self.numinputs:
                for name in inputnames:
                    self.inputnames.append(name)
            else:
                print('Input names must be given in a list with length equal to the number of inputs. Defaulting to q0, q1, etc.')
                inputnames = None
        if inputnames is None:
            for i in range(self.numinputs):
                self.inputnames.append('q{}'.format(i))

        self.inputtypes = list()
        if inputtypes is not None:
            if isinstance(inputtypes, list) and len(inputtypes)==self.numinputs:
                for typ in inputtypes:
                    self.inputtypes.append(typ)
            else:
                print('Input types must be given in a list with length equal to the number of inputs. Defaulting to ''Input''')
                inputtypes = None
        if inputtypes is None:
            for i in range(self.numinputs):
                self.inputtypes.append('Input')


    def generategraycode(self, numinputs):
        self.graycode = np.zeros(shape = (2 ** numinputs, numinputs), dtype = np.int)
        for i in range(2 ** numinputs):
            binstring = "{0:b}".format(i)
            binstring = "0"*(numinputs-len(binstring)) + binstring

            for j in range(numinputs):
                self.graycode[i,j] = int(binstring[j])


    def manually_define_truth_table(self, numinputs):

        print("\nFill in truth table (0 or 1): \n")

        for i in range(numinputs):
            print("| {} ".format(self.inputnames[numinputs-i-1]), end='')        
        print("|true?|")
        for i in range(numinputs):
            print("-----", end='')
        print("-------")

        self.outputs = np.zeros(shape = (2 ** numinputs), dtype = np.int) - 1
        for i in range(2 ** numinputs):
            for j in range(numinputs):
                print("|  {} ".format(self.graycode[i,j]), end='')
            print("|  ", end='')
            while self.outputs[i] != 0 and self.outputs[i] != 1:
                try: 
                    self.outputs[i] = int(input(""))
                except:
                    continue
        print("")

    def add_ancilla(self):
        # Right now it just puts all output ones on ancilla zeros except for the last output
        # which is put on an ancilla one maybe there is a better way to select which 
        # outputs are put on ancilla ones
        #
        # The maximum number of ancilla bits that can be added is the number
        # of 1's in truthtable.outputs - this shouldn't ever be an issue but may be worth 
        # implementing especially if the solver doesn't improve 
        
        self.numinputs = self.numinputs + 1
        self.generategraycode(self.numinputs)
        newoutputs = np.zeros(shape = (2 ** self.numinputs), dtype = np.int)
        idxs = np.where(self.outputs == 1)[0]
        for i in range(len(idxs)):
            idxs[i] = idxs[i]*2
            if i == len(idxs)-1-self.ancillasadded:
                idxs[i] = idxs[i]+1
            newoutputs[idxs[i]] = 1
        self.outputs = newoutputs
        self.inputnames.append('a{}'.format(self.ancillasadded))
        self.inputtypes.append('Ancilla')
        self.ancillasadded = self.ancillasadded + 1
        

    def reduce_truthtable(self):

        # Must change for bloch sphere representation
        pass
        '''
        ancillaidxs = []
        ancillanames = []
        for i in range(len(self.inputtypes)):
            if self.inputtypes[i]=='Ancilla':
                ancillaidxs.append(i)
                ancillanames.append(self.inputnames[i])
         
        ancillaidxs.reverse()
        ancillanames.reverse()
        
        count = 0 
        for idx in ancillaidxs:
            numberofswaps = len(self.inputnames) - idx - 1 - count 
            count = count + 1
            for i in range(numberofswaps):
                self.inputnames[idx+i], self.inputnames[idx+i+1] = self.inputnames[idx+i+1], self.inputnames[idx+i]
                self.inputtypes[idx+i], self.inputtypes[idx+i+1] = self.inputtypes[idx+i+1], self.inputtypes[idx+i]
                
                outputsone = np.where(self.outputs)[0]
        
                newones = [] 
                for j in outputsone:
                    self.outputs[j] = 0
                    row=[]
                    for g in range(len(self.graycode[j,:])):
                        row.append(self.graycode[j,g])
                    
                    row = np.asarray(row)
                    row[idx+i], row[idx+i+1] = row[idx+i+1], row[idx+i]
        
                    for k in range(len(self.outputs)):
                        if np.array_equal(row, self.graycode[k,:]):    
                            newones.append(k)
         
                for m in newones:
                    self.outputs[m] = 1

            #for i in range(len(self.outputs)):
            #    print(self.graycode[i], self.outputs[i])
            #print("\n")

        numancillas = len(ancillaidxs)
        for i in range(numancillas):
            self.numinputs = self.numinputs - 1
            newoutputs = np.zeros(shape = (2 ** self.numinputs), dtype = np.int)
            for j in range(len(newoutputs)):
                if 1 in self.outputs[2*j:2*j+2]:
                    newoutputs[j] = 1
                else:
                    newoutputs[j] = 0
            self.outputs = newoutputs
            self.inputnames.pop()
            self.inputtypes.pop()
            self.generategraycode(self.numinputs)
        '''

def get_ineq_from_truthtable(truthtable):
    numinputs = truthtable.numinputs
    graycode = truthtable.graycode
    outputs = truthtable.outputs

    w_ = ['']*numinputs
    for i in range(numinputs):
        symname = "w{}".format(numinputs-i-1)
        w_[i] = symname
    
    numcouplers = 0
    for i in range(numinputs):
        numcouplers = numcouplers + i
    J_ = ['']*numcouplers
    idx = 0
    for i in range(numinputs):
        for j in range(numinputs):
            if i<j:
                symname = "J{}{}".format(numinputs-j-1,numinputs-i-1)
                J_[idx] = symname
                idx=idx+1

    G = 'G'
    exps = [[] for x in range(2 ** numinputs)]
    eqns = [[] for x in range(2 ** numinputs)]

    for i in range(2 ** numinputs):
        idx = 0
        for j in range(numinputs):
            if graycode[i,j] == 1:
                exps[i].append(w_[j])
            for k in range(numinputs):
                if j<k:
                    if graycode[i,j] == 1 and graycode[i,k] == 1:
                        exps[i].append(J_[idx])
                    idx=idx+1

    for i in range(len(exps)):
        if len(exps[i]) == 0:
            exps[i].append('0')
        expstring = exps[i][0]
        if len(exps[i]) > 0: 
            for j in range(1, len(exps[i])):
                expstring = expstring + ' + ' + exps[i][j] 

        if outputs[i] == 1:
            eqns[i] = expstring + ' = ' + G
        else:
            eqns[i] = expstring + ' > ' + G
    
    return eqns

def main():
    trutab = truth_table()
    eqns = get_ineq_from_truthtable(trutab)

    stop = False
    count = 0
    while stop == False:
        symbols = solve(eqns)
        correct = evaluate_sys(eqns, symbols)
        truecount = 0
        for elem in correct:
            #print(elem['valid'], "\t-", elem['inequality'])
            if elem['valid']==True:
                truecount = truecount + 1
        if truecount == len(correct):
            stop = True
        count = count + 1
        print("{}/1000 attempts made to solve".format(count))
        if count == 1000:
            yn = 'x'
            while yn is not 'y' and yn is not 'n':
                yn = input("Couldn't find solution. Add Ancilla? (y/n) ")
                if yn is 'y':
                    trutab.add_ancilla()
                    eqns = get_ineq_from_truthtable(trutab)
                    count = 0
                if yn is 'n':
                    stop = True

    print("Count = {}".format(count))

    print("\nAnnealer Encoding:")
    for symbol in symbols:
        print(symbol.name, "\t", symbol.value, "\t", symbol.isknown)
    print("\nCheck:")
    for i in range(len(eqns)):
        print(correct[i]['valid'], "\t-\t", eqns[i])
    print("\nAncillas added: {}".format(trutab.ancillasadded))

if __name__=="__main__":
    main()
