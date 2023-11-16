**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli sqlserver DescribeDatabases --cli-unfold-argument  \
    --InstanceIdSet mssql-ds3p26cv
```

Output: 
```
{
    "Response": {
        "DBInstances": [
            {
                "DBDetails": [
                    {
                        "Accounts": [
                            {
                                "AccountType": "L3",
                                "Privilege": "ReadWrite",
                                "UserName": "L2"
                            },
                            {
                                "AccountType": "L1",
                                "Privilege": "DBOwner",
                                "UserName": "L0"
                            }
                        ],
                        "Charset": "Chinese_PRC_CI_AS",
                        "CreateTime": "2023-09-21 21:37:47",
                        "Encryption": "disable",
                        "InternalStatus": "ONLINE",
                        "Name": "test_db3",
                        "Remark": "--",
                        "Status": 2
                    },
                    {
                        "Accounts": [
                            {
                                "AccountType": "L3",
                                "Privilege": "ReadOnly",
                                "UserName": "L3"
                            },
                            {
                                "AccountType": "L3",
                                "Privilege": "ReadOnly",
                                "UserName": "L2"
                            },
                            {
                                "AccountType": "L1",
                                "Privilege": "DBOwner",
                                "UserName": "L0"
                            }
                        ],
                        "Charset": "Chinese_PRC_CI_AS",
                        "CreateTime": "2023-09-21 15:49:48",
                        "Encryption": "disable",
                        "InternalStatus": "ONLINE",
                        "Name": "test_db2",
                        "Remark": "--",
                        "Status": 2
                    },
                    {
                        "Accounts": [
                            {
                                "AccountType": "L3",
                                "Privilege": "ReadWrite",
                                "UserName": "L3"
                            },
                            {
                                "AccountType": "L3",
                                "Privilege": "ReadWrite",
                                "UserName": "L2"
                            },
                            {
                                "AccountType": "L1",
                                "Privilege": "DBOwner",
                                "UserName": "L0"
                            }
                        ],
                        "Charset": "Chinese_PRC_CI_AS",
                        "CreateTime": "2023-09-20 20:21:50",
                        "Encryption": "disable",
                        "InternalStatus": "ONLINE",
                        "Name": "test_db",
                        "Remark": "--",
                        "Status": 2
                    }
                ],
                "InstanceId": "mssql-ds3p26cv"
            }
        ],
        "RequestId": "1e4e038e-76eb-11ee-b611-525400853186",
        "TotalCount": 3
    }
}
```

