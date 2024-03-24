import os
from cryptography.fernet import Fernet

key = "Decryption key here"
f = Fernet(key)
fpath = ""
file = ""

with open(fpath, "rb") as of:
    original: bytes = of.read()

    encrypted = f.encrypt(original)

with open(fpath, "wb") as of:
    of.write(encrypted)

filename = f.encrypt(file.encode())
newpath: str = filename.decode()