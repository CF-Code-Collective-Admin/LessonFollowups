# Returns the length of the input string

import stringlength as test_module

cases = [
    ["12345", "5"],
    ["1234567890", "10"],
    ["1234567", "7"],
    ["123456789012345678901234567890", "30"],
    ["Hello, world!", "13"]
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
