# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
from string import ascii_uppercase
import operator


cypher_text = open("applications\crack_caesar\ciphertext.txt","r")

text = cypher_text.read()

f = open('applications\crack_caesar\decoded.txt', 'w+')

# print(text)



new_text = ''

for x in ascii_uppercase: ## This for loop creates a new string without spaces, gotta have that precision!!
    for y in text:
        if x == y:
            new_text += x


def letter_count(text):
    count = 0
    for x in text:
        count += 1
    return count

list_text = list(set(new_text))

letters = {}

for x in ascii_uppercase:
    letters[x] = round((new_text.count(x)/letter_count(new_text))*100,2)

frequency = {
    "A": 8.46,
    "B": 2.19,
    "C": 1.58,
    "D": 4.74,
    "E": 11.53,
    "F": 2.42,
    "G": 2.48,
    "H": 7.71,
    "I": 5.84,
    "J": 0.07,
    "K": 0.84,
    "L": 3.92,
    "M": 2.18,
    "N": 6.73,
    "O": 8.08,
    "P": 1.08,
    "Q": 0.17,
    "R": 6.29,
    "S": 5.56,
    "T": 9.75,
    "U": 2.59,
    "V": 0.59,
    "W": 3.08,
    "X": 0.07,
    "Y": 2.02,
    "Z": 0.03,
}

cypher = {}
for x in frequency:
    for y in letters:
        if frequency[x] == letters[y]:
            cypher[x] = y

new_text = ''
for x in text:
    new_text += x

doc = ''

for x in range(len(new_text)):
    for y in cypher:
        if new_text[x] == y:
            doc += cypher[y]




def decode(text, cypher):
    r = ""
    for c in text:
        if c not in cypher:
            r += " "
        else:
            r += cypher[c]
    return r

def decoder(value, text , cypher):
    num = 0
    r = text
    while num < value:
        r = decode(r,cypher)
        num += 1
    return r

first = decode(text,cypher)
second = decode(first, cypher)
third = decode(second,cypher)
print(cypher)

print(f"Decoded text:\n {decoder(10,text,cypher)}")


       



    

