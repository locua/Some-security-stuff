import random
alphabet = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

plainText = "helloitsmeadelehowareyou"

listPlain = list(plainText)

plainI = [None] * len(plainText)
randoms = [None] * len(plainText)
cipher = [None] * len(plainText)

# change letters into letter index
for i in range(0, len(plainI)):
    for j in range(0, len(alphabet)):
        if listPlain[i] == alphabet[j]:
            plainI[i] = j

print(plainText)
print(plainI)

cipherMessage = ""
for i in range (0, len(plainText)):
    randoms[i] = random.randint(0, 99999999)
    iPlusR = plainI[i] + randoms[i]
    cipher[i] = iPlusR%26

print(randoms)
print(cipher)
cipher_and_key = (cipher, randoms)

cipherText = "pcnsvhqkxf"
key = [216, 50, 262, 267, 293, 22, 2, 250, 223, 13]
listCipher = list(cipherText)

indexes = [None] * len(cipherText)
for i in range(0, len(listCipher)):
    for j in range(0, len(alphabet)):
        if listCipher[i] == alphabet[j]:
            indexes[i] = j

decrypted = [None] * len(randoms)
message = ""

for i in range(0, len(key)):
    iMinusR = cipher[i] - randoms[i]
    decrypted[i] = iMinusR%26
    if decrypted[i] < 0:
        decrypted[i] += 26
    message += alphabet[decrypted[i]]

print(message)
