def test_circuit_evaluates_simple():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_gate("g1", GateType.AND, inputs=["A", "B"])
    result = c.evaluate({"A": True, "B": False})
    assert result["g1"] == False