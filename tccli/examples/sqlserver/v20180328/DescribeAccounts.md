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
        "InstanceId": "mssql-632eyp63",
        "TotalCount": 1,
        "Accounts": [
            {
                "Status": 2,
                "Remark": "--",
                "AccountType": "L0",
                "Host": "127.0.0.1",
                "Name": "xiaowei",
                "IsAdmin": true,
                "UpdateTime": "2020-09-22 00:00:00",
                "InternalStatus": "enable",
                "Authentication": "win-windows",
                "PassTime": "2020-09-22 00:00:00",
                "Dbs": [
                    {
                        "Privilege": "ReadOnly",
                        "DBName": "test"
                    }
                ],
                "CreateTime": "2020-09-22 00:00:00"
            }
        ],
        "RequestId": "5729760c-db94-4c71-a1ee-ebd43adae189"
    }
}
```

