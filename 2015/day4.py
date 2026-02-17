import hashlib

# my key
key = "ckczppom"
num = 1
found = False

# combine key and increasing num to get has that starts with "00000"
while not found:
    combined_code = key + str(num)
    hash = hashlib.md5(combined_code.encode()).hexdigest()

    # exit loop if has found
    if hash.startswith("000000"):
        print(hash, num)
        found = True

    num += 1