import math
import random
import paillier
import hashlib

# A 3D array used to store the votes of a user
userVotes = [[[[0, 0, 0]] * 4] * 5][0]
encryptedVotes = []

# fetch public key from the paillier.py script
publicKey = paillier.public_key

# get n and g values from the public Key
n, g = publicKey.n, publicKey.g
r = random.randint(0, n)


# function to compute gcd
def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1%n2)


# function to generate coprimes of a number
def generateCoPrimes(num):
    coprimes = []
    for i in range(2, num):
        if gcd(i, num) == 1:
            coprimes.append(i)
    return coprimes


# function to fetch a co-prime number randomly from a list of co-primes
def randomCoPrime(coprimes):
    return random.choice(coprimes)


def ejList(coprimes):
    c_temp = coprimes
    ejl = []
    for i in range(4):
        x = random.choice(c_temp)
        c_temp.pop(c_temp.index(x))
        ejl.append(x)
    return ejl


def vjlist(coprimes):
    c_temp = coprimes
    vjl = []
    for i in range(4):
        x = random.choice(c_temp)
        c_temp.pop(c_temp.index(x))
        vjl.append(x)
    return vjl


# function to fill the userVotes array randomly with 1 once per question per user
def fillArray():
    for i in range(5):
        for j in range(4):
            randomNum = random.randint(0, 2)  # Generate a random number between 0 and 2
            userVotes[i][j][randomNum] = 1


# generates a list of encrypted votes using the public key generated using the Paillier Crypto-system
def encryptQuestion():
    b = math.ceil(math.log2(5))
    qSum = []
    for i in range(5):
        questionsSum = 0
        for j in range(4):
            optionsSum = 0
            for k in range(3):
                optionsSum += userVotes[i][j][k] * (2 ** (k * b))  # b * Options

            questionsSum += optionsSum * (2 ** (j * b * 3))  # b * L * Questions
        qSum.append(questionsSum)
        encryptedVotes.append(publicKey.encrypt(questionsSum))

    # .ciphertext()
    return encryptedVotes, qSum


def calculate_UI(w):
    return (w**n) % n


def ujList(ej, vj, encVotes, qSum):
    ujl = []
    for i in range(5):
        v1 = vj[i] ** n
        v2 = g ** qSum[i]
        v3 = (v2//encVotes[i]) ** ej[i]
        v4 = (v1 * v3) % (n ** 2)
        ujl.append(v4)
    return ujl


# function to perform SHA356 hashing on a given string
def hashing(uj, encVotes, qSum):
    ujs = "".join(uj)
    encvs = "".join(encVotes)
    qSums = "".join(qSum)
    gn = str(g)+str(n)
    return hashlib.sha256(ujs+encvs+gn+qSums).hexdigest()


def calculate_EI(e, ej):
    eiList = []
    for i in range(4):
        sumn = 0
        for j in range(4):
            sumn += (ej[j] % n) if i != j else 0
        ei = e - sumn
        eiList.append(ei)

    return eiList


def calculate_VI(w, ei):
    viList = []
    for i in range(len(ei)):
        viList.append(w * (r**ei[i]) % n)
    return viList


if __name__ == '__main__':
    fillArray()
    encryptedVotes, qSum = encryptQuestion()
    coprimes = generateCoPrimes(n)
    w = randomCoPrime(coprimes)
    ej = ejList(coprimes)
    vj = vjlist(coprimes)
    ui = calculate_UI(w)
    uj = ujList(ej, vj, encryptedVotes, qSum)
    e = hashing(uj, encryptedVotes, qSum)
    ei = calculate_EI(int(e), ej)
    vi = calculate_VI(e, ei)
