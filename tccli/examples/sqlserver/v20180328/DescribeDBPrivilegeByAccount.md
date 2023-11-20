**Example 1: 查询账号关联的数据库和权限信息**

查询账号关联的数据库和权限信息

Input: 

```
tccli sqlserver DescribeDBPrivilegeByAccount --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --InstanceId mssql-mz23h8n7 \
    --AccountName acc_test
```

Output: 
```
{
    "Response": {
        "DBList": [
            {
                "DBName": "db6_new",
                "Privilege": "DBOwner"
            },
            {
                "DBName": "db5_new",
                "Privilege": "ReadOnly"
            },
            {
                "DBName": "db4_new",
                "Privilege": "ReadWrite"
            },
            {
                "DBName": "db2_new",
                "Privilege": "ReadOnly"
            },
            {
                "DBName": "bigData",
                "Privilege": "DBOwner"
            }
        ],
        "RequestId": "0d8e4888-f464-11ed-8347-525400853186",
        "TotalCount": 5
    }
}
```

