// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0;
import "hardhat/console.sol";


contract MyContract {

    uint [3][4][5] myArray;

    function printArray() public view {
        for (uint256 i = 0; i < 5; i++) {
            for (uint256 j = 0; j < 4; j++) {
                console.log(myArray[i][j][0],myArray[i][j][1],myArray[i][j][2]);
            }
        }
    }
    

    function fillArray() public returns(uint256[3][4][5] memory) {
        uint256 randomNum;
        for (uint256 i = 0; i < 5; i++) {
            for (uint256 j = 0; j < 4; j++) {
                    randomNum = uint256(keccak256(abi.encodePacked(i, j, block.timestamp))) % 3; // Generate a random number between 0 and 1
                    myArray[i][j][randomNum] = 1;
            }
        }
        return myArray;
    }

    function ceilLog2(uint256 x) public pure returns (uint256) {
        uint256 result = 0;

        if (x > 1) {
            uint256 temp = x - 1;

            while (temp > 0) {
                temp >>= 1;
                result += 1;
            }
        }

        return result;
    }

    function encryptQuestion() public view returns(uint256) {
        uint256 b = ceilLog2(5);
        
        for (uint256 i = 0; i < 5; i++) {
            uint256 questionsSum = 0;
            for (uint256 j = 0; j < 4; j++) {
                uint256 optionsSum = 0;
                for (uint256 k = 0; k < 3; k++) {
                    optionsSum += myArray[i][j][k] * (2 ** (k * b)); //b * Options
                }
                questionsSum += optionsSum * (2 ** (j * b * 3)); //b * L * Questions
            }
            console.log(questionsSum);
        }

        return 1;
    }

    function generatePublicKey() public returns(){
        uint256 p=151;
        uint256 q=173;
        uint256 n=p*q;
        uint256 g=1123581321;
        
    }
    function printNum(uint256 x) public view returns(uint256){
        console.log(x);
        return x;
    }

}
