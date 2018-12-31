

from copy import deepcopy
import uuid
import logging


#from converter.qiskit import transpiler
#from converter.qiskit.transpiler._passmanager import PassManager
#from converter.qiskit.qobj import Qobj, QobjConfig, QobjExperiment, QobjItem, QobjHeader
#from converter.qiskit.unroll import DagUnroller, JsonBackend
#from converter.qiskit.transpiler._parallel import parallel_map
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.cloud.exceptions import SolverOfflineError
import minorminer

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





def execute(circuit, backend = None,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):

    outputs = list()
    inputs = list()

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == True:
                outputs.append(circuit.annealergraph.qubits[qubit]['components'][-1])
                # can't omit output bit from being included as input, but is its put
                # first in the list, it will be zero the top portion of the readout
                inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == False:
                inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])

    qubit_weights = circuit.annealergraph.qubitweights
    coupler_weights = circuit.annealergraph.couplerweights

    bqm = dimod.BinaryQuadraticModel(qubit_weights, coupler_weights, 0, dimod.BINARY)
    sampler = DWaveSampler(endpoint='https://cloud.dwavesys.com/sapi', token = 'DEV-beb5d0babc40334f66b655704f1b5315917b4c41', solver = 'DW_2000Q_2_1')
    
    #_, target_edgelist, target_adjacency = sampler.structure
    #embedding = minorminer.find_embedding(bqm.quadratic, target_edgelist)
    #bqm_embedded = dimod.embed_bqm(bqm, embedding, target_adjacency, 3.0)
    
    kwargs = {}
    if 'num_reads' in sampler.parameters:
        kwargs['num_reads'] = 5000
    if 'answer_mode' in sampler.parameters:
        kwargs['answer_mode'] = 'histogram'
    response = sampler.sample(bqm, **kwargs)
    #response = dimod.unembed_response(response, embedding, source_bqm=bqm)
    
    sampler.client.close()
    print(response.data)
    input()
    
    ''' 
    # ExactSolver simulation
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
    '''