# Tests the four mathematical operators

import mathops as test_module

cases = [
    ["537 + 264", "801"],
    ["5278 + 1469", "6747"],
    ["396 - 195", "201"],
    ["2497 - 8265", "-5768"],
    ["385 * 105", "40425"],
    ["8562 * 1356", "11610072"],
    ["512 / 16", "32"],
    ["100016 / 658", "152"]
]

for case in cases:
    assert str(int(test_module.run(case[0]))) == case[1]

print("OK")
