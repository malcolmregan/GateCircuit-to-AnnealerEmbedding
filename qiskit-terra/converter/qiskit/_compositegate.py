

from ._gate import Gate
from ._qiskiterror import QISKitError


class CompositeGate(Gate):
    pass

    def __init__(self, name, param, qargs, circuit=None, inverse_name=None):
        pass


    def instruction_list(self):
        pass


    def has_register(self, register):
        pass

    def _modifiers(self, gate):
        pass

    def _attach(self, gate):
        pass

    def _check_qubit(self, qubit):
        pass

    def _check_qreg(self, register):
        pass


    def _check_creg(self, register):
        pass


    def _check_dups(self, qubits):
        pass


    def qasm(self):
        pass

    def inverse(self):
        pass

    def reapply(self, circ):
        pass

    def q_if(self, *qregs):
        pass

    def c_if(self, classical, val):
        pass
