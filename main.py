import random
import qrcode
import hashlib, binascii, sys

nums = {}
wordlist = []
with open('english.txt') as fin:
    i = 0
    for word in fin:
        nums[word.strip()] = i
        wordlist.append(word.strip())
        i += 1

def isOk(ws):
    N = 0
    for w in ws:
        N = (N<<11) + nums[w]

    nhex = format(N, '033x') # include leading zero if needed

    h = hashlib.sha256(binascii.unhexlify(nhex[:-1])).hexdigest()

    return h[0] == nhex[-1]


# wordslist = list(filter(lambda w: w != '', open('./english.txt','r').read().split('\n')))

while True:
    passphrasel = [random.choice(wordlist) for i in range(12)]
    if isOk(passphrasel):
        print(' '.join(passphrasel))
        img = qrcode.make(' '.join(passphrasel))
        img.save('pass.png')
        break