**Example 1: 拉取实例账户列表**



Input: 

```
tccli sqlserver DescribeAccounts --cli-unfold-argument  \
    --InstanceId mssql-j8kv137v
```

Output: 
```
{
    "Response": {
        "RequestId": "5729760c-db94-4c71-a1ee-ebd43adae189",
        "InstanceId": "mssql-632eyp63",
        "TotalCount": 1,
        "Accounts": [
            {
                "CreateTime": "2021-09-16 14:33:04",
                "Dbs": [],
                "InternalStatus": "enable",
                "IsAdmin": true,
                "Name": "xiaowei",
                "PassTime": "2021-09-16 14:33:55",
                "Remark": "--",
                "Status": 2,
                "UpdateTime": "2021-09-16 14:33:55"
            }
        ]
    }
}
```

