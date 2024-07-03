**Example 1: DescribeConnectRoomRequest**

存在{ABCD}房间PK，查询{A}房间状态，查询成功

Input: 

```
tccli trtc DescribeConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400728753 \
    --RoomIdType 1 \
    --ConnectRoom aaa
```

Output: 
```
{
    "Response": {
        "ConnectError": null,
        "DetailErrorMsg": null,
        "ExistConnectRoom": [
            {
                "ConnectRooms": [
                    "B",
                    "C",
                    "D"
                ],
                "LastRequestSeq": 13,
                "SelfRoomId": "A"
            }
        ],
        "RequestId": "f8e446fa-7811-43be-a720-3427de6bc193"
    }
}
```

**Example 2: DescribeConnectRoomRequest-1**

存在{ABCD}房间PK

Input: 

```
tccli trtc DescribeConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400728753 \
    --RoomIdType 1 \
    --ConnectRoom A E F
```

Output: 
```
{
    "Response": {
        "ConnectError": "FailedOperation.GetConnectRoomInfoFailed",
        "DetailErrorMsg": [
            {
                "ErrorCode": -203010,
                "ErrorMsg": "room not exist",
                "StrRoomId": "F"
            },
            {
                "ErrorCode": -203004,
                "ErrorMsg": "conned room not exist",
                "StrRoomId": "E"
            }
        ],
        "ExistConnectRoom": [
            {
                "ConnectRooms": [
                    "B",
                    "C",
                    "D"
                ],
                "LastRequestSeq": 13,
                "SelfRoomId": "A"
            },
            {
                "ConnectRooms": null,
                "SelfRoomId": "E"
            }
        ],
        "RequestId": "a3b69432-51b8-4fd3-b122-338c457578ed"
    }
}
```

