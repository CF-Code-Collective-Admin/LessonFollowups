# Describe test case

import MODULE as test_module

cases = [
    []
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
