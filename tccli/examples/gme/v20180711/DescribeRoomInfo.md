**Example 1: 获取房间内用户信息**



Input: 

```
tccli gme DescribeRoomInfo --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --RoomIds 88888
```

Output: 
```
{
    "Response": {
        "Result": 0,
        "RoomUsers": [
            {
                "RoomId": 88888,
                "Uins": [
                    1234,
                    5678
                ]
            }
        ],
        "RequestId": "xxx-xxx-xxx"
    }
}
```

