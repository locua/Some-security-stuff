import random

alphabet = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
alphabetlen = len(alphabet)

message = "hello alex you big gay"

def createkey(length):
    out = []
    for i in range(0, length):
        digit = random.randint(0, 9999999999)
        out.append(digit)
        #print(digit)
    return out

def letter_index(letter):
    for i in range(0, len(alphabet)):
        if letter == alphabet[i]:
            return i

def indexes_2_string(indexes):
    out = ""
    for i in indexes:
        for j in range(0, len(alphabet)):
            if i == j:
                out += alphabet[j]
    return out


def split(word):
    return [char for char in word]

key = createkey(26)

def encrypt(plaintext):
    plaintextsplit = split(plaintext)
    key = createkey(len(plaintextsplit))
    message_indexes = []
    for l in plaintextsplit:
        message_indexes.append(letter_index(l))

    iplusr = [x + y for x, y in zip(message_indexes, key)]
    out = [x % alphabetlen for x in iplusr]
    out = indexes_2_string(out)
    return (out, key)

def decrypt(ciphertext, key):
    ciphertext = split(ciphertext)
    cipher_indexes = []
    for l in ciphertext:
        cipher_indexes.append(letter_index(l))

    iminusr = [x - y for x, y in zip(cipher_indexes, key)]
    out = [x % alphabetlen for x in iminusr]
    out = indexes_2_string(out)
    print(out)

out_key = encrypt(message)
print(out_key)
decrypt(out_key[0], out_key[1])






