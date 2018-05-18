ages = {}
ages['bob'] = 9
ages['alice'] = 18


ages['bob']              # 9
ages.bob                 # error: 'dict' object has no attribute 'bob'
ages.get('bob')          # 9
ages['john']             # KeyError: 'john'
ages.get('john')         # None
ages.get('john', 'N/A')  # 'N/A'
len(ages)                # 2
list(ages)               # ['bob', 'alice'], order may differ
'bob' in ages            # True
'john' in ages           # False

ages = { 'bob': 9, 'alice': 18 }
ages2 = dict({'bob': 9, 'alice': 18}) # same as ages
ages3 = dict(bob=9, alice=18)          # same as ages
ages4 = dict([('bob', 9), (alice, 18)]) # same as ages