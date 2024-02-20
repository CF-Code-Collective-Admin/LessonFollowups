# Creates a car() instance and tests it

import cars as test_module

cases = [
    [2014, "Kia", "Sportage"],
    [2001, "Mercury", "Mountaineer"],
    [2017, "Honda", "Civic"],
    [1973, "Ford", "F150"],
    [2024, "Nissan", "Rogue"]
]

test_module.run()

def test(year, make, model):
    car = test_module.car(year, make, model)
    a, b, c = car.info()
    if a == year and b == make and c == model:
        return True
    return False

for case in cases:
    assert test(*case)

print("OK")
