// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0;
import "hardhat/console.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract MyContract {
    uint256 c;
    uint256 n = 7 * 11;
    uint256 g = n + 1;
    uint256 num;
    uint256[5] V;
    uint256[5] vj;
    uint256[5] ej;
    uint256[5] uj;
    uint256 e;

    constructor() public {
        num = 5;
    }

    function randomOracle() public {
        string memory concatInput = Strings.toString(concatenate(c, g, n, V, uj));
        e = uint256(sha256(bytes(concatInput)));
    }

    function concatenate(uint256 a, uint256 b, uint256 d, uint256[5] memory arr1, uint256[5] memory arr2) public pure returns (uint256) {
        string memory str1 = Strings.toString(a);
        string memory str2 = Strings.toString(b);
        string memory str3 = Strings.toString(d);
        string memory str4 = "";

        for (uint i = 0; i < 5; i++) {
            str4 = string(abi.encodePacked(str4, Strings.toString(arr1[i])));
        }

        string memory str5 = "";

        for (uint i = 0; i < 5; i++) {
            str5 = string(abi.encodePacked(str5, Strings.toString(arr2[i])));
        }

        string memory str = string(abi.encodePacked(str5, str1, str2, str3, str4));
        return uint256(keccak256(abi.encodePacked(str)));
    }

    function checkE() public view returns (bool) {
        uint256 eSum = 0;

        for (uint256 i = 0; i < 5; i++) {
            eSum += (ej[i] % n);
        }

        if (eSum == e) {
            return true;
        } else {
            return false;
        }
    }

    function checkvj() public view returns (bool) {
        for (uint256 i = 0; i < 5; i++) {
            uint256 val = (uj[i] * ((c / (g ** V[i])) ** ej[i])) % (n ** 2);

            if (val != vj[i]) {
                return false;
            }
        }

        return true;
    }

    function checkInputValidity() public view returns (bool) {
        return checkE() && checkvj();
    }
}
