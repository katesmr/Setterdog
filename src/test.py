from src.DictObj import DictObj
import sys

js = {'s': 45, 'p': 77, 'd': {}}
js = DictObj(js)
print(js.s)
js.d.f = 9
js.g = 'g'
print(js)


d1 = {'s': 5, 'r': 4, 'k': 9}
d2 = {'s': 2, 'r': 0}
d = {**d1, **d2}
print(d)
d3 = {'s': 6, 'j': 66, 'r': 4, 'i': 222}
d = {**d, **d3}
print(d)

print(max([]))
