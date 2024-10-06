// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "contracts/userAuth.sol";

contract UserRewardManagement {

    mapping(uint => uint) public userPoints;

    event GetUserPoints(uint indexed userID, uint points);
    event RewardRedeemed(uint indexed userID, string rewardDescription, uint pointsSpent);

    function get_user_points(uint userID) public {
        uint points = userPoints[userID];
        emit GetUserPoints(userID, points);  
    }

    function awardPoints(uint userID, uint points) public {
        userPoints[userID] += points; 
    }

    function redeemReward(uint userID, string memory rewardDescription, uint pointsRequired) public {
        require(userPoints[userID] >= pointsRequired, "Not enough points to redeem the reward");  
        userPoints[userID] -= pointsRequired;  
        emit RewardRedeemed(userID, rewardDescription, pointsRequired);
    }
}