from itertools import takewhile


with open('01/input.txt') as f:
    lines = map(lambda x: x.rstrip(), f.readlines())

def process(l) -> list:
    while(True):
        if not (a := sum(map(int, takewhile(lambda x: len(x), lines)))):
            break
        yield a

print(sum(sorted(process(lines), reverse=True)[:3]))