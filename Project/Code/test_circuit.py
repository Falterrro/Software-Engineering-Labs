from circuit import Circuit

def test_circuit_add_gate_and_input():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_gate("g1", GateType.AND, inputs=["A", "B"])
    assert "g1" in c.gates
    asser "g2" in c.inputs