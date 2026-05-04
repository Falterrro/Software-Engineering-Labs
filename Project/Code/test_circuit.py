def test_not_gate_flips():
    g = Gate(GateType.NOT)
    assert g.evaluate([True]) == False
    assert g.evaluate([False]) == True

def test_xor_gate():
    g = Gate(GateType.XOR)
    assert g.evaluate([True, False]) == True
    assert g.evaluate([True, True]) == False