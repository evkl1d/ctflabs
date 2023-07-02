import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


flag = b"sikorsky{***}"


def encrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    return cipher.encrypt(data)


def generate(ch, index, l):
    random.seed(ch)
    result = [bytes([random.randint(0, 255)]) for _ in range(l)]
    result[index] = bytes([ch])
    return result


key = get_random_bytes(16)
iv = get_random_bytes(16)

pt = []
for i in range(len(flag)):
    pt.append(generate(flag[i], i, len(flag)))

ct = []
for i in pt:
    ct.append(encrypt(b"".join(i), key, iv))

print(ct)
