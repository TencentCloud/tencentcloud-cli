**Example 1: 获取房间内用户信息**

获取房间内用户信息,RoomIds和StrRoomIds填一个即可,若都存在,则优先查询StrRoomIds。

Input: 

```
tccli gme DescribeRoomInfo --cli-unfold-argument  \
    --RoomIds 88888 \
    --StrRoomIds aaaaa \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "Result": 1,
        "RoomUsers": [
            {
                "RoomId": 0,
                "Uins": [
                    1111
                ],
                "StrRoomId": "aaaaa",
                "StrUins": [
                    ""
                ]
            }
        ],
        "RequestId": "50d01794-367f-4993-b4e3-cac5a4c1aaaa"
    }
}
```

**Example 2: 获取房间内用户信息1**

获取房间内用户信息1

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
        "Result": 1,
        "RoomUsers": [
            {
                "RoomId": 11,
                "Uins": [
                    1111
                ],
                "StrRoomId": "",
                "StrUins": [
                    ""
                ]
            }
        ],
        "RequestId": "50d01794-367f-4993-b4e3-cac5a4c1aaaa"
    }
}
```

