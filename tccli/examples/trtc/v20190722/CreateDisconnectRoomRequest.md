**Example 1: CreateDisconnectRoomRequest**

取消多房间PK。{ABC}存在PK关系，取消A房间PK，A房间不存在，取消失败。

Input: 

```
tccli trtc CreateDisconnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RequestSeq 1 \
    --RoomIdType 1 \
    --DisconnectRoom A
```

Output: 
```
{
    "Response": {
        "RequestSeq": 1,
        "ConnectError": "FailedOperation.QueryRoomInfoFailed",
        "DetailErrorMsg": [
            {
                "StrRoomId": "A",
                "ErrorCode": -203010,
                "ErrorMsg": "room not exist"
            }
        ],
        "RequestId": "xxxxx"
    }
}
```

**Example 2: CreateDisconnectRoomRequest-1**

取消多房间PK。{ABC}存在PK关系，取消A，B房间PK，取消成功。

Input: 

```
tccli trtc CreateDisconnectRoomRequest --cli-unfold-argument  \
    --RequestSeq 1 \
    --SdkAppId 1400188366 \
    --RoomIdType 1 \
    --DisconnectRoom A B
```

Output: 
```
{
    "Response": {
        "ConnectError": null,
        "DetailErrorMsg": null,
        "RequestId": "xxxxx",
        "RequestSeq": 1
    }
}
```

**Example 3: CreateDisconnectRoomRequest-2**

取消多房间PK。{ABC}存在PK关系，取消{A,D}，A房间取消PK成功，D房间返回房间不存在。

Input: 

```
tccli trtc CreateDisconnectRoomRequest --cli-unfold-argument  \
    --RequestSeq 1 \
    --SdkAppId 1400188366 \
    --RoomIdType 1 \
    --DisconnectRoom A D
```

Output: 
```
{
    "Response": {
        "RequestSeq": 1,
        "ConnectError": "FailedOperation.QueryRoomInfoFailed",
        "DetailErrorMsg": [
            {
                "StrRoomId": "D",
                "ErrorCode": -203010,
                "ErrorMsg": "room not exist"
            }
        ],
        "RequestId": "xxxxx"
    }
}
```

