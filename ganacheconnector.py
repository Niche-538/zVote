import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
w3 = Web3(Web3.HTTPProvider(ganache_url))

print(w3.is_connected())
print(w3.eth.block_number)

deploy_address = w3.eth.accounts[0]

abi = """[
    {
        "inputs": [],
        "name": "randomOracle",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [],
        "name": "checkE",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "checkInputValidity",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "checkvj",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "a",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "b",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "d",
                "type": "uint256"
            },
            {
                "internalType": "uint256[5]",
                "name": "arr1",
                "type": "uint256[5]"
            },
            {
                "internalType": "uint256[5]",
                "name": "arr2",
                "type": "uint256[5]"
            }
        ],
        "name": "concatenate",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "pure",
        "type": "function"
    }
]"""

abi_var = json.loads(abi)
bytecode_var = "608060405234801561001057600080fd5b50600436106100575760003560e01c8063306e3db41461005c5780639c2492d71461007a578063a224c19814610098578063a6ced1d6146100a2578063c61aa118146100d2575b600080fd5b6100646100f0565b6040516100719190610712565b60405180910390f35b61008261010f565b60405161008f9190610712565b60405180910390f35b6100a0610182565b005b6100bc60048036038101906100b791906108b9565b610277565b6040516100c99190610945565b60405180910390f35b6100da6103f4565b6040516100e79190610712565b60405180910390f35b60006100fa61010f565b801561010a57506101096103f4565b5b905090565b6000806000905060005b600581101561016557600154600e826005811061013957610138610960565b5b015461014591906109be565b826101509190610a1e565b9150808061015d90610a52565b915050610119565b50601854810361017957600191505061017f565b60009150505b90565b600061021961021460005460025460015460046005806020026040519081016040528092919082600580156101cc576020028201915b8154815260200190600101908083116101b8575b5050505050601360058060200260405190810160405280929190826005801561020a576020028201915b8154815260200190600101908083116101f6575b5050505050610277565b6104d6565b905060028160405161022b9190610b0b565b602060405180830381855afa158015610248573d6000803e3d6000fd5b5050506040513d601f19601f8201168201806040525081019061026b9190610b58565b60001c60188190555050565b600080610283876104d6565b90506000610290876104d6565b9050600061029d876104d6565b9050600060405180602001604052806000815250905060005b600581101561031557816102e08983600581106102d6576102d5610960565b5b60200201516104d6565b6040516020016102f1929190610bcc565b6040516020818303038152906040529150808061030d90610a52565b9150506102b6565b50600060405180602001604052806000815250905060005b600581101561038c578161035789836005811061034d5761034c610960565b5b60200201516104d6565b604051602001610368929190610bcc565b6040516020818303038152906040529150808061038490610a52565b91505061032d565b50600081868686866040516020016103a8959493929190610bf0565b6040516020818303038152906040529050806040516020016103ca9190610c3b565b6040516020818303038152906040528051906020012060001c965050505050505095945050505050565b600080600090505b60058110156104cd57600060026001546104169190610d92565b600e836005811061042a57610429610960565b5b0154600484600581106104405761043f610960565b5b015460025461044f9190610ddd565b60005461045c9190610e28565b6104669190610ddd565b6013846005811061047a57610479610960565b5b01546104869190610e59565b61049091906109be565b9050600982600581106104a6576104a5610960565b5b015481146104b9576000925050506104d3565b5080806104c590610a52565b9150506103fc565b50600190505b90565b6060600060016104e5846105a4565b01905060008167ffffffffffffffff81111561050457610503610788565b5b6040519080825280601f01601f1916602001820160405280156105365781602001600182028036833780820191505090505b509050600082602001820190505b600115610599578080600190039150507f3031323334353637383961626364656600000000000000000000000000000000600a86061a8153600a858161058d5761058c61098f565b5b04945060008503610544575b819350505050919050565b600080600090507a184f03e93ff9f4daa797ed6e38ed64bf6a1f0100000000000000008310610602577a184f03e93ff9f4daa797ed6e38ed64bf6a1f01000000000000000083816105f8576105f761098f565b5b0492506040810190505b6d04ee2d6d415b85acef8100000000831061063f576d04ee2d6d415b85acef810000000083816106355761063461098f565b5b0492506020810190505b662386f26fc10000831061066e57662386f26fc1000083816106645761066361098f565b5b0492506010810190505b6305f5e1008310610697576305f5e100838161068d5761068c61098f565b5b0492506008810190505b61271083106106bc5761271083816106b2576106b161098f565b5b0492506004810190505b606483106106df57606483816106d5576106d461098f565b5b0492506002810190505b600a83106106ee576001810190505b80915050919050565b60008115159050919050565b61070c816106f7565b82525050565b60006020820190506107276000830184610703565b92915050565b6000604051905090565b600080fd5b6000819050919050565b61074f8161073c565b811461075a57600080fd5b50565b60008135905061076c81610746565b92915050565b600080fd5b6000601f19601f8301169050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052604160045260246000fd5b6107c082610777565b810181811067ffffffffffffffff821117156107df576107de610788565b5b80604052505050565b60006107f261072d565b90506107fe82826107b7565b919050565b600067ffffffffffffffff82111561081e5761081d610788565b5b602082029050919050565b600080fd5b600061084161083c84610803565b6107e8565b9050806020840283018581111561085b5761085a610829565b5b835b818110156108845780610870888261075d565b84526020840193505060208101905061085d565b5050509392505050565b600082601f8301126108a3576108a2610772565b5b60056108b084828561082e565b91505092915050565b60008060008060006101a086880312156108d6576108d5610737565b5b60006108e48882890161075d565b95505060206108f58882890161075d565b94505060406109068882890161075d565b93505060606109178882890161088e565b9250506101006109298882890161088e565b9150509295509295909350565b61093f8161073c565b82525050565b600060208201905061095a6000830184610936565b92915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601260045260246000fd5b60006109c98261073c565b91506109d48361073c565b9250826109e4576109e361098f565b5b828206905092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b6000610a298261073c565b9150610a348361073c565b9250828201905080821115610a4c57610a4b6109ef565b5b92915050565b6000610a5d8261073c565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8203610a8f57610a8e6109ef565b5b600182019050919050565b600081519050919050565b600081905092915050565b60005b83811015610ace578082015181840152602081019050610ab3565b60008484015250505050565b6000610ae582610a9a565b610aef8185610aa5565b9350610aff818560208601610ab0565b80840191505092915050565b6000610b178284610ada565b915081905092915050565b6000819050919050565b610b3581610b22565b8114610b4057600080fd5b50565b600081519050610b5281610b2c565b92915050565b600060208284031215610b6e57610b6d610737565b5b6000610b7c84828501610b43565b91505092915050565b600081519050919050565b600081905092915050565b6000610ba682610b85565b610bb08185610b90565b9350610bc0818560208601610ab0565b80840191505092915050565b6000610bd88285610b9b565b9150610be48284610b9b565b91508190509392505050565b6000610bfc8288610b9b565b9150610c088287610b9b565b9150610c148286610b9b565b9150610c208285610b9b565b9150610c2c8284610b9b565b91508190509695505050505050565b6000610c478284610b9b565b915081905092915050565b60008160011c9050919050565b6000808291508390505b6001851115610ca957808604811115610c8557610c846109ef565b5b6001851615610c945780820291505b8081029050610ca285610c52565b9450610c69565b94509492505050565b600082610cc25760019050610d7e565b81610cd05760009050610d7e565b8160018114610ce65760028114610cf057610d1f565b6001915050610d7e565b60ff841115610d0257610d016109ef565b5b8360020a915084821115610d1957610d186109ef565b5b50610d7e565b5060208310610133831016604e8410600b8410161715610d545782820a905083811115610d4f57610d4e6109ef565b5b610d7e565b610d618484846001610c5f565b92509050818404811115610d7857610d776109ef565b5b81810290505b9392505050565b600060ff82169050919050565b6000610d9d8261073c565b9150610da883610d85565b9250610dd57fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8484610cb2565b905092915050565b6000610de88261073c565b9150610df38361073c565b9250610e207fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8484610cb2565b905092915050565b6000610e338261073c565b9150610e3e8361073c565b925082610e4e57610e4d61098f565b5b828204905092915050565b6000610e648261073c565b9150610e6f8361073c565b9250828202610e7d8161073c565b91508282048414831517610e9457610e936109ef565b5b509291505056fea264697066735822122064a5570b29b88e0e08e6e0d0c91ead283601067ab6836333bfa3053096cdbd9464736f6c63430008120033"
zkp_contract = w3.eth.contract(abi=abi_var, bytecode=bytecode_var)

tx_hash = zkp_contract.constructor().transact()
print(tx_hash)