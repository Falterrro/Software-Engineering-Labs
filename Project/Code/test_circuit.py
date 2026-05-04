# test_circuit.py — Student B adds:
def test_cycle_detection():
    c = Circuit()
    c.add_input("A")
    c.add_gate("g1", GateType.NOT, inputs=["g2"])
    c.add_gate("g2", GateType.NOT, inputs=["g1"])
    with pytest.raises(ValueError, match="Cycle"):
        c.evaluate({"A": True})

def test_truth_table_has_correct_rows():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_gate("g1", GateType.AND, inputs=["A", "B"])
    table = c.truth_table()
    assert len(table) == 4 