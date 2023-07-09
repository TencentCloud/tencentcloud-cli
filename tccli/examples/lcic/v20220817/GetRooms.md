**Example 1: 示例**

示例

Input: 

```
tccli lcic GetRooms --cli-unfold-argument  \
    --SdkAppId 1 \
    --StartTime 1 \
    --EndTime 1 \
    --Page 1 \
    --Limit 1 \
    --Status 0 1 2 3
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Rooms": [
            {
                "Name": "abc",
                "RoomId": 1,
                "Status": 1,
                "StartTime": 1,
                "EndTime": 1,
                "RealStartTime": 1,
                "RealEndTime": 1,
                "Resolution": 1,
                "MaxRTCMember": 1,
                "ReplayUrl": "abc",
                "EnableDirectControl": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

