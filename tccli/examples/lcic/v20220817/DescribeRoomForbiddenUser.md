**Example 1: 获取房间中被禁言人员列表**



Input: 

```
tccli lcic DescribeRoomForbiddenUser --cli-unfold-argument  \
    --SdkAppId 23233 \
    --RoomId 344563
```

Output: 
```
{
    "Response": {
        "MutedAccountList": [
            {
                "MemberAccount": "23ksl89sdhk&sddd",
                "MutedUntil": 10
            }
        ],
        "RequestId": "udkuisncjdlskm"
    }
}
```

