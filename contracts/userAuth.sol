// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
// # ------------------------------------------------------------------
// #                             IMPORTS
// # ------------------------------------------------------------------
import "./notifications.sol";
import "./rewardPoints.sol";
import "./adminFunctions.sol";
import "./rewardCatalog.sol";
import "./userRewardManagement.sol";

contract UserAuth {

    // ------------------------------------------------------------------
    //                             EVENTS
    // ------------------------------------------------------------------
    event UserRegistered(uint userID);
    event UserAuthenticated(uint userID, string message);
    
    // ------------------------------------------------------------------
    //                             DATA
    // ------------------------------------------------------------------
    struct User {
        uint userID;
        address userAddress;
        bool isAuthenticated;
    }

    mapping(address => User) public users;

    modifier isRegistered(address _userAddress) {
        require(users[_userAddress].userID != 0, "User is not registered. Please register first.");
        _;
    }

    // ------------------------------------------------------------------
    //                             CONTRACT
    // ------------------------------------------------------------------
    
    function registerUser(uint _userID) public {
        require(users[msg.sender].userID == 0, "User is already registered");

        users[msg.sender] = User({
            userID: _userID,
            userAddress: msg.sender,
            isAuthenticated: false
        });

        emit UserRegistered(_userID);
    }
     
    function authenticateUser() public isRegistered(msg.sender) {
        users[msg.sender].isAuthenticated = true;
        emit UserAuthenticated(users[msg.sender].userID, "User is authenticated");
    }
}