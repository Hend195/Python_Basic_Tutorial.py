"""
list_vs_tuple_demo.py
--------------------
A simple Python project to demonstrate the differences between lists and tuples.

Idea:
- Define a list and a tuple with the same initial values.
- Try to apply various list-specific methods to both structures.
- Use try/except to catch errors that occur with tuples, so the program doesn't crash.
- Print out results for each operation.

How to run:
python list_vs_tuple_demo.py
"""

def run_demo():
    # Initial values
    original_list = [1, 2, 3]
    original_tuple = (1, 2, 3)

    # Mutating operations (name, function)
    mutating_ops = [
        ("append", lambda seq: seq.append(99)),
        ("extend", lambda seq: seq.extend([4, 5])),
        ("insert", lambda seq: seq.insert(1, "inserted")),
        ("remove", lambda seq: seq.remove(seq[0])),
        ("pop", lambda seq: seq.pop()),
        ("clear", lambda seq: seq.clear()),
        ("sort", lambda seq: seq.sort()),
        ("reverse", lambda seq: seq.reverse()),
        ("copy", lambda seq: seq.copy()),
    ]

    # Safe operations for both list and tuple
    safe_ops = [
        ("count(2)", lambda seq: seq.count(2)),
        ("index(3)", lambda seq: seq.index(3)),
        ("len()", lambda seq: len(seq)),
    ]

    print("====== List vs Tuple Comparison ======")

    # Try mutating operations
    for op_name, op_func in mutating_ops:
        print(f"\n--- Testing operation: {op_name} ---")
        lst = original_list.copy()  # Create a fresh list copy
        tpl = original_tuple        # Tuples are immutable, no need to copy

        # On list
        try:
            result = op_func(lst)
            if result is not None:
                print(f"List result    -> {result}")
            print(f"List after op  -> {lst}")
        except Exception as e:
            print(f"List error     -> {e.__class__.__name__}: {e}")

        # On tuple
        try:
            result = op_func(tpl)
            if result is not None:
                print(f"Tuple result   -> {result}")
            print(f"Tuple after op -> {tpl}")
        except Exception as e:
            print(f"Tuple error    -> {e.__class__.__name__}: {e}")

    # Try safe operations
    for op_name, op_func in safe_ops:
        print(f"\n--- Testing safe operation: {op_name} ---")
        print(f"List {op_name}  -> {op_func(original_list)}")
        print(f"Tuple {op_name} -> {op_func(original_tuple)}")

if __name__ == "__main__":
    run_demo()
