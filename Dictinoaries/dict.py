dt = {'key': 'val', 'key1': 'val2'}
# print(dt['key'])

dt1 = {"A": 65, "B": 66}
dt2 = {"C": 55, "D": 88}
print(dt1.keys())
print(dt1.values())

Dt = {"1": dt1, "2": dt2}
print(Dt)

## Dictionary Methods

tpl1 = ('k1', 'k2', 'k3')
# val = (4)
# dt = dict.fromkeys(tpl1,val)

dt = dict.fromkeys(tpl1)
dt['k1'] = 19
dt['k2'] = 19
dt['k3'] = 19

dt.update({'k4': 17})

dt.clear()
print(dt)