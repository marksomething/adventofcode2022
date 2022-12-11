from itertools import takewhile
from typing import Iterable, List
from pathlib import Path


def process(clean_lines: List[str]) -> Iterable[int]:
    while a := sum(map(int, takewhile(lambda x: len(x), clean_lines))):
        yield a


elf_loads = sorted(
    process(map(lambda x: x.rstrip(), Path("01/input.txt").read_text().splitlines())),
    reverse=True,
)

print(f"Max: {elf_loads[0]}")
print(f"Max3: {sum(elf_loads[:3])}")
