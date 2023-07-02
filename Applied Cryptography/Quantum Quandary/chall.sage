from secrets import priv_key
from random import randint

with open('flag.txt') as f:
    FLAG = f.read()

F_bin = [bin(ord(char))[2:].zfill(8) for char in FLAG]

assert len(priv_key) == 8

q = randint(sum(priv_key)+1,sum(priv_key)*5)
while True:
    r = randint(2,priv_key[-1]-1)
    if gcd(r,q) == 1:
        break

pub_key = [(elem*r)%q for elem in priv_key]
print(f"pub_key = {pub_key}")

ct = []
for c in F_bin:
    sum = 0
    for pos, bit in enumerate(c):
        sum += pub_key[pos] * int(bit)
    ct.append(sum)

print(f"ct = {ct}")