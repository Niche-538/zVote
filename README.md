# zVote
Course project for graduate level course CIS6930: Advanced Blockchain at the University of Florida.

This project is an implementation of the <a href="https://ieeexplore.ieee.org/document/9838690">zVote</a> research paper. The Zero-Knowledge Proof (ZKP) is used to check the validity of the votes submitted by the user. The user encrypt their votes using the Paillier encryption system and sends a proof to the smart contract. The smart contract verifies the validity of the votes. This validation occurs without the users needing to disclose any private information about themselves.

# Additional libraries required
1. phe: Python Paillier encryption library.
2. web3: Python web3 library.
3. py-solc-x: Python wrapper tool for solc Solidity compiler.
4. pymerkle: Python library for Merkle Tree

# How to Run
1. Clone this repository in your local system.
2. Install Ganache.
3. Create a workspace in the Ganache.
4. In the ganacheconnector.py file ensure that the variable 'ganache_url' is equal to the 'RPC Server' value in your ganache workspace.
5. In a command line terminal, ensure that you are in the project directory.
6. Run 'python3 ganacheconnector.py' in the terminal.
