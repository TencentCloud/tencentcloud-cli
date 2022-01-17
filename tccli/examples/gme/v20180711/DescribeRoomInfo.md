**Example 1: 获取房间内用户信息**



Input: 

```
tccli gme DescribeRoomInfo --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --RoomIds 88888 \
    --StrRoomIds aaaaa
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

**Example 2: 获取房间内用户信息1**



Input: 

```
tccli gme DescribeRoomInfo --cli-unfold-argument  \
    --RoomIds 11 \
    --SdkAppId 1400405451
```

Output: 
```
{
    "Response": {
        "RequestId": "50d01794-367f-4993-b4e3-cac5a4c1aaaa",
        "Result": 0,
        "RoomUsers": [
            {
                "RoomId": 11,
                "StrRoomId": "",
                "Uins": []
            }
        ]
    }
}
```

