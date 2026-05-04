import json

def test_save_and_load_circuit():
    c = Circuit()
    c.add_input("A")
    c.add_input("B")
    c.add_gate("g1", GateType.OR, inputs=["A", "B"])
    data = json.dumps(c.to_dict())
    c2 = Circuit.from_dict(json.loads(data))
    result = c2.evaluate({"A": False, "B": True})
    assert result["g1"] == True