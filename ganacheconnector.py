from users import valuesForSmartContract
from web3 import Web3
from solcx import install_solc, compile_source
import time

# installs the latest version of solc
install_solc(version='latest')

# read the smart contract written in solidity
with open('zkp-contract.sol') as f:
    read_sol = f.readlines()

# compile the smart contract and fetch the abi and bin values
compiled_sol = compile_source("".join(read_sol), output_values=['abi', 'bin'])

contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

# set the Ganache URL
ganache_url = "http://127.0.0.1:7545"
# Connect to Ganache using web3 library
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.default_account = w3.eth.accounts[1]

# interact with the smart contract using web3 contract instances
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = contract.constructor().transact()

# The transaction receipt contains an address that should be used to interact with functions of the contract
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

zkp_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

V, c, g, n, vj, ej, uj, e_st, piAuth, nop = valuesForSmartContract()
st = time.time()
tx_hash = zkp_contract.functions.setValues(V, c, g, n, vj, ej, uj, e_st, piAuth, nop).transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print('Check Validity: ', zkp_contract.functions.checkInputValidity().call())
print(f'time: {time.time() - st}')
