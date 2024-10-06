// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "contracts/userAuth.sol";

contract RewardsCatalog {

    struct RewardItem {
        string description;
        uint256 pointsRequired;
        bool available;
    }

    mapping(uint256 => RewardItem) public rewardCatalog;

    uint256 public rewardCount;

    modifier rewardExists(uint256 itemID) {
        require(bytes(rewardCatalog[itemID].description).length != 0, "Reward item does not exist");
        _;
    }

    event RewardAdded(uint256 itemID, string description, uint256 pointsRequired);
    event RewardUpdated(uint256 itemID, string newDescription, uint256 newPointsRequired);
    event RewardDeleted(uint256 itemID);
  
    function addRewardItem(string memory description, uint256 pointsRequired) public {
        rewardCatalog[rewardCount] = RewardItem({
            description: description,
            pointsRequired: pointsRequired,
            available: true
        });
        
        emit RewardAdded(rewardCount, description, pointsRequired);
        rewardCount++;
    }

    function updateRewardItem(uint256 itemID, string memory newDescription, uint256 newPointsRequired) public rewardExists(itemID) {
        RewardItem storage item = rewardCatalog[itemID];
        item.description = newDescription;
        item.pointsRequired = newPointsRequired;

        emit RewardUpdated(itemID, newDescription, newPointsRequired);
    }

    function deleteRewardItem(uint256 itemID) public rewardExists(itemID) {
        delete rewardCatalog[itemID];
        emit RewardDeleted(itemID);
    }

    function listRewardItems() public view returns (RewardItem[] memory) {
        RewardItem[] memory availableItems = new RewardItem[](rewardCount);
        uint256 counter = 0;
        for (uint256 i = 0; i < rewardCount; i++) {
            if (rewardCatalog[i].available) {
                availableItems[counter] = rewardCatalog[i];
                counter++;
            }
        }
        return availableItems;
    }
}
