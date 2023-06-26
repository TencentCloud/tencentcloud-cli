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
        "RequestId": "5062de55-d048-4d3b-92f9-b98b6f244360",
        "TotalCount": 1,
        "DBInstances": [
            {
                "InstanceId": "mssql-632eyp63",
                "DBDetails": [
                    {
                        "Name": "ceshi1",
                        "Charset": "Chinese_PRC_CI_AS",
                        "Remark": "测试db1",
                        "CreateTime": "2018-07-02 20:12:24",
                        "Status": 2,
                        "Accounts": [
                            {
                                "UserName": "victorwind",
                                "Privilege": "ReadWrite"
                            }
                        ],
                        "InternalStatus": "ONLINE"
                    }
                ]
            }
        ]
    }
}
```

