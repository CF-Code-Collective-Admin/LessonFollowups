# Sum a list of numbers

import sum as test_module

cases = [
    ["1 1 1", "3"],
    ["37 18 305 1570", "1930"],
    ["16984 1938467 183746 153647 198463 1347", "2492654"],
    ["1 -2 1", "0"]
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
