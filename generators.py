import random
import string
from decorator import timed

@timed
def generate_numbers(n) -> list[int]:
    return [random.randint(0, 99999999) for _ in range(n)]

@timed
def generate_dlids(n) -> list[str]:
    ints = [random.randint(0, 999999) for _ in range(n)]
    ret: list[str] = []
    for x in ints:
        ret.append(f"{''.join(random.choices(string.ascii_letters, k=2)).upper()}{str(x).ljust(6, '0')}")
    return ret