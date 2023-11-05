**Example 1: 查询数据库列表**

查询数据库列表

Input: 

```
tccli sqlserver DescribeDBs --cli-unfold-argument  \
    --InstanceIdSet mssql-njj2mtpl
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
                        "CreateTime": "2023-09-21 15:49:47",
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
        "RequestId": "dcab478c-770a-11ee-9264-525400853186",
        "TotalCount": 3
    }
}
```

