**Example 1: 查询会话存档列表**



Input: 

```
tccli wav QueryChatArchivingList --cli-unfold-argument  \
    --Cursor xxxx \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PageData": [
            {
                "MsgId": "xx",
                "Action": "send",
                "MsgType": "video",
                "From": "xx",
                "ToList": [
                    "xx"
                ],
                "RoomId": "xx",
                "MsgTime": "1616990135",
                "Video": {
                    "PlayLength": 4,
                    "FileSize": 645990,
                    "CosKey": "http://xx"
                }
            }
        ],
        "NextCursor": "xx",
        "RequestId": "xx"
    }
}
```

