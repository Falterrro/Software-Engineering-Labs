from enum import Enum

class GateType(Enum):
    AND = "AND"
    OR  = "OR"
    NOT = "NOT"
    NAND = "NAND"
    NOR  = "NOR"
    XOR  = "XOR"

GATE_FUNCTIONS = {
    GateType.AND:  lambda inputs: all(inputs),
    GateType.OR:   lambda inputs: any(inputs),
    GateType.NOT:  lambda inputs: not inputs[0],
    GateType.NAND: lambda inputs: not all(inputs),
    GateType.NOR:  lambda inputs: not any(inputs),
    GateType.XOR:  lambda inputs: inputs[0] ^ inputs[1],
}

class Gate:
    def __init__(self, gate_type: GateType):
        self.gate_type = gate_type

    def evaluate(self, inputs: list[bool]) -> bool:
        return GATE_FUNCTIONS[self.gate_type](inputs)

class Circuit:
    def __init__(self):
        self.inputs = {}       
        self.gates = {}        
        self.wiring = {}

    def add_input(self, name: str):
        self.inputs[name] = False

    def add_gate(self, name: str, gate_type: GateType, inputs: list[str]):
        self.gates[name] = Gate(gate_type)
        self.wiring[name] = inputs