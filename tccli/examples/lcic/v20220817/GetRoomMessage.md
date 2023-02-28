**Example 1: 示例**

获取房间历史消息示例

Input: 

```
tccli lcic GetRoomMessage --cli-unfold-argument  \
    --SdkAppId 0 \
    --RoomId 1 \
    --Seq 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Messages": [
            {
                "Timestamp": 0,
                "FromAccount": "xx",
                "Seq": 0,
                "MessageBody": [
                    {
                        "MessageType": 0,
                        "TextMessage": "xx",
                        "ImageMessage": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

