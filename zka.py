import hashlib
import random
from ia import create_merkle_tree, verify_merkle_path

xi = []


def create_user_list():
    users = [0, 1, 2, 3]
    print("hello")
    global xi
    for i in range(len(users)):
        rand = str(random.randint(0, 100))
        xi.append(hashlib.sha256(rand.encode()).hexdigest())   
    xi.append('c')
    create_merkle_tree(xi)


def submit_vote(user_idx):
    proof = verify_merkle_path(xi[user_idx])
    generate_pi_auth(proof)


def generate_pi_auth(proof):
    print(proof['path'])
    concat = ""
    for i in range(len(proof['path'])):
        concat += proof['path'][i][1]
    pi_auth = hashlib.sha256(concat.encode()).hexdigest()
    print(pi_auth)


create_user_list()
submit_vote(4)
