**Example 1: 查询房间信息**

查询房间信息

Input: 

```
tccli mgobe DescribeRoom --cli-unfold-argument  \
    --GameId obg-fr4vwil4 \
    --PlayerId joe123455
```

Output: 
```
{
    "Response": {
        "Room": {
            "Name": "xx",
            "IsForbidJoin": false,
            "StartGameTime": 0,
            "Owner": "xx",
            "FrameRate": 15,
            "MaxPlayers": 2,
            "Teams": [
                {
                    "MinPlayers": 1,
                    "Id": "xx",
                    "MaxPlayers": 1,
                    "Name": "xx"
                },
                {
                    "MinPlayers": 1,
                    "Id": "xx",
                    "MaxPlayers": 1,
                    "Name": "xx"
                }
            ],
            "Players": [
                {
                    "OpenId": "joe123455",
                    "Name": "xx",
                    "CustomProfile": "worker",
                    "IsRobot": false,
                    "PlayerId": "joe123455",
                    "CustomPlayerStatus": 1,
                    "TeamId": "xx"
                },
                {
                    "OpenId": "xx",
                    "Name": "xx",
                    "CustomProfile": "xx",
                    "IsRobot": false,
                    "PlayerId": "xx",
                    "CustomPlayerStatus": 1,
                    "TeamId": "xx"
                }
            ],
            "CreateTime": 1578494768,
            "FrameSyncState": 0,
            "CreateType": 2,
            "CustomProperties": "xx",
            "IsPrivate": true,
            "OwnerOpenId": "xx",
            "RouteId": "xx",
            "Type": "xx",
            "Id": "xx"
        },
        "RequestId": "xx"
    }
}
```

