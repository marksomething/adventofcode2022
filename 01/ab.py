from itertools import takewhile
from typing import Iterable


def process(l) -> Iterable[int]:
    while a := sum(map(int, takewhile(lambda x: len(x), lines))):
        yield a


with open("01/input.txt") as f:
    lines = map(lambda x: x.rstrip(), f.readlines())

top3 = sorted(process(lines), reverse=True)[:3]
print(f"Max: {top3[0]}")
print(f"Max3: {sum(top3)}")
