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

    def evaluate(self, input_values: dict) -> dict:
        cache = dict(input_values)
        for name in self._topological_order():
            resolved = [cache[i] for i in self.wiring[name]]
            cache[name] = self.gates[name].evaluate(resolved)
        return cache

    def _topological_order(self) -> list[str]:
        visited, in_stack, order = set(), set(), []
        def visit(name):
            if name in self.inputs:
                return
            if name in in_stack:
                raise ValueError(f"Cycle detected at gate '{name}'")
            if name in visited:
                return
            in_stack.add(name)
            for dep in self.wiring.get(name, []):
                visit(dep)
            in_stack.discard(name)
            visited.add(name)
            order.append(name)
        for name in self.gates:
            visit(name)
        return order

    def truth_table(self) -> list[dict]:
        import itertools
        keys = list(self.inputs.keys())
        rows = []
        for combo in itertools.product([False, True], repeat=len(keys)):
            input_vals = dict(zip(keys, combo))
            result = self.evaluate(input_vals)
            rows.append(result)
        return rows