


import itertools
from collections import OrderedDict

from converter.qiskit.qasm import _qasm
from converter.qiskit.unrollers import _unroller
from converter.qiskit.unrollers import _circuitbackend
from converter.qiskit._qiskiterror import QISKitError
from converter.qiskit._quantumregister import QuantumRegister
from converter.qiskit._classicalregister import ClassicalRegister
from converter.qiskit.tools import visualization


def _circuit_from_qasm(qasm, basis=None):
    pass



class QuantumCircuit(object):
    pass



    def from_qasm_file(path):
        pass


    def from_qasm_str(qasm_str):
        pass


    def __init__(self, *regs, name=None):
        pass








    def _increment_instances(cls):
        pass

    def cls_instances(cls):
        pass

    def cls_prefix(cls):
        pass

    def has_register(self, register):
        pass



    def combine(self, rhs):
        pass




    def extend(self, rhs):
        pass





    def __add__(self, rhs):
        pass

    def __iadd__(self, rhs):
        pass

    def __len__(self):
        pass

    def __getitem__(self, item):
        pass

    def _attach(self, instruction):
        pass

    def add(self, *regs):
        pass

    def _check_qreg(self, register):
        pass

    def _check_qubit(self, qubit):
        pass

    def _check_creg(self, register):
        pass

    def _check_dups(self, qubits):
        pass

    def _check_compatible_regs(self, rhs):
        pass

    def _gate_string(self, name):
        pass

    def qasm(self):
        pass

    def draw(self, scale=0.7, filename=None, style=None, output='text',
        pass





    def __str__(self):
        pass
