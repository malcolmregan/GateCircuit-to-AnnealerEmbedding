

from copy import deepcopy
import uuid
import logging


from converter.qiskit import transpiler
from converter.qiskit.transpiler._passmanager import PassManager
from converter.qiskit.qobj import Qobj, QobjConfig, QobjExperiment, QobjItem, QobjHeader
from converter.qiskit.unroll import DagUnroller, JsonBackend
from converter.qiskit.transpiler._parallel import parallel_map



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





def execute(circuits, backend=None,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):
    
    print(circuits)

    trutab = self.truthtable
    eqns = get_ineq_from_truthtable(trutab)

    stop = False
    count = 0
    while stop == False and count<1000:
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
        print(count)
        if count == 1000:
            yn = 'x'
            while yn is not 'y' and yn is not 'n':
                yn = input("Couldn''t find solution. Add Ancilla? (y/n) ")
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


