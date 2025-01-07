**Example 1: 获取房间事件**

获取房间事件

Input: 

```
tccli lcic GetRoomEvent --cli-unfold-argument  \
    --RoomId 1 \
    --SdkAppId 13465287 \
    --Page 1 \
    --Limit 10 \
    --Keyword 
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Events": [
            {
                "Timestamp": 1,
                "EventType": "MemberJoin",
                "EventData": {
                    "RoomId": 1,
                    "UserId": "2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc"
                }
            }
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

