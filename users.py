import random
import paillier
import hashlib
import zka

# A 3D array used to store the votes of a user
# userVotes = [[[[0, 0, 0]] * 4] * 7][0]
encryptedVotes = []

# fetch public key from the paillier.py script
publicKey = paillier.public_key
uj = []
c = []

# get n and g values from the public Key
number_of_users = 10
n, g = 5, 3
r = 1

random_list = []
piAuthList = []
for i in range(number_of_users):
    random_list.append(random.randint(1, 5))
    piAuthList.append(zka.submit_vote(i))

message = random.sample(random_list, 1)[0]
message_index = random_list.index(message)


# function to compute gcd
def gcd(n1, n2):
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)


def isPrime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


# function to generate coprimes of a number
def generateCoPrimes(num):
    coprimes = []
    for i in range(2, num):
        if isPrime(i) and gcd(i, num) == 1:
            coprimes.append(i)
    return coprimes


coprimes_n = generateCoPrimes(n)


def sampleValues():
    w = random.sample(coprimes_n, 1)[0]
    l = len(random_list)
    ej, vj = [], []
    for j in range(l):
        if j == message_index:
            continue
        ej.append(random.sample(coprimes_n, 1)[0])
        vj.append(random.sample(coprimes_n, 1)[0])
    return w, ej, vj


def compute_C():
    for i in range(len(random_list)):
        c.append(((g ** random_list[i]) * (r ** n)) % (n ** 2))
    return c


def compute_U(w, ej, vj):
    for j in range(len(random_list)):
        if j == message_index:
            uj.append((w ** n) % (n ** 2))
        elif j > message_index:
            value = ((vj[j - 1] ** n) * (((g ** random_list[j - 1]) // (c[j - 1])) ** ej[j - 1])) % (n ** 2)
            uj.append(value)
        else:
            value = ((vj[j] ** n) * (((g ** random_list[j]) // (c[j])) ** ej[j])) % (n ** 2)
            uj.append(value)
    return uj


def compute_E():
    uj_string = "".join(str(i) for i in uj)
    c_string = "".join(str(i) for i in c)
    gs, ns = str(g), str(n)
    rl_string = "".join(str(i) for i in random_list)
    s = uj_string + c_string + gs + ns + rl_string
    return s, hashlib.sha256(s.encode('utf-8')).hexdigest()


def compute_EI_VI(w, e, ej, vj):
    temp = 0
    for j in range(len(random_list)-1):
        temp += ej[j] % n

    ei = int(e, 16) - temp
    ej.insert(message_index, ei)

    vi = w * (r**ei) % n
    vj.insert(message_index, vi)
    return ej, vj


def valuesForSmartContract():
    w, ej, vj = sampleValues()
    global c, uj
    c = compute_C()
    uj = compute_U(w, ej, vj)
    e_st, e = compute_E()
    ej, vj = compute_EI_VI(w, e, ej, vj)
    # print(f'Users.py List: V: {random_list},\nc: {c},\ng: {g},\nn: {n},\nvj: {vj},\nej: {ej},\nuj: {uj}')
    return random_list, c, g, n, vj, ej, uj, e_st, piAuthList, number_of_users




