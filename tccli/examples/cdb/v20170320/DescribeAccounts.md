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
        "TotalCount": 1,
        "Items": [
            {
                "Notes": "andy1",
                "Host": "172.1.1.1",
                "User": "andy",
                "ModifyTime": "2020-09-22 00:00:00",
                "ModifyPasswordTime": "2020-09-22 00:00:00",
                "CreateTime": "2020-09-22 00:00:00",
                "MaxUserConnections": 20,
                "OpenCam": true
            }
        ],
        "MaxUserConnections": 20,
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

