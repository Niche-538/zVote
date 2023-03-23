// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0;
import "hardhat/console.sol";


contract MyContract {

    uint [3][4][5] myArray;

    function printit() public view {
        console.log(123);
    }
    

    function fillArray() public returns(uint256[3][4][5] memory) {
        
        uint256 randomNum;
        for (uint256 i = 0; i < 5; i++) {
            for (uint256 j = 0; j < 4; j++) {
                for (uint256 k = 0; k < 3; k++) {
                    randomNum = uint256(keccak256(abi.encodePacked(i, j, block.timestamp))) % 2; // Generate a random number between 0 and 1
                    myArray[i][j][k] = randomNum;
                }
            }
        }

        return myArray;
    }
}
