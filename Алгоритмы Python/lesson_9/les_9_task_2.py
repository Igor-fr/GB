# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import namedtuple
from collections import Counter

class Node(namedtuple("Node", ["left", "right"])):
    def find_code(self, code, str):
        self.left.find_code(code, str + "0")
        self.right.find_code(code, str + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def find_code(self, code, str):
        code[self.char] = str or "0"

s = "beep boop beer!"

counter = Counter(s)
deq = []

for item in counter.most_common():
    deq.append((Leaf(item[0]), item[1]))

print(deq)

deq.sort(key=lambda x: x[1], reverse=True)

while len(deq) > 1:
    el1 = deq.pop()
    el2 = deq.pop()
    deq.append((Node(el1[0], el2[0]), el1[1] + el2[1]))
    deq.sort(key=lambda x: x[1], reverse=True)

code = {}
if deq:
    deq[0][0].find_code(code, "")

encoded = " ".join(code[ch] for ch in s)

print(s)
print(code)
print(encoded)