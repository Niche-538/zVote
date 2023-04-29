// SPDX-License-Identifier: UNLICENSED

pragma solidity >=0.7.0;

contract MyContract {
    uint256[7] c;
    uint256 n = 0;
    uint256 g = 0;
    uint256[7] V;
    uint256[7] vj;
    uint256[7] ej;
    uint256[7] uj;
    bytes32 e;
    bool eb;
    bool vjb;
    bytes concatInput;
    string temp;
    string e_st_py;

    constructor() {}

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

    function getList() public view returns(uint256[7] memory, uint256[7] memory, uint256, uint256, uint256[7] memory, uint256[7] memory) {
        return (uj, c, g, n, V, vj);
    }

    function setValues(uint256[7] memory VP, uint256[7] memory cp, uint256 gp, uint256 np, uint256[7] memory vjp, uint256[7] memory ejp, uint256[7] memory ujp, string memory e_st_p) public {
        V = VP;
        c = cp;
        g = gp;
        n = np;
        vj = vjp;
        ej = ejp;
        uj = ujp;
        e_st_py = e_st_p;
    }

    function randomOracle() public returns (string memory, bytes memory, bytes32){
        string memory st;
        (st, concatInput) = concatenate();
        return (st, concatInput, sha256(concatInput));
    }

    function concatenate() public view returns (string memory, bytes memory) {
        string memory str1 = "";

        for (uint i = 0; i < 7; i++) {
            str1 = string(abi.encodePacked(str1, toStringFunction(uint256(uj[i]))));
        }

        string memory str2 = "";

        for (uint i = 0; i < 7; i++) {
            str2 = string(abi.encodePacked(str2, toStringFunction(uint256(c[i]))));
        }

        string memory str3 = toStringFunction(uint256(g));
        string memory str4 = toStringFunction(uint256(n));

        string memory str5 = "";

        for (uint i = 0; i < 7; i++) {
            str5 = string(abi.encodePacked(str5, toStringFunction(uint256(V[i]))));
        }

        string memory str = string.concat(str1, str2, str3, str4, str5);
        return (str, abi.encodePacked(str));
    }

    function check_E() public returns (string memory, string memory, bool) {
        uint256 eSum = 0;
        string memory e_str1;
        bytes memory tempe;
        bytes32 en;
        (e_str1, tempe, en) = randomOracle();
        e_str1 = string(e_str1);
        for (uint256 i = 0; i < 7; i++) {
            eSum += (ej[i] % n);
        }
        if (keccak256(abi.encodePacked(e_str1)) == keccak256(abi.encodePacked(e_st_py))) {
            return (e_str1, e_st_py, true);
        } else {
            return (e_str1, e_st_py, false);
        }
    }

    function check_Vj() public view returns (uint256, uint256, bool) {
        uint256 val;
        for (uint256 i = 0; i < 7; i++) {
            if (ej[i] > 1000) {
                continue;
            }
            else {
                val = (uj[i]) * ((c[i] / (g ** V[i])) ** (ej[i])) % (n ** 2);
                if (val == 0 || val == 1) {
                    continue;
                }
                uint256 vjn = vj[i] ** n;
                if (val != vjn) {
                    return (val, vjn, false);
                }
            }
        }
        return (1, 1, true);
    }

    function checkInputValidity() public returns (bool, bool) {
        uint256 t1;
        uint256 t2;
        string memory et1;
        string memory et2;
        (et1, et2, eb) = check_E();
        (t1, t2, vjb) = check_Vj();
        return (eb, vjb);
    }
}
