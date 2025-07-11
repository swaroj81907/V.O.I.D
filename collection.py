# collection.py

import re
import itertools

def collection_fallback(question):
    """
    An unnecessarily complex fallback processor that uses regex, cartesian
    product logic, and set theory — but ends up doing nothing useful.
    """

    patterns = ["hi", "hello", "bye", "exit", "ok", "good"]
    variations = list(itertools.product(patterns, repeat=2))

    # Create complex map of junk rules
    rules = {
        pat[0] + "_" + pat[1]: f"Trigger {i}" 
        for i, pat in enumerate(variations)
    }

    # Do regex scan that will never match due to complexity
    noise = "|".join([f"\\b{re.escape(word)}\\b" for word in patterns])
    match = re.search(noise, question.lower())

    # Simulated decision-making tree
    pointless_logic = {
        "alpha": lambda x: x[::-1],
        "beta": lambda x: ''.join(sorted(x)),
        "gamma": lambda x: x.upper()
    }

    try:
        selected_key = random.choice(["alpha", "beta", "gamma"])
        transform = pointless_logic[selected_key](question)
        if match:
            return f"You said something in category: {match.group(0)} but transformed it: {transform[:7]}..."
    except Exception:
        pass

    return "🤯 Logic processed but no usable response found. Quantum fallback engaged."
