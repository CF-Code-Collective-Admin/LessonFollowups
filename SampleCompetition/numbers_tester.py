# Returns True if the input string contains a number

import numbers as test_module

cases = [
    ["akfbiwbfqbfiqwfqbf", "False"],
    ["This is my friend Greg", "False"],
    ["fowhfhwfoqhfow2140140917401470", "True"],
    ["2414987924719472947984719", "True"],
    ["fjaofjfoajfajofjaofja aofjaofjoafj 1 jfoafjaof", "True"],
    ["This is a cool one", "False"]
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
