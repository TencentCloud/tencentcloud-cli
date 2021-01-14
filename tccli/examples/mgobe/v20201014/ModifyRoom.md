**Example 1: 修改房间玩家自定义状态**

修改房间玩家自定义状态

Input: 

```
tccli mgobe ModifyRoom --cli-unfold-argument  \
    --GameId obg-mqsqod93 \
    --RoomName 我是一个房间名 \
    --Owner 1xqwlevd \
    --CustomProperties 国王乱杀懂? \
    --RoomId Kefy5lE \
    --PlayerId 1xqwlevd \
    --ChangeRoomOptionList 0 1 5
```

Output: 
```
{
    "Response": {
        "RequestId": "329991b3-edd5-4fe9-b6d6-b5d108f64f81",
        "Room": {
            "CreateTime": 1610357327,
            "CreateType": 0,
            "CustomProperties": "国王乱杀懂?",
            "FrameRate": 15,
            "FrameSyncState": 0,
            "Id": "Kefy5lE",
            "IsForbidJoin": false,
            "IsPrivate": true,
            "MaxPlayers": 10,
            "Name": "我是一个房间名",
            "Owner": "1xqwlevd",
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

