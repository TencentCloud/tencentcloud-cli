**Example 1: 用户列表查询成功示例**



Input: 

```
tccli account GetGroupUserListIntl --cli-unfold-argument  \
    --GroupId 1274
```

Output: 
```
{
    "Response": {
        "GroupUserList": [
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收04",
                "Uid": 1000258
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收05",
                "Uid": 1000259
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收06",
                "Uid": 1000277
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收07",
                "Uid": 1000279
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收08",
                "Uid": 1000280
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收09",
                "Uid": 1000281
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "测试接收10",
                "Uid": 1000300
            },
            {
                "CreateTime": "2015-12-29 20:49:31",
                "Name": "fd",
                "Uid": 1000306
            }
        ],
        "RequestId": "e73b2b7c-508b-4645-a1ec-87f7de75ed72"
    }
}
```

