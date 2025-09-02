import random
import time

def test_intentionally_flaky():
    r = random.random()
    # ~30% chance to simulate a race/timeout-like flake
    if r < 0.3:
        time.sleep(0.01)
        assert False, "Random flake happened"
    else:
        assert True
