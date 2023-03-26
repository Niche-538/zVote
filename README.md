# zVote
Course project for graduate level course CIS6930: Advanced Blockchain at the University of Florida.

This project is an implementation of the <a href="https://ieeexplore.ieee.org/document/9838690">zVote</a> research paper. The Zero-Knowledge Proof (ZKP) is used to check the validity of the votes submitted by the user. The user encrypt their votes using the Paillier encryption system and sends a proof to the smart contract. The smart contract verifies the validity of the votes. This validation occurs without the users needing to disclose any private information about themselves.

# Additional libraries required
1. phe: Python Paillier encryption library.
2. web3: Python web3 library.
3. py-solc-x: Python wrapper tool for solc Solidity compiler.
