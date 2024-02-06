# Returns True if the input is "Hello, world!"

import helloworld as test_module

cases = [
    ["Hello, world!", "True"],
    ["Not hello world!", "False"],
    ["Hello, world!", "True"],
    ["Hello, Steve!", "False"]
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
