// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "contracts/userAuth.sol";

contract reward_points {
  
  event point_Awarded(uint userID, uint points_Awarded);
  event point_Deducted(uint userID, uint points_Deducted);
  
  mapping(uint => uint) public userPoints;

  function awardPoints(uint userID, uint pointsAwarded) public {
     userPoints[userID] += pointsAwarded;
     emit point_Awarded(userID, pointsAwarded);
  } 

  function deductPoints(uint userID, uint pointsDeducted) public {
    require(userPoints[userID] >= pointsDeducted, "Insufficient points");
    userPoints[userID] -= pointsDeducted;
    emit point_Deducted(userID, pointsDeducted);
  }
} 