**Example 1: Pulling the list of instance accounts**



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
        "Accounts": [
            {
                "Name": "wang",
                "Remark": "wang test account",
                "CreateTime": "2018-07-27 22:24:54",
                "Status": 2,
                "UpdateTime": "2018-07-27 22:25:25",
                "PassTime": "2018-07-27 22:25:25",
                "Dbs": [],
                "InternalStatus": "enable"
            },
            {
                "Name": "test",
                "Remark": "N/A",
                "CreateTime": "2018-08-07 15:28:00",
                "Status": 2,
                "UpdateTime": "2018-08-07 15:28:00",
                "PassTime": "0000-00-00 00:00:00",
                "Dbs": [],
                "InternalStatus": "enable"
            }
        ]
    }
}
```

