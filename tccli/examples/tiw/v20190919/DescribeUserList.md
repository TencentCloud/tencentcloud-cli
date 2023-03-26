**Example 1: 查询白板用户列表**



Input: 

```
tccli tiw DescribeUserList --cli-unfold-argument  \
    --SdkAppId 1400000001 \
    --RoomId 0 \
    --Query * \
    --MaxSize 1000 \
    --TimeRange 1614519034000 1615190492000
```

Output: 
```
{
    "Response": {
        "RequestId": "7f560a64-d7fb-476b-89b9-2b90acc5c675",
        "UserList": [
            {
                "UserId": "131001012",
                "StartTime": 1614519034000,
                "EndTime": 1615190492000
            }
        ]
    }
}
```

