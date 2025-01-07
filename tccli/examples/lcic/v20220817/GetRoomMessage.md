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
                "FromAccount": "2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc",
                "Seq": 0,
                "MessageBody": [
                    {
                        "MessageType": 0,
                        "TextMessage": "hello",
                        "ImageMessage": "https://www.image.com/haha.jpg",
                        "CustomMessage": {
                            "Data": "data",
                            "Desc": "custom_message",
                            "Ext": "CHAT"
                        }
                    }
                ]
            }
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

