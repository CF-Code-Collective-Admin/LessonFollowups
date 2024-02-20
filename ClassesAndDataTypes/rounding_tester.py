# Rounds a number to the nearest int

import rounding as test_module

cases = [
    [124.47, "124"],
    [0.295, "0"],
    [124.6127, "125"],
    [125.7274, "126"],
    [96.2689, "96"],
    [35.499, "35"],
    [9.995, "10"],
    [3.5, "4"],
    [246.51, "247"],
    [205.0001, "205"],
    [424.53, "425"],
    [394.4, "394"],
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
