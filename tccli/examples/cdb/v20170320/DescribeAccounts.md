**Example 1: 查询云数据库的所有账号信息**



Input: 

```
tccli cdb DescribeAccounts --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 2,
        "Items": [
            {
                "Notes": "test",
                "Host": "localhost",
                "User": "test_user",
                "ModifyTime": "2020-11-10 01:00:00",
                "ModifyPasswordTime": "2020-11-10 01:00:00",
                "CreateTime": "2020-11-10 01:00:00"
            },
            {
                "Notes": "test2",
                "Host": "localhost",
                "User": "root",
                "ModifyTime": "2020-11-10 01:00:00",
                "ModifyPasswordTime": "2020-11-10 01:00:00",
                "CreateTime": "2020-11-10 01:00:00"
            }
        ]
    }
}
```

