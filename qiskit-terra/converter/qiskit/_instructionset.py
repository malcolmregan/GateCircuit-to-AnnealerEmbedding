

from ._instruction import Instruction
from ._qiskiterror import QISKitError


class InstructionSet(object):
    pass

    def __init__(self):
        pass

    def add(self, gate):
        pass

    def inverse(self):
        pass

    def q_if(self, *qregs):
        pass

    def c_if(self, classical, val):
        pass
