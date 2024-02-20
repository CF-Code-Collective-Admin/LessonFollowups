# Describe test case

import MODULE as test_module

def test(inp):
    inp = set(inp)
    if len(inp) != 50:
        return False
    for i in inp:
        if i < 1 or i > 1000:
            return False
    return True

assert test(test_module.run())

print("OK")
