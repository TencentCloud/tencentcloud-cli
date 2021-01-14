**Example 1: 修改房间玩家自定义状态**

修改房间玩家自定义状态

Input: 

```
tccli mgobe ChangeRoomPlayerStatus --cli-unfold-argument  \
    --GameId obg-mqsqod93 \
    --CustomStatus 123 \
    --PlayerId 1xqwlevd
```

Output: 
```
{
    "Response": {
        "RequestId": "7d56ee17-e6d7-4faf-8643-db4f0adcd39a",
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
                },
                {
                    "CustomPlayerStatus": 123,
                    "CustomProfile": "测试人员xxxxxxxxx",
                    "IsRobot": false,
                    "Name": "测试人员1",
                    "OpenId": "",
                    "PlayerId": "1xqwlevd",
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

