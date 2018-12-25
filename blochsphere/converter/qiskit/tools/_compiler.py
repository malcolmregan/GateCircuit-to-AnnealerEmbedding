

from copy import deepcopy
import uuid
import logging


#from converter.qiskit import transpiler
#from converter.qiskit.transpiler._passmanager import PassManager
#from converter.qiskit.qobj import Qobj, QobjConfig, QobjExperiment, QobjItem, QobjHeader
#from converter.qiskit.unroll import DagUnroller, JsonBackend
#from converter.qiskit.transpiler._parallel import parallel_map

from converter.qiskit.get_annealer_encoding import *
from converter.qiskit.solve_sys_multivar_ineq import *


def compile(circuits, backend,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):
    pass










def dags_2_qobj(dags, backend_name, config=None, shots=None,
                max_credits=None, qobj_id=None, basis_gates=None, coupling_map=None,
                seed=None):
    pass










def _dags_2_qobj_parallel(dag, config=None, basis_gates=None, coupling_map=None):
    pass





def execute(circuit, backend=None,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):

    # 1) find ancillas - output bits that dont get measured
    #                    and for which there is a logically 
    #                    equivalent reduced truthtable without
    #                    them. (ie output bits that dont get 
    #                    and are logically don't-cares)
    # 
    # 2) Reduce truth table
    #
    # 3) Solve

    names = circuit.truthtable.inputnames
    outidxs = [i for i, x in enumerate(circuit.truthtable.inputtypes) if x == 'Circ_Output']
    circoutputnames = [names[i] for i in outidxs]
    measuredqubits = circuit.data
    ancillas = [x for x in circoutputnames if x not in measuredqubits]
    ancidx = [i for i, x in enumerate(circuit.truthtable.inputnames) if x in ancillas]

    

    for idx in ancidx:
        circuit.truthtable.inputtypes[idx] = 'Ancilla'

    #for i in range(len(circuit.truthtable.outputs)):
    #    print(circuit.truthtable.graycode[i], circuit.truthtable.outputs[i])
    #print("\n")
    
    beforelen = circuit.truthtable.numinputs
    circuit.truthtable.reduce_truthtable()
    afterlen = circuit.truthtable.numinputs

    #for i in range(len(circuit.truthtable.outputs)):
    #    print(circuit.truthtable.graycode[i], circuit.truthtable.outputs[i])
    #print("\n")
    #print(circuit.truthtable.inputnames)

    if afterlen < beforelen:
        if beforelen - afterlen == 1:
            print("Truthtable reduced: 1 ancilla removed")
        else:
            print("Truthtable reduced: {} ancillas removed".format(beforelen - afterlen))


    trutab = circuit.truthtable
    eqns = get_ineq_from_truthtable(trutab)

    stop = False
    count = 0
    maxcount = 10000
    reportsteps = 100

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
        if count % reportsteps == 0:
            print("{}/{} attempts made to solve".format(count, maxcount))
        if count == maxcount:
            yn = 'x'
            while yn is not 'y' and yn is not 'n':
                yn = 'y' #input("Couldn't find solution. Add Ancilla? (y/n) ")
                if yn is 'y':
                    trutab.add_ancilla()
                    eqns = get_ineq_from_truthtable(trutab)
                    count = 0
                if yn is 'n':
                    stop = True

    #print("Count = {}".format(count))

    print("\nAnnealer Encoding:")
    for symbol in symbols:
        print(symbol.name, "\t", symbol.value)
    print("\nCheck:")
    for i in range(len(eqns)):
        print(correct[i]['valid'], "\t-\t", eqns[i])
    print("\nAncillas added: {}".format(trutab.ancillasadded))


