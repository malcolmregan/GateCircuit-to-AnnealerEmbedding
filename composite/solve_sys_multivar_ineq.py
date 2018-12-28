import numpy as np
from random  import randint, uniform, shuffle

boundmax = 10000
num = '0123456789'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
oper = '+-*/'
rel = '=><'

class SYM:
    def __init__(self, name, sys):
        self.name = name
        self.bounds = [-boundmax, boundmax]
        self.value = 0
        self.isknown = False
        self.bounddist = self.bounds[1]-self.bounds[0]
        self.constraints = self.get_symbolic_constraints(sys)
        self.isdisjointwithsys = False
    
    def updatebounds(self, low, high):
        self.bounds = [round(low,1), round(high,1)]
        self.bounddist = self.bounds[1]-self.bounds[0]
        if self.bounddist > 0:
            self.value = round(uniform(self.bounds[0], self.bounds[1]), 1)
            self.isknown = False
        else:
            self.value = round(self.bounds[0],1)
            self.isknown = True
    
    def get_symbolic_constraints(self, sys):
        constraints = list()

        for ineq in sys:
            if self.name in ineq:
                if '=' in ineq:
                    relation = '='
                if '>' in ineq:
                    relation = '>'
                if '<' in ineq:
                    relation = '<'

                splitineq = str.split(ineq, relation)
                LHS = splitineq[0]
                RHS = splitineq[1]
                
                Llist = str.split(LHS, ' ')[:-1]
                Rlist = str.split(RHS, ' ')[1:]
                
                if self.name in Rlist:
                    temp = Rlist
                    Rlist = Llist
                    Llist = temp
                    if relation != '=':
                        if relation == '<':
                            rela = '>'
                        if relation == '>':
                            rela = '<'
                        relation = rela
                    
                delidxs = list()
                for i in range(len(Llist)):
                    if len(Llist[i]) > 1:
                        elem = Llist[i][0]
                    else:
                        elem = Llist[i]
                    if elem in alpha and Llist[i] != self.name:
                        if i==0:
                            Rlist.append('-')
                            Rlist.append(Llist[i])
                            delidxs.append(i)

                        else:
                            if Llist[i-1] == '+':
                                Rlist.append('-')
                            else:
                                Rlist.append('+')
                            Rlist.append(Llist[i])
                            delidxs.append(i)
                            delidxs.append(i-1)
                    if Llist[i] == self.name and i > 0:
                        delidxs.append(i-1)


                delidxs.sort()
                count = 0
                for i in delidxs:
                    Llist.pop(i-count)
                    count = count + 1

                RHS = ''
                for i in range(len(Rlist)):
                    RHS = RHS + Rlist[i]
                    if i < len(Rlist)-1:
                        RHS = RHS + ' '
                
                
                ## This is probably unnecesary. #####################
                
                if RHS in num:
                    if relation == '=':
                        self.updatebounds(round(float(RHS),1),round(float(RHS),1))
                    if relation == '>':
                        self.updatebounds(round(float(RHS),1),boundmax)
                    if relation == '<':
                        self.updatebounds(-boundmax,round(float(RHS),1))
                if len(RHS)>1:
                    if RHS[0] not in alpha and RHS[1] in num:
                        if relation == '=':
                            self.updatebounds(round(float(RHS),1),round(float(RHS),1))
                        if relation == '>':
                            self.updatebounds(round(float(RHS),1),boundmax)
                        if relation == '<':
                            self.updatebounds(-boundmax,round(float(RHS),1))

                #####################################################
                

                constraint = {'relation': relation, 'expression': RHS}
                constraints.append(constraint)

        return constraints

def extract_symbols(sys_ineq):
    syms = list()
    for i in range(len(sys_ineq)):
        components = str.split(sys_ineq[i], ' ')
        for j in range(len(components)):
            if len(components[j]) > 1:
                if components[j][0] in alpha:
                    syms.extend([components[j]])
            else:
                if components[j] in alpha:
                    syms.extend([components[j]])
    syms = list(set(syms))
    for i in range(len(syms)):
        syms[i] = SYM(syms[i], sys_ineq)
    return syms

def intersection(b1, b2, rel=None):
    if rel == None:
        rel = '='

    inter = [0,0]
    if rel == '=':
        if b2[0]>b1[1] or b1[0]>b2[1]:
            return 'disjoint'
        else:
            inter[0] = max(b1[0],b2[0])
            inter[1] = min(b1[1],b2[1])
            return inter

    if rel == '>':
        if b1[1] < b2[0]:
            return 'disjoint'
        else:
            inter[0] = max(b1[0],b2[0])
            inter[1] = min(b1[1],b2[1])
            return inter

    if rel == '<':
        if b1[0] > b2[1]:
            return 'disjoint'
        else:
            inter[0] = max(b1[0],b2[0])
            inter[1] = min(b1[1],b2[1])
            return inter

def update_bounds(syms):

    names = ['']*len(syms)
    for i in range(len(names)):
        names[i] = syms[i].name
    
    for sym in syms:
        if sym.isknown == False:
            for constraint in sym.constraints:
                relation = constraint['relation']
                RHS = str.split(constraint['expression'])
                
                RHSbound = [0,0]
                for i in range(len(RHS)):
                    if RHS[i] in names:
                        Rsym = syms[names.index(RHS[i])]
                        if i == 0:
                            RHSbound[0] = RHSbound[0] + Rsym.bounds[0]
                            RHSbound[1] = RHSbound[1] + Rsym.bounds[1]
                        else:
                            if RHS[i-1] == '-':
                                RHSbound[0] = RHSbound[0] - Rsym.bounds[0]
                                RHSbound[1] = RHSbound[1] - Rsym.bounds[1]
                            if RHS[i-1] == '+':
                                RHSbound[0] = RHSbound[0] + Rsym.bounds[0]
                                RHSbound[1] = RHSbound[1] + Rsym.bounds[1]
                    
                    # change this block
                    # determine if RHS[i] is a number
                    # negative, postive, long, short, whatever
                    if len(RHS[i])>1:
                        if RHS[i][0] not in alpha and RHS[i][1] in num:
                            if i == 0:
                                RHSbound[0] = RHSbound[0] + float(RHS[i])
                                RHSbound[1] = RHSbound[1] + float(RHS[i])
                            else:
                                if RHS[i-1] == '-':
                                    RHSbound[0] = RHSbound[0] - float(RHS[i])
                                    RHSbound[1] = RHSbound[1] - float(RHS[i])
                                if RHS[i-1] == '+':
                                    RHSbound[0] = RHSbound[0] + float(RHS[i])
                                    RHSbound[1] = RHSbound[1] + float(RHS[i])

                    #change this too
                    if RHS[i] in num:
                        if i == 0:
                            RHSbound[0] = RHSbound[0] + float(RHS[i])
                            RHSbound[1] = RHSbound[1] + float(RHS[i])
                        else:
                            if RHS[i-1] == '-':
                                RHSbound[0] = RHSbound[0] - float(RHS[i])
                                RHSbound[1] = RHSbound[1] - float(RHS[i])
                            if RHS[i-1] == '+':
                                RHSbound[0] = RHSbound[0] + float(RHS[i])
                                RHSbound[1] = RHSbound[1] + float(RHS[i])
               



                if RHSbound[0]>RHSbound[1]:
                    temp = RHSbound[0]
                    RHSbound[0] = RHSbound[1]
                    RHSbound[1] = temp

                if RHSbound[0] < -boundmax:
                    RHSbound[0] = -boundmax
                if RHSbound[1] > boundmax:
                    RHSbound[1] = boundmax
 
                inter = intersection(sym.bounds, RHSbound, rel=relation)
                if inter == 'disjoint':
                    #print('disjoint bounds:', sym.name, sym.bounds, constraint['relation'], constraint['expression'], RHSbound)
                    sym.isdisjointwithsys = True
                    return

                if inter[1]-inter[0] < sym.bounddist:                 
                    if relation == '=':
                        sym.updatebounds(inter[0],inter[1])
                    if relation == '<':
                        sym.updatebounds(sym.bounds[0],inter[1])
                    if relation == '>':
                        sym.updatebounds(inter[0], sym.bounds[1])
                
                #print(sym.name, sym.bounds, constraint['relation'], constraint['expression'], RHSbound)
    
    return

def tighten_bounds(syms):
    newbounds = [[0,0] for x in range(len(syms))]
    oldbounds = [[-boundmax,boundmax] for x in range(len(syms))]
    while not newbounds == oldbounds:
        update_bounds(syms)
        for i in range(len(syms)):
            oldbounds[i] = newbounds[i]
            newbounds[i] = syms[i].bounds
    return

def find_best_sym(syms):
    bestunknowncount = len(syms)
    bestbounddist = 2*boundmax

    symlist = ['']*len(syms)
    for i in range(len(symlist)):
        symlist[i] = syms[i]
    
    bestsym = ''

    for sym in syms:
        if sym.isknown == False:
            for constraint in sym.constraints:
                expression = constraint['expression']
                unknowncount = 0
                for Rsym in symlist:
                    if Rsym.name in expression:
                        if Rsym.isknown == False:
                            unknowncount = unknowncount + 1
                #print(sym.name, constraint['relation'], expression, unknowncount) 
                if unknowncount <= bestunknowncount and unknowncount > 0:
                    if sym.bounddist <= bestbounddist:
                            bestsym = sym
                            bestbounddist = sym.bounddist
                            bestunknowncount = unknowncount
   
    if bestsym == '':
        for sym in syms:
            if sym.isknown == False:
                bestsym = sym

    return bestsym

def pick_value(syms):
    sym = find_best_sym(syms)
    offset = 0.1
    val = round(uniform(sym.bounds[0]+offset,sym.bounds[1]-offset),1)
    sym.updatebounds(val,val)
    
    #print("value picked for {}: {}".format(sym.name,sym.value))
    return

def determine_symbol_values(syms):
    tighten_bounds(syms)
    system_solved = True
    for sym in syms:
        check = sym.isknown
        if check == False:
            system_solved = False

    #print("After first bound tightening\n\tNew bounds:")
    #for sym in syms:
    #    print("\t\t",sym.name, sym.bounds)
    #print("\n")

    while system_solved == False:
        pick_value(syms)
        tighten_bounds(syms)
        #print("\tNew bounds:")
        #for sym in syms:
        #    print("\t\t",sym.name, sym.bounds)
        #print("\n")

        system_solved = True
        for sym in syms:
            check = sym.isknown
            if check == False:
                system_solved = False
        
    return syms

def solve(sys_ineq):
    syms = extract_symbols(sys_ineq)
    #print("After symbol initialization\n\tBounds:")
    #for sym in syms:
    #    print("\t\t",sym.name, sym.bounds)
    #print("\n")

    determine_symbol_values(syms)

    return syms

def evaluate_sys(sys_ineq, syms):
    
    iscorrect = list()
    for ineq in sys_ineq:
        if '=' in ineq:
            relation = '='
        if '>' in ineq:
            relation = '>'
        if '<' in ineq:
            relation = '<'

        splitineq = str.split(ineq, relation)
        LHS = splitineq[0]
        RHS = splitineq[1]

        Llist = str.split(LHS, ' ')[:-1]
        Rlist = str.split(RHS, ' ')[1:]

        knowncount = 0
        for sym in syms:
            if sym.isknown == True:
                knowncount = knowncount + 1
        if knowncount == len(syms):
            allknown = True
        else:
            allknown = False

        Lval = 0
        for elem in Llist:
            for sym in syms:
                if elem == sym.name:
                    Lval = Lval + sym.value
            if len(elem)>1:
                if elem[0] not in alpha and elem[1] in num:
                    Lval = Lval + float(elem)


        Rval = 0
        for elem in Rlist:
            for sym in syms:
                if elem == sym.name:
                    Rval = Rval + sym.value
                
            if len(elem)>1:
                if elem[0] not in alpha and elem[1] in num:
                    Rval = Rval + float(elem)
                    

        if relation == '=':
            iscorrect.append({'inequality': ineq, 'valid': round(float(Lval),1) == round(float(Rval),1)})
        if relation == '>':
            iscorrect.append({'inequality': ineq, 'valid': Lval > Rval})
        if relation == '<':
            iscorrect.append({'inequality': ineq, 'valid': Lval < Rval})

        
    return iscorrect
   
def evaluate_constraints(syms):
    pass


def main():
    ''' 
    # XOR encoding (4 bit)
    system_inequalities = ['0 = G',
                           'w0 > G',
                           'w1 > G',
                           'w1 + J01 + w0 > G',
                           'w2 > G',
                           'w2 + J02 + w0 > G',
                           'w2 + J12 + w1 = G',
                           'w2 + J12 + J02 + w1 + J01 + w0 > G',
                           'w3 > G',
                           'w3 + J03 + w0 > G',
                           'w3 + J13 + w1 = G',
                           'w3 + J13 + J03 + w1 + J01 + w0 > G',
                           'w3 + J23 + w2 > G',
                           'w3 + J23 + J03 + w2 + J02 + w0 = G',
                           'w3 + J23 + J13 + w2 + J12 + w1 > G',
                           'w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G',
                           'w3 = 50',
                           'w2 = 50',
                           'w1 = 50',
                           'w0 = 500',
                           'J02 = -300',
                           'J23 = 80',
                           'J12 = -100',
                           'J13 = -100']

    inputs = ['w2','w3']
    outputs = ['w1'] 
    '''
    
    '''
    # XNOR encoding (4 bit)
    system_inequalities = ['0 > G',
                           'w0 > G',
                           'w1 = G',
                           'w1 + J01 + w0 > G',
                           'w2 = G',
                           'w2 + J02 + w0 > G',
                           'w2 + J12 + w1 > G',
                           'w2 + J12 + J02 + w1 + J01 + w0 > G',
                           'w3 = G',
                           'w3 + J03 + w0 > G',
                           'w3 + J13 + w1 > G',
                           'w3 + J13 + J03 + w1 + J01 + w0 > G',
                           'w3 + J23 + w2 > G',
                           'w3 + J23 + J03 + w2 + J02 + w0 > G',
                           'w3 + J23 + J13 + w2 + J12 + w1 > G',
                           'w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 = G',
                           'w3 = -50',
                           'w2 = -50',
                           'w1 = -50',
                           'w0 = 500',
                           'J02 = -300',
                           'J23 = 80',
                           'J12 = 100',
                           'J13 = 100']
    
    inputs = ['w2','w3']
    outputs = ['w1']
    '''

    '''
    # Combine XOR and NOT into XNOR. XOR qubits as above, NOT output = q4, NOT input = q5
    # split q4 and q5 ...
    system_inequalities = ['0 > G', 
                           'w0 > G', 
                           'w1 > G', 
                           'w1 + J01 + w0 > G', 
                           'w2 > G', 
                           'w2 + J02 + w0 > G', 
                           'w2 + J12 + w1 > G', 
                           'w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w3 > G', 
                           'w3 + J03 + w0 > G', 
                           'w3 + J13 + w1 > G', 
                           'w3 + J13 + J03 + w1 + J01 + w0 > G', 
                           'w3 + J23 + w2 > G', 
                           'w3 + J23 + J03 + w2 + J02 + w0 > G', 
                           'w3 + J23 + J13 + w2 + J12 + w1 > G', 
                           'w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w4 > G', 
                           'w4 + J04 + w0 > G', 
                           'w4 + J14 + w1 > G', 
                           'w4 + J14 + J04 + w1 + J01 + w0 > G', 
                           'w4 + J24 + w2 > G', 
                           'w4 + J24 + J04 + w2 + J02 + w0 > G', 
                           'w4 + J24 + J14 + w2 + J12 + w1 = G', 
                           'w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w4 + J34 + w3 > G', 
                           'w4 + J34 + J04 + w3 + J03 + w0 > G', 
                           'w4 + J34 + J14 + w3 + J13 + w1 = G', 
                           'w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                           'w4 + J34 + J24 + w3 + J23 + w2 > G', 
                           'w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 
                           'w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 
                           'w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w5 = G', 
                           'w5 + J05 + w0 > G', 'w5 + J15 + w1 > G', 
                           'w5 + J15 + J05 + w1 + J01 + w0 > G', 'w5 + J25 + w2 > G', 
                           'w5 + J25 + J05 + w2 + J02 + w0 > G', 
                           'w5 + J25 + J15 + w2 + J12 + w1 > G', 
                           'w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w5 + J35 + w3 > G', 
                           'w5 + J35 + J05 + w3 + J03 + w0 > G', 
                           'w5 + J35 + J15 + w3 + J13 + w1 > G', 
                           'w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                           'w5 + J35 + J25 + w3 + J23 + w2 > G',
                           'w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 > G', 
                           'w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 = G', 
                           'w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w5 + J45 + w4 > G', 
                           'w5 + J45 + J05 + w4 + J04 + w0 > G', 
                           'w5 + J45 + J15 + w4 + J14 + w1 > G', 
                           'w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 
                           'w5 + J45 + J25 + w4 + J24 + w2 > G', 
                           'w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 > G', 
                           'w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 
                           'w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 
                           'w5 + J45 + J35 + w4 + J34 + w3 > G', 
                           'w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 
                           'w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 
                           'w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 
                           'w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 
                           'w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 
                           'w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 
                           'w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G',
                           'w2 = 50',
                           'w3 = 50',
                           'w1 = 300',
                           'w5 = -50',
                           'J04 = 0',
                           'J05 = 0',
                           'J15 = 0',
                           #'J24 = 0',
                           'J25 = 0',
                           #'J34 = 0',
                           'J35 = 0'] 
    
    
    # outN    inN     in2X    in1X    outX    anc    
    # w5      w4      w3      w2      w1      w0
    # 1       0       0       0       0       0                                  
    # 0       1       0       1       1       0 
    # 0       1       1       0       1       0 
    # 1       0       1       1       0       1 
    
    inputs = ['w2','w3']
    outputs = ['w5']
    '''

    
    # compose 2 XORS into an embedding for the following circuit

    #    X1  X2           
    # a --o------- a      a b c o
    #     |               0 0 0|0
    #     | o1            0 0 1|1
    # b --x----o-- b      0 1 0|1
    #          |          0 1 1|0
    # c -------x-- o      1 0 0|1
    #                     1 0 1|0
    #                     1 1 0|0
    #                     1 1 1|1
    #
    #
    #       a       b       o1              o1       c      o 
    # X1a   X1i1    X1i2    X1o  |  X2a     X2i1    X2i2    X2o        line
    # 0     0       0       0    |  0       0       0       0          0   
    # 0     1       0       1    |  0       1       0       1          85  
    # 0     0       1       1    |  0       1       0       1          53
    # 0     0       0       0    |  0       0       1       1          3
    # 1     1       1       0    |  0       0       0       0          224
    # 0     1       0       1    |  1       1       1       0          94
    # 0     0       1       1    |  1       1       1       0          62
    # 1     1       1       0    |  0       0       1       1          227
    # 
    # General XOR embedding:
    # 
    #    Ancilla         J01 = 3263.6        Output
    #  w0 = 500.0 O------------------------O w1 = 50.0            
    #             |'.    J03 =           .'|                     
    # 		  |  ''. -380.0       .''  |                     
    #		  |     ''.        .''     |                      
    #		  |        ''.  .''        |                       
    # J02 =-300.0 |          .''.          | J13 = -100.0          
    #		  |       .''    ''.       |                      
    #		  |    .''J12 =     ''.    |                      
    #		  |,.''  -100.0        ''.,|                      
    #   w2 = 50.0 O------------------------O w3 = 50.0   
    #     Input		 J23 = 80.0          Input    
    #
    # Combine XOR embedding:
    #
    #                                                  o1 
    #              Ancilla         J01 = 3263.6        Output
    #            w0 = 500.0 O------------------------O w1 = ?               
    #                       |'.    J03 =           .'|',                   
    #                       |  ''. -380.0       .''  |  '--------------.   
    #                       |     ''.        .''     |                 |    
    #                       |        ''.  .''        |                 |      
    #           J02 =-300.0 |          .''.          | J13 = -100.0    |      
    #                       |       .''    ''.       |                 |     
    #                       |    .''J12 =     ''.    |                 |         
    #             a         |,.''  -100.0        ''.,| b               |     
    #             w2 = 50.0 O------------------------O w3 = 50.0       |
    #             Input            J23 = 80.0          Input           |
    #                                                                  |
    #                                                                  | 
    #                                                                  |
    #                                                                  |
    #                                                                  |
    #                                                 o                | J16 = ?
    #             Ancilla         J45 = 3263.6        Output           |
    #           w4 = 500.0 O------------------------O w5 = 50.0        |   
    #                      |'.    J47 =           .'|                  |  
    #                      |  ''. -380.0       .''  |                  |  
    #                      |     ''.        .''     |                  |   
    #                      |        ''.  .''        |                  |    
    #          J46 =-300.0 |          .''.          | J57 = -100.0     |    
    #                      |       .''    ''.       |                  |   
    #                      |    .''J56 =     ''.    |                  |   
    #            o1        |,.''  -100.0        ''.,| c                |   
    #            w6 = ?    O------------------------O w7 = 50.0        |
    #              Input   |      J67 = 80.0          Input            |
    #                      ',                                          |
    #                        '-----------------------------------------'
    inputs = ['w2','w3','w7']
    outputs = ['w5']
    

    #system_inequalities = ['0 = G', 'w0 > G', 'w1 > G', 'w1 + J01 + w0 = G', 'w2 > G', 'w2 + J02 + w0 > G', 'w2 + J12 + w1 > G', 'w2 + J12 + J02 + w1 + J01 + w0 > G', 'w3 > G', 'w3 + J03 + w0 > G', 'w3 + J13 + w1 > G', 'w3 + J13 + J03 + w1 + J01 + w0 > G', 'w3 + J23 + w2 > G', 'w3 + J23 + J03 + w2 + J02 + w0 > G', 'w3 + J23 + J13 + w2 + J12 + w1 > G', 'w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w4 > G', 'w4 + J04 + w0 > G', 'w4 + J14 + w1 > G', 'w4 + J14 + J04 + w1 + J01 + w0 > G', 'w4 + J24 + w2 > G', 'w4 + J24 + J04 + w2 + J02 + w0 > G', 'w4 + J24 + J14 + w2 + J12 + w1 > G', 'w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w4 + J34 + w3 > G', 'w4 + J34 + J04 + w3 + J03 + w0 > G', 'w4 + J34 + J14 + w3 + J13 + w1 > G', 'w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w4 + J34 + J24 + w3 + J23 + w2 > G', 'w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w5 > G', 'w5 + J05 + w0 > G', 'w5 + J15 + w1 > G', 'w5 + J15 + J05 + w1 + J01 + w0 > G', 'w5 + J25 + w2 > G', 'w5 + J25 + J05 + w2 + J02 + w0 > G', 'w5 + J25 + J15 + w2 + J12 + w1 > G', 'w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w5 + J35 + w3 > G', 'w5 + J35 + J05 + w3 + J03 + w0 > G', 'w5 + J35 + J15 + w3 + J13 + w1 > G', 'w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w5 + J35 + J25 + w3 + J23 + w2 > G', 'w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w5 + J45 + w4 > G', 'w5 + J45 + J05 + w4 + J04 + w0 > G', 'w5 + J45 + J15 + w4 + J14 + w1 > G', 'w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w5 + J45 + J25 + w4 + J24 + w2 > G', 'w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 = G', 'w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w5 + J45 + J35 + w4 + J34 + w3 > G', 'w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 = G', 'w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 > G', 'w6 + J06 + w0 > G', 'w6 + J16 + w1 > G', 'w6 + J16 + J06 + w1 + J01 + w0 > G', 'w6 + J26 + w2 > G', 'w6 + J26 + J06 + w2 + J02 + w0 > G', 'w6 + J26 + J16 + w2 + J12 + w1 > G', 'w6 + J26 + J16 + J06 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J36 + w3 > G', 'w6 + J36 + J06 + w3 + J03 + w0 > G', 'w6 + J36 + J16 + w3 + J13 + w1 > G', 'w6 + J36 + J16 + J06 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w6 + J36 + J26 + w3 + J23 + w2 > G', 'w6 + J36 + J26 + J06 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w6 + J36 + J26 + J16 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w6 + J36 + J26 + J16 + J06 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J46 + w4 > G', 'w6 + J46 + J06 + w4 + J04 + w0 > G', 'w6 + J46 + J16 + w4 + J14 + w1 > G', 'w6 + J46 + J16 + J06 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w6 + J46 + J26 + w4 + J24 + w2 > G', 'w6 + J46 + J26 + J06 + w4 + J24 + J04 + w2 + J02 + w0 = G', 'w6 + J46 + J26 + J16 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w6 + J46 + J26 + J16 + J06 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J46 + J36 + w4 + J34 + w3 > G', 'w6 + J46 + J36 + J06 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w6 + J46 + J36 + J16 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w6 + J46 + J36 + J16 + J06 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w6 + J46 + J36 + J26 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w6 + J46 + J36 + J26 + J06 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w6 + J46 + J36 + J26 + J16 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 = G', 'w6 + J46 + J36 + J26 + J16 + J06 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J56 + w5 > G', 'w6 + J56 + J06 + w5 + J05 + w0 > G', 'w6 + J56 + J16 + w5 + J15 + w1 > G', 'w6 + J56 + J16 + J06 + w5 + J15 + J05 + w1 + J01 + w0 > G', 'w6 + J56 + J26 + w5 + J25 + w2 > G', 'w6 + J56 + J26 + J06 + w5 + J25 + J05 + w2 + J02 + w0 > G', 'w6 + J56 + J26 + J16 + w5 + J25 + J15 + w2 + J12 + w1 > G', 'w6 + J56 + J26 + J16 + J06 + w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J56 + J36 + w5 + J35 + w3 > G', 'w6 + J56 + J36 + J06 + w5 + J35 + J05 + w3 + J03 + w0 > G', 'w6 + J56 + J36 + J16 + w5 + J35 + J15 + w3 + J13 + w1 > G', 'w6 + J56 + J36 + J16 + J06 + w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w6 + J56 + J36 + J26 + w5 + J35 + J25 + w3 + J23 + w2 > G', 'w6 + J56 + J36 + J26 + J06 + w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w6 + J56 + J36 + J26 + J16 + w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w6 + J56 + J36 + J26 + J16 + J06 + w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J56 + J46 + w5 + J45 + w4 > G', 'w6 + J56 + J46 + J06 + w5 + J45 + J05 + w4 + J04 + w0 > G', 'w6 + J56 + J46 + J16 + w5 + J45 + J15 + w4 + J14 + w1 > G', 'w6 + J56 + J46 + J16 + J06 + w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w6 + J56 + J46 + J26 + w5 + J45 + J25 + w4 + J24 + w2 > G', 'w6 + J56 + J46 + J26 + J06 + w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 > G', 'w6 + J56 + J46 + J26 + J16 + w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w6 + J56 + J46 + J26 + J16 + J06 + w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w6 + J56 + J46 + J36 + w5 + J45 + J35 + w4 + J34 + w3 > G', 'w6 + J56 + J46 + J36 + J06 + w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w6 + J56 + J46 + J36 + J16 + w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w6 + J56 + J46 + J36 + J16 + J06 + w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w6 + J56 + J46 + J36 + J26 + w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w6 + J56 + J46 + J36 + J26 + J06 + w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w6 + J56 + J46 + J36 + J26 + J16 + w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w6 + J56 + J46 + J36 + J26 + J16 + J06 + w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 > G', 'w7 + J07 + w0 > G', 'w7 + J17 + w1 > G', 'w7 + J17 + J07 + w1 + J01 + w0 > G', 'w7 + J27 + w2 > G', 'w7 + J27 + J07 + w2 + J02 + w0 > G', 'w7 + J27 + J17 + w2 + J12 + w1 > G', 'w7 + J27 + J17 + J07 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J37 + w3 > G', 'w7 + J37 + J07 + w3 + J03 + w0 > G', 'w7 + J37 + J17 + w3 + J13 + w1 > G', 'w7 + J37 + J17 + J07 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J37 + J27 + w3 + J23 + w2 > G', 'w7 + J37 + J27 + J07 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J37 + J27 + J17 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J37 + J27 + J17 + J07 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J47 + w4 > G', 'w7 + J47 + J07 + w4 + J04 + w0 > G', 'w7 + J47 + J17 + w4 + J14 + w1 > G', 'w7 + J47 + J17 + J07 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w7 + J47 + J27 + w4 + J24 + w2 > G', 'w7 + J47 + J27 + J07 + w4 + J24 + J04 + w2 + J02 + w0 > G', 'w7 + J47 + J27 + J17 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w7 + J47 + J27 + J17 + J07 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J47 + J37 + w4 + J34 + w3 > G', 'w7 + J47 + J37 + J07 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w7 + J47 + J37 + J17 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w7 + J47 + J37 + J17 + J07 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J47 + J37 + J27 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w7 + J47 + J37 + J27 + J07 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J47 + J37 + J27 + J17 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J47 + J37 + J27 + J17 + J07 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J57 + w5 > G', 'w7 + J57 + J07 + w5 + J05 + w0 > G', 'w7 + J57 + J17 + w5 + J15 + w1 > G', 'w7 + J57 + J17 + J07 + w5 + J15 + J05 + w1 + J01 + w0 > G', 'w7 + J57 + J27 + w5 + J25 + w2 > G', 'w7 + J57 + J27 + J07 + w5 + J25 + J05 + w2 + J02 + w0 > G', 'w7 + J57 + J27 + J17 + w5 + J25 + J15 + w2 + J12 + w1 > G', 'w7 + J57 + J27 + J17 + J07 + w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J57 + J37 + w5 + J35 + w3 > G', 'w7 + J57 + J37 + J07 + w5 + J35 + J05 + w3 + J03 + w0 > G', 'w7 + J57 + J37 + J17 + w5 + J35 + J15 + w3 + J13 + w1 > G', 'w7 + J57 + J37 + J17 + J07 + w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J57 + J37 + J27 + w5 + J35 + J25 + w3 + J23 + w2 > G', 'w7 + J57 + J37 + J27 + J07 + w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J57 + J37 + J27 + J17 + w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J57 + J37 + J27 + J17 + J07 + w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J57 + J47 + w5 + J45 + w4 > G', 'w7 + J57 + J47 + J07 + w5 + J45 + J05 + w4 + J04 + w0 > G', 'w7 + J57 + J47 + J17 + w5 + J45 + J15 + w4 + J14 + w1 > G', 'w7 + J57 + J47 + J17 + J07 + w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w7 + J57 + J47 + J27 + w5 + J45 + J25 + w4 + J24 + w2 > G', 'w7 + J57 + J47 + J27 + J07 + w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 > G', 'w7 + J57 + J47 + J27 + J17 + w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w7 + J57 + J47 + J27 + J17 + J07 + w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J57 + J47 + J37 + w5 + J45 + J35 + w4 + J34 + w3 > G', 'w7 + J57 + J47 + J37 + J07 + w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w7 + J57 + J47 + J37 + J17 + w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w7 + J57 + J47 + J37 + J17 + J07 + w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J57 + J47 + J37 + J27 + w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w7 + J57 + J47 + J37 + J27 + J07 + w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J57 + J47 + J37 + J27 + J17 + w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J57 + J47 + J37 + J27 + J17 + J07 + w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + w6 > G', 'w7 + J67 + J07 + w6 + J06 + w0 > G', 'w7 + J67 + J17 + w6 + J16 + w1 > G', 'w7 + J67 + J17 + J07 + w6 + J16 + J06 + w1 + J01 + w0 > G', 'w7 + J67 + J27 + w6 + J26 + w2 > G', 'w7 + J67 + J27 + J07 + w6 + J26 + J06 + w2 + J02 + w0 > G', 'w7 + J67 + J27 + J17 + w6 + J26 + J16 + w2 + J12 + w1 > G', 'w7 + J67 + J27 + J17 + J07 + w6 + J26 + J16 + J06 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J37 + w6 + J36 + w3 > G', 'w7 + J67 + J37 + J07 + w6 + J36 + J06 + w3 + J03 + w0 > G', 'w7 + J67 + J37 + J17 + w6 + J36 + J16 + w3 + J13 + w1 > G', 'w7 + J67 + J37 + J17 + J07 + w6 + J36 + J16 + J06 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J67 + J37 + J27 + w6 + J36 + J26 + w3 + J23 + w2 > G', 'w7 + J67 + J37 + J27 + J07 + w6 + J36 + J26 + J06 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J67 + J37 + J27 + J17 + w6 + J36 + J26 + J16 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J67 + J37 + J27 + J17 + J07 + w6 + J36 + J26 + J16 + J06 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J47 + w6 + J46 + w4 > G', 'w7 + J67 + J47 + J07 + w6 + J46 + J06 + w4 + J04 + w0 > G', 'w7 + J67 + J47 + J17 + w6 + J46 + J16 + w4 + J14 + w1 > G', 'w7 + J67 + J47 + J17 + J07 + w6 + J46 + J16 + J06 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w7 + J67 + J47 + J27 + w6 + J46 + J26 + w4 + J24 + w2 > G', 'w7 + J67 + J47 + J27 + J07 + w6 + J46 + J26 + J06 + w4 + J24 + J04 + w2 + J02 + w0 > G', 'w7 + J67 + J47 + J27 + J17 + w6 + J46 + J26 + J16 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w7 + J67 + J47 + J27 + J17 + J07 + w6 + J46 + J26 + J16 + J06 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J47 + J37 + w6 + J46 + J36 + w4 + J34 + w3 > G', 'w7 + J67 + J47 + J37 + J07 + w6 + J46 + J36 + J06 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w7 + J67 + J47 + J37 + J17 + w6 + J46 + J36 + J16 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w7 + J67 + J47 + J37 + J17 + J07 + w6 + J46 + J36 + J16 + J06 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J67 + J47 + J37 + J27 + w6 + J46 + J36 + J26 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w7 + J67 + J47 + J37 + J27 + J07 + w6 + J46 + J36 + J26 + J06 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J67 + J47 + J37 + J27 + J17 + w6 + J46 + J36 + J26 + J16 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J67 + J47 + J37 + J27 + J17 + J07 + w6 + J46 + J36 + J26 + J16 + J06 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + w6 + J56 + w5 = G', 'w7 + J67 + J57 + J07 + w6 + J56 + J06 + w5 + J05 + w0 > G', 'w7 + J67 + J57 + J17 + w6 + J56 + J16 + w5 + J15 + w1 > G', 'w7 + J67 + J57 + J17 + J07 + w6 + J56 + J16 + J06 + w5 + J15 + J05 + w1 + J01 + w0 = G', 'w7 + J67 + J57 + J27 + w6 + J56 + J26 + w5 + J25 + w2 > G', 'w7 + J67 + J57 + J27 + J07 + w6 + J56 + J26 + J06 + w5 + J25 + J05 + w2 + J02 + w0 > G', 'w7 + J67 + J57 + J27 + J17 + w6 + J56 + J26 + J16 + w5 + J25 + J15 + w2 + J12 + w1 > G', 'w7 + J67 + J57 + J27 + J17 + J07 + w6 + J56 + J26 + J16 + J06 + w5 + J25 + J15 + J05 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J37 + w6 + J56 + J36 + w5 + J35 + w3 > G', 'w7 + J67 + J57 + J37 + J07 + w6 + J56 + J36 + J06 + w5 + J35 + J05 + w3 + J03 + w0 > G', 'w7 + J67 + J57 + J37 + J17 + w6 + J56 + J36 + J16 + w5 + J35 + J15 + w3 + J13 + w1 > G', 'w7 + J67 + J57 + J37 + J17 + J07 + w6 + J56 + J36 + J16 + J06 + w5 + J35 + J15 + J05 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J37 + J27 + w6 + J56 + J36 + J26 + w5 + J35 + J25 + w3 + J23 + w2 > G', 'w7 + J67 + J57 + J37 + J27 + J07 + w6 + J56 + J36 + J26 + J06 + w5 + J35 + J25 + J05 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J67 + J57 + J37 + J27 + J17 + w6 + J56 + J36 + J26 + J16 + w5 + J35 + J25 + J15 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J67 + J57 + J37 + J27 + J17 + J07 + w6 + J56 + J36 + J26 + J16 + J06 + w5 + J35 + J25 + J15 + J05 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J47 + w6 + J56 + J46 + w5 + J45 + w4 > G', 'w7 + J67 + J57 + J47 + J07 + w6 + J56 + J46 + J06 + w5 + J45 + J05 + w4 + J04 + w0 > G', 'w7 + J67 + J57 + J47 + J17 + w6 + J56 + J46 + J16 + w5 + J45 + J15 + w4 + J14 + w1 > G', 'w7 + J67 + J57 + J47 + J17 + J07 + w6 + J56 + J46 + J16 + J06 + w5 + J45 + J15 + J05 + w4 + J14 + J04 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J47 + J27 + w6 + J56 + J46 + J26 + w5 + J45 + J25 + w4 + J24 + w2 > G', 'w7 + J67 + J57 + J47 + J27 + J07 + w6 + J56 + J46 + J26 + J06 + w5 + J45 + J25 + J05 + w4 + J24 + J04 + w2 + J02 + w0 > G', 'w7 + J67 + J57 + J47 + J27 + J17 + w6 + J56 + J46 + J26 + J16 + w5 + J45 + J25 + J15 + w4 + J24 + J14 + w2 + J12 + w1 > G', 'w7 + J67 + J57 + J47 + J27 + J17 + J07 + w6 + J56 + J46 + J26 + J16 + J06 + w5 + J45 + J25 + J15 + J05 + w4 + J24 + J14 + J04 + w2 + J12 + J02 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J47 + J37 + w6 + J56 + J46 + J36 + w5 + J45 + J35 + w4 + J34 + w3 > G', 'w7 + J67 + J57 + J47 + J37 + J07 + w6 + J56 + J46 + J36 + J06 + w5 + J45 + J35 + J05 + w4 + J34 + J04 + w3 + J03 + w0 > G', 'w7 + J67 + J57 + J47 + J37 + J17 + w6 + J56 + J46 + J36 + J16 + w5 + J45 + J35 + J15 + w4 + J34 + J14 + w3 + J13 + w1 > G', 'w7 + J67 + J57 + J47 + J37 + J17 + J07 + w6 + J56 + J46 + J36 + J16 + J06 + w5 + J45 + J35 + J15 + J05 + w4 + J34 + J14 + J04 + w3 + J13 + J03 + w1 + J01 + w0 > G', 'w7 + J67 + J57 + J47 + J37 + J27 + w6 + J56 + J46 + J36 + J26 + w5 + J45 + J35 + J25 + w4 + J34 + J24 + w3 + J23 + w2 > G', 'w7 + J67 + J57 + J47 + J37 + J27 + J07 + w6 + J56 + J46 + J36 + J26 + J06 + w5 + J45 + J35 + J25 + J05 + w4 + J34 + J24 + J04 + w3 + J23 + J03 + w2 + J02 + w0 > G', 'w7 + J67 + J57 + J47 + J37 + J27 + J17 + w6 + J56 + J46 + J36 + J26 + J16 + w5 + J45 + J35 + J25 + J15 + w4 + J34 + J24 + J14 + w3 + J23 + J13 + w2 + J12 + w1 > G', 'w7 + J67 + J57 + J47 + J37 + J27 + J17 + J07 + w6 + J56 + J46 + J36 + J26 + J16 + J06 + w5 + J45 + J35 + J25 + J15 + J05 + w4 + J34 + J24 + J14 + J04 + w3 + J23 + J13 + J03 + w2 + J12 + J02 + w1 + J01 + w0 > G',
    #XOR 1 embedding
    system_inequalities = ['w0 = 500',
    'w2 = 50',
    'w3 = 50',
    'J01 = 3263.6',
    'J02 = -300',
    'J03 = -380',
    'J12 = -100',
    'J13 = -100',
    'J23 = 80',
    #XOR 2 embedding
    'w4 = 500',
    'w5 = 50',
    'w7 = 50',
    'J45 = 3263.6',
    'J46 = -300',
    'J47 = -380',
    'J56 = -100',
    'J57 = -100',
    'J67 = 80',
    # all couplers btwn XORS zero except J16
    'J04 = 0',
    'J05 = 0',
    'J06 = 0',
    'J07 = 0',
    'J14 = 0',
    'J15 = 0',
    'J17 = 0',
    'J24 = 0',
    'J25 = 0',
    'J26 = 0',
    'J27 = 0',
    'J34 = 0',
    'J35 = 0',
    'J36 = 0',
    'J37 = 0',
    'w1 = 100',
    'w6 = 100',
    'J16 = -100']
    

    ''' 
    # Half adder emdedding
    


    '''

    '''
    # Full adder embedding
    '''

############################################
############################################

    besttruecount = 0

    stop = False
    count = 0
    while stop == False:  
        shuffle(system_inequalities)
        symbols = solve(system_inequalities)
        
        correct = evaluate_sys(system_inequalities, symbols)
        truecount = 0
        falses = list()
        for elem in correct:
            #print(elem['valid'], "\t-", elem['inequality'])
            if elem['valid']==True:
                truecount = truecount + 1
            else:
                falses.append(elem['inequality'])
        #print("\n")

        if truecount >= besttruecount:
            best = list()
            for sym in symbols:
                a = [sym.name, sym.value]
                best.append(a)    
            besttruecount = truecount
            #print('best: ', besttruecount)
            bestfalse = falses
        if truecount == len(correct): 
            stop = True
        
        count = count + 1

        if count % 200 == 0:
            s = input('Tried {} times. Stop? (y/n) '.format(count))
            if s == 'y':
                stop = True
            elif s == 'n':
                stop = False
            else:
                stop = False
        print(count)
    
    print("\nSymbol Values: ")
    for entry in best:
        print("\t",entry[0],"\t",entry[1])

    print('{} were true, {} were false:'.format(besttruecount,len(system_inequalities)-besttruecount))
    for i in range(len(bestfalse)):
        print('False: ', bestfalse[i])

    import dimod

    qubit=list()
    qubitweight =list()
    coupler=list()
    couplerweight=list()
    offset = 0
  
    for sym in symbols:
        if 'w' in sym.name:
            qubit.append(sym.name)
            qubitweight.append(sym.value)
        if  'J' in sym.name:
            numbers = sym.name[1:]
            coupler.append(('w{}'.format(numbers[0]), 'w{}'.format(numbers[1])))
            couplerweight.append(sym.value)
        if sym.name == 'offset':
            offset = sym.value

    qubit_weights = {q:w for q,w in zip(qubit, qubitweight)}
    coupler_weights = {c:w for c,w in zip(coupler,couplerweight)}

    print(qubit_weights,coupler_weights)

    bqm = dimod.BinaryQuadraticModel(qubit_weights, coupler_weights, offset, dimod.BINARY)
    sampler = dimod.ExactSolver()
    response = sampler.sample(bqm)

    groundstate = 1000000
    for sample, energy in response.data(['sample','energy']):
        if energy<groundstate:
            groundstate = round(energy,1)

    function = list()
    for sample, energy in response.data(['sample', 'energy']):
        if round(energy,1) == groundstate:
            print(sample, round(energy,1))
            row = []
            for inp in inputs:
                row.append(sample[inp])
            for outp in outputs:
                row.append(sample[outp])
            function.append(row)
    print('\n')

    function.sort()
    for i in range(len(function)):
        print(function[i])


if __name__ == "__main__":
    main()
