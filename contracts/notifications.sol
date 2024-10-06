// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "contracts/userAuth.sol";

contract notifications {
 
  event message(uint user_ID, string msg);
  
  function notifyUser(uint userID, string memory letter) public {
    emit message(userID, letter);   
  }
}
