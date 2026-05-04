def test_chained_circuit_not_and():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_gate("g1", GateType.AND, inputs=["A", "B"])
    c.add_gate("g2", GateType.NOT, inputs=["g1"])
    result = c.evaluate({"A": True, "B": True})
    assert result["g2"] == False

def test_complex_chain():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_input("C")
    c.add_gate("g1", GateType.AND, inputs=["A", "B"])
    c.add_gate("g2", GateType.OR,  inputs=["g1", "C"])
    result = c.evaluate({"A": True, "B": True, "C": False})
    assert result["g2"] == True
