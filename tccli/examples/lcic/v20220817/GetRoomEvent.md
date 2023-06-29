**Example 1: 获取房间事件**

获取房间事件

Input: 

```
tccli lcic GetRoomEvent --cli-unfold-argument  \
    --RoomId 1 \
    --SdkAppId 1234 \
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
                "EventType": "abc",
                "EventData": {
                    "RoomId": 1,
                    "UserId": "abc"
                }
            }
        ],
        "RequestId": "abc"
    }
}
```

