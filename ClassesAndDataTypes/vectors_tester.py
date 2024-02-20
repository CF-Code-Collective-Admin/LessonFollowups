# Describe test case

import MODULE as test_module

cases = [
    [(5, 7, 4), (2, 4, 8), [(7, 11, 12), (3, 3, -4), 70, (40, -32, 6)]],
    [(12, 18, 41), (123, 1, 5), [(135, 19, 46), (-111, 17, 36), 1699, (49, 4983, -2202)]],
    [(74, 19, 73), (19, 94, 75), [(93, 113, 148), (55, -75, -2), 8667, (-5437, -4163, 6595)]],
    [(13, 9, 5), (6, 15, 8), [(19, 24, 13), (7, -6, -3), 253, (-3, -74, 141)]],
]

test_module.run()

def test(case):
    vector_a = test_module.vector3(*case[0])
    vector_b = test_module.vector3(*case[1])
    
    add = vector_a.add(vector_b)
    sub = vector_a.subtract(vector_b)
    dot = int(vector_a.dot(vector_b))
    cross = vector_a.cross(vector_b)
    
    if str(add) != str(case[2][0]):
        return False
    if str(sub) != str(case[2][1]):
        return False
    if str(dot) != str(case[2][2]):
        return False
    if str(cross) != str(case[2][3]):
        return False
    return True

for case in cases:
    assert test(test_module.run(case))

print("OK")
