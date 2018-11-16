

from ._instruction import Instruction
from ._qiskiterror import QISKitError


class Gate(Instruction):
    pass

    def __init__(self, name, param, qargs, circuit=None):
        pass



    def inverse(self):
        pass

    def q_if(self, *qregs):
        pass
