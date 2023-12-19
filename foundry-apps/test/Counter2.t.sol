// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import {Test, stdError} from "forge-std/Test.sol";
import {Counter2} from "src/Counter2.sol";

contract Counter2Test is Test {
    Counter2 public counter2;

    function setUp() public {
        counter2 = new Counter2();
    }

    function testInc() public {
        counter2.inc();
        assertEq(
            counter2.count(),
            1
        );
    }

    function testFailDec() public {
        counter2.dec();
        // counter2.inc();
    }

    function testDecUnderflow() public {
        vm.expectRevert(stdError.arithmeticError);
        counter2.dec();
    }

    function testDec() public {
        counter2.inc();
        counter2.inc();
        counter2.dec();
        assertEq(
            counter2.count(),
            1
        );
    }
}