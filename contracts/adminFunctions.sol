// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

event adminAdded(string admin1, uint adminID);

contract adminFunctions {
  mapping(address => uint) admins;
  function addAdmin(address admin, uint admin_ID) public {
    admins[admin] = admin_ID;
    emit adminAdded("Admin Added", admin_ID);
  }

  function removeAdmin(address admin) public {
     delete admins[admin];
  }
}
 