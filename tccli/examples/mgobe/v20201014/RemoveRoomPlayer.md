**Example 1: 修改房间玩家自定义状态**

修改房间玩家自定义状态

Input: 

```
tccli mgobe RemoveRoomPlayer --cli-unfold-argument  \
    --GameId obg-mqsqod93 \
    --RemovePlayerId 1xqwlevd
```

Output: 
```
{
    "Response": {
        "RequestId": "1f7dc756-ad45-40c9-911d-8700c6d63a9d",
        "Room": {
            "CreateTime": 1610357327,
            "CreateType": 0,
            "CustomProperties": "xxxxxxxxx",
            "FrameRate": 15,
            "FrameSyncState": 0,
            "Id": "Kefy5lE",
            "IsForbidJoin": false,
            "IsPrivate": true,
            "MaxPlayers": 10,
            "Name": "测试",
            "Owner": "1nv49l55",
            "OwnerOpenId": "",
            "Players": [
                {
                    "CustomPlayerStatus": 112233,
                    "CustomProfile": "测试人员12321",
                    "IsRobot": false,
                    "Name": "czh007测试",
                    "OpenId": "",
                    "PlayerId": "1nv49l55",
                    "TeamId": "0"
                }
            ],
            "RouteId": "4hrNbSFqepv7dGq/wLw+jN7E2nvfCNep7N5WO01EktcFJtru+173SH5opwUZOxJK",
            "StartGameTime": 0,
            "Teams": [
                {
                    "Id": "0",
                    "MaxPlayers": 10,
                    "MinPlayers": 1,
                    "Name": ""
                }
            ],
            "Type": "A"
        }
    }
}
```

