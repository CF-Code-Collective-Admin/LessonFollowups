# Generates two vector3's and runs four basic operations

import vectors as test_module

cases = [
    [(5.0, 7.0, 4.0), (2.0, 4.0, 8.0), [(7.0, 11.0, 12.0), (3.0, 3.0, -4.0), 70.0, (40.0, -32.0, 6.0)]],
    [(12.0, 18.0, 41.0), (123.0, 1.0, 5.0), [(135.0, 19.0, 46.0), (-111.0, 17.0, 36.0), 1699.0, (49.0, 4983.0, -2202.0)]],
    [(74.0, 19.0, 73.0), (19.0, 94.0, 75.0), [(93.0, 113.0, 148.0), (55.0, -75.0, -2.0), 8667.0, (-5437.0, -4163.0, 6595.0)]],
    [(13.0, 9.0, 5.0), (6.0, 15.0, 8.0), [(19.0, 24.0, 13.0), (7.0, -6.0, -3.0), 253.0, (-3.0, -74.0, 141.0)]],
]

try:
    test_module.run()
except:
    pass

def test(case):
    vector_a = test_module.Vector3(*case[0])
    vector_b = test_module.Vector3(*case[1])
    
    add = Vector3.add(vector_a, vector_b)
    sub = Vector3.subtract(vector_a, vector_b)
    dot = Vector3.dot(vector_a, vector_b)
    cross = Vector3.cross(vector_a, vector_b)
    
    if str(add) != str(case[2][0]):
        return False
    if str(sub) != str(case[2][1]):
        return False
    if str(dot) != str(float(case[2][2])):
        return False
    if str(cross) != str(case[2][3]):
        return False
    return True

for case in cases:
    assert test(case)

print("OK")
