from circuit import Gate, GateType

def test_and_gate_evaluates_correctly():
    g = Gate(GateType.AND)
    assert g.evaluate([True, True]) == True
    assert g.evaluate([True, False]) == False
    assert g.evaluate([False, False]) == False