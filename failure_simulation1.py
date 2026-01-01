import random
import numpy as np

class Component:
    def __init__(self, name, failure_prob):
        self.name = name
        self.failure_prob = failure_prob
        self.failed = False

    def check_failure(self):
        self.failed = random.random() < self.failure_prob
        return self.failed

def simulate_system(components, runs=1000):
    failures = 0
    for _ in range(runs):
        if any(c.check_failure() for c in components):
            failures += 1
    return failures / runs

if __name__ == "__main__":
    components = [
        Component("Transformer", 0.05),
        Component("Feeder", 0.03),
        Component("Switchgear", 0.02)
    ]

    failure_rate = simulate_system(components)
    print(f"Estimated system failure rate: {failure_rate:.2%}")
