# Given a name, should return the debt

import registry as test_module

cases = [
    ["Emanuel", "123"],
    ["Colt", "526"],
    ["Gavin", "2784"],
    ["Layla", "235"],
    ["Kianna", "98765"],
    ["Jaydan", "236"],
    ["Shaniya", "7934"],
    ["Amanda", "427"],
    ["Joseph", "247"],
    ["Jazlyn", "2945"],
    ["Luke", "23880"],
    ["Blaine", "5"]
]

for case in cases:
    assert str(test_module.run(case[0])) == case[1]

print("OK")
