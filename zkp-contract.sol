// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0;
// import "hardhat/console.sol";

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

    function log10(uint256 value) internal pure returns (uint256) {
        uint256 result = 0;
        unchecked {
            if (value >= 10 ** 64) {
                value /= 10 ** 64;
                result += 64;
            }
            if (value >= 10 ** 32) {
                value /= 10 ** 32;
                result += 32;
            }
            if (value >= 10 ** 16) {
                value /= 10 ** 16;
                result += 16;
            }
            if (value >= 10 ** 8) {
                value /= 10 ** 8;
                result += 8;
            }
            if (value >= 10 ** 4) {
                value /= 10 ** 4;
                result += 4;
            }
            if (value >= 10 ** 2) {
                value /= 10 ** 2;
                result += 2;
            }
            if (value >= 10 ** 1) {
                result += 1;
            }
        }
        return result;
    }

    function toStringFunction(uint256 value) internal pure returns (string memory) {
        bytes16 _SYMBOLS = "0123456789abcdef";
        unchecked {
            uint256 length = log10(value) + 1;
            string memory buffer = new string(length);
            uint256 ptr;
            /// @solidity memory-safe-assembly
            assembly {
                ptr := add(buffer, add(32, length))
            }
            while (true) {
                ptr--;
                /// @solidity memory-safe-assembly
                assembly {
                    mstore8(ptr, byte(mod(value, 10), _SYMBOLS))
                }
                value /= 10;
                if (value == 0) break;
            }
            return buffer;
        }
    }

    function getNum() public view returns(uint256) {
        return num;
    }

    function setNum(uint256 n) public {
        num = n;
    }

    function randomOracle() public {
        string memory concatInput = toStringFunction(concatenate(c, g, n, V, uj));
        e = uint256(sha256(bytes(concatInput)));
    }

    function concatenate(uint256 a, uint256 b, uint256 d, uint256[5] memory arr1, uint256[5] memory arr2) public pure returns (uint256) {
        string memory str1 = toStringFunction(a);
        string memory str2 = toStringFunction(b);
        string memory str3 = toStringFunction(d);
        string memory str4 = "";

        for (uint i = 0; i < 5; i++) {
            str4 = string(abi.encodePacked(str4, toStringFunction(arr1[i])));
        }

        string memory str5 = "";

        for (uint i = 0; i < 5; i++) {
            str5 = string(abi.encodePacked(str5, toStringFunction(arr2[i])));
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
