# main.py
import json
from circuit import Circuit, GateType

HELP = """
Commands:
  input <name>                     Add a named input (e.g. input A)
  gate <name> <TYPE> <i1> <i2...>  Add a gate (e.g. gate g1 AND A B)
  eval <name>=<0|1> ...            Evaluate (e.g. eval A=1 B=0)
  table                            Print full truth table
  show                             Show current circuit
  save <file>                      Save circuit to JSON file
  load <file>                      Load circuit from JSON file
  reset                            Clear the circuit
  help                             Show this message
  quit                             Exit
"""

def parse_inputs(args):
    result = {}
    for token in args:
        k, v = token.split("=")
        result[k.strip()] = v.strip() in ("1", "true", "True")
    return result

def main():
    circuit = Circuit()
    print("Logic Circuit Simulator")
    print(HELP)

    while True:
        try:
            line = input("circuit> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()

        if cmd == "quit":
            print("Bye!")
            break

        elif cmd == "help":
            print(HELP)

        elif cmd == "reset":
            circuit = Circuit()
            print("Circuit cleared.")

        elif cmd == "input":
            if len(parts) < 2:
                print("Usage: input <name>"); continue
            circuit.add_input(parts[1])
            print(f"  Added input '{parts[1]}'")

        elif cmd == "gate":
            if len(parts) < 4:
                print("Usage: gate <name> <TYPE> <input1> [input2]"); continue
            name, gtype_str, *inputs = parts[1], parts[2], parts[3:]
            try:
                gtype = GateType(parts[2].upper())
                circuit.add_gate(parts[1], gtype, parts[3:])
                print(f"  Added {gtype.value} gate '{parts[1]}' ← {parts[3:]}")
            except ValueError:
                print(f"  Unknown gate type '{parts[2]}'. Options: AND OR NOT NAND NOR XOR")

        elif cmd == "eval":
            try:
                vals = parse_inputs(parts[1:])
                result = circuit.evaluate(vals)
                print("\n  Results:")
                for k, v in result.items():
                    tag = "INPUT" if k in circuit.inputs else "GATE "
                    print(f"    [{tag}] {k} = {int(v)}")
            except Exception as e:
                print(f"  Error: {e}")

        elif cmd == "table":
            try:
                keys = list(circuit.inputs.keys())
                gate_names = list(circuit.gates.keys())
                header = " | ".join(keys + gate_names)
                print("\n  " + header)
                print("  " + "-" * len(header))
                for row in circuit.truth_table():
                    values = [str(int(row[k])) for k in keys + gate_names]
                    print("  " + " | ".join(values))
                print()
            except Exception as e:
                print(f"  Error: {e}")

        elif cmd == "show":
            print(f"\n  Inputs: {list(circuit.inputs.keys())}")
            for name, gate in circuit.gates.items():
                print(f"  Gate '{name}': {gate.gate_type.value} ← {circuit.wiring[name]}")
            print()

        elif cmd == "save":
            if len(parts) < 2:
                print("Usage: save <file>"); continue
            with open(parts[1], "w") as f:
                json.dump(circuit.to_dict(), f, indent=2)
            print(f"  Saved to '{parts[1]}'")

        elif cmd == "load":
            if len(parts) < 2:
                print("Usage: load <file>"); continue
            try:
                with open(parts[1]) as f:
                    circuit = Circuit.from_dict(json.load(f))
                print(f"  Loaded from '{parts[1]}'")
            except Exception as e:
                print(f"  Error loading: {e}")

        else:
            print(f"  Unknown command '{cmd}'. Type 'help' for options.")

if __name__ == "__main__":
    main()