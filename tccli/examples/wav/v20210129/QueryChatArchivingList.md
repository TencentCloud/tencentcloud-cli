**Example 1: 查询会话存档列表**



Input: 

```
tccli wav QueryChatArchivingList --cli-unfold-argument  \
    --Cursor +1H24tK0tELjSiTOR10DzA \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PageData": [
            {
                "MsgId": "1312616990135121111",
                "Action": "send",
                "MsgType": "video",
                "From": "YangYan",
                "ToList": [
                    "YangGuo"
                ],
                "RoomId": "100001",
                "MsgTime": "1616990135",
                "Video": {
                    "PlayLength": 4,
                    "FileSize": 645990,
                    "CosKey": "http://test"
                }
            }
        ],
        "NextCursor": "+1H24tK0tELjSiTOR10DzA==",
        "RequestId": "4d48312c-a062-4875-a5d5-69f0f11baf96"
    }
}
```

