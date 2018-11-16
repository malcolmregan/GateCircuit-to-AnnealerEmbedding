

from copy import deepcopy
import uuid
import logging


from converter.qiskit import transpiler
from converter.qiskit.transpiler._passmanager import PassManager
from converter.qiskit.qobj import Qobj, QobjConfig, QobjExperiment, QobjItem, QobjHeader
from converter.qiskit.unroll import DagUnroller, JsonBackend
from converter.qiskit.transpiler._parallel import parallel_map



def compile(circuits, backend,
    pass










def dags_2_qobj(dags, backend_name, config=None, shots=None,
    pass










def _dags_2_qobj_parallel(dag, config=None, basis_gates=None, coupling_map=None):
    pass





def execute(circuits, backend,
    pass


