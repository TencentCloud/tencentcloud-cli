**Example 1: 查询白板房间列表**



Input: 

```
tccli tiw DescribeRoomList --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --Query * \
    --MaxSize 1000 \
    --TimeRange 1614519034000 1615190492000
```

Output: 
```
{
    "Response": {
        "RequestId": "7f560a64-d7fb-476b-89b9-2b90acc5c675",
        "RoomList": [
            {
                "RoomId": "108594741",
                "StartTime": 1614851243268,
                "EndTime": 1614851284952,
                "UserNumber": 1
            }
        ]
    }
}
```

