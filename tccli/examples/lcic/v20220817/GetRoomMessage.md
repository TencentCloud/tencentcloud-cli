**Example 1: 示例**

示例

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
                "FromAccount": "abc",
                "Seq": 0,
                "MessageBody": [
                    {
                        "MessageType": 0,
                        "TextMessage": "abc",
                        "ImageMessage": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

