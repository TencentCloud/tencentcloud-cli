**Example 1: CreateConnectRoomRequest**

创建多房间PK，本地存在{AB}PK,发起old{AB}，new{ABC}房间PK。PK成功

Input: 

```
tccli trtc CreateConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RequestSeq 1 \
    --RoomIdType 1 \
    --OldConnectRoom.0.ConnectedRoomList A B \
    --NewConnectRoom A B C
```

Output: 
```
{
    "Response": {
        "ConnectError": null,
        "DetailErrorMsg": null,
        "ExistConnectRoom": null,
        "RequestId": "xxxxxx",
        "RequestSeq": 1
    }
}
```

**Example 2: CreateConnectRoomRequest-1**

创建多房间PK，本地不存在PK，发起old{},new{AB}房间PK。PK成功

Input: 

```
tccli trtc CreateConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RequestSeq 1 \
    --RoomIdType 1 \
    --NewConnectRoom A B
```

Output: 
```
{
    "Response": {
        "ConnectError": null,
        "DetailErrorMsg": null,
        "ExistConnectRoom": null,
        "RequestId": "xxxxxx",
        "RequestSeq": 1
    }
}
```

**Example 3: CreateConnectRoomRequest-2**

创建多房间PK，本地不存在PK，发起old{},new{ABC}房间PK。A房间不存在，PK失败。

Input: 

```
tccli trtc CreateConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RequestSeq 1 \
    --RoomIdType 1 \
    --NewConnectRoom A B C
```

Output: 
```
{
    "Response": {
        "RequestSeq": 1,
        "ExistConnectRoom": null,
        "ConnectError": "FailedOperation.QueryRoomInfoFailed",
        "DetailErrorMsg": [
            {
                "StrRoomId": "A",
                "ErrorCode": -203010,
                "ErrorMsg": "room not exist"
            }
        ],
        "RequestId": "dba067e6-cdb0-4500-bfdb-c6f3a1799e9c"
    }
}
```

**Example 4: CreateConnectRoomRequest-3**

创建多房间PK，本地存在{AB}PK，发起old{AC},new{ABC}房间PK。本地PK状态与oldlist不一致，PK失败，返回本地状态{AB}

Input: 

```
tccli trtc CreateConnectRoomRequest --cli-unfold-argument  \
    --SdkAppId 1400188366 \
    --RequestSeq 1 \
    --RoomIdType 1 \
    --OldConnectRoom.0.ConnectedRoomList A C \
    --NewConnectRoom A B C
```

Output: 
```
{
    "Response": {
        "ConnectError": "FailedOperation.ConnectRoomFailed",
        "DetailErrorMsg": [
            {
                "ErrorCode": -203063,
                "ErrorMsg": "API oldlist not equal with local",
                "StrRoomId": "A"
            },
            {
                "ErrorCode": -203063,
                "ErrorMsg": "API oldlist not equal with local",
                "StrRoomId": "B"
            },
            {
                "ErrorCode": -203063,
                "ErrorMsg": "API oldlist not equal with local",
                "StrRoomId": "C"
            }
        ],
        "ExistConnectRoom": [
            {
                "ConnectRooms": [
                    "B"
                ],
                "LastRequestSeq": 1,
                "SelfRoomId": "A"
            },
            {
                "ConnectRooms": [
                    "A"
                ],
                "LastRequestSeq": 1,
                "SelfRoomId": "B"
            },
            {
                "ConnectRooms": null,
                "SelfRoomId": "C"
            }
        ],
        "RequestId": "dba067e6-cdb0-4500-bfdb-c6f3a1799e9c",
        "RequestSeq": 1
    }
}
```

