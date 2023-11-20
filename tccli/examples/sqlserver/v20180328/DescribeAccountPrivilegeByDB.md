**Example 1: 查询数据库关联的账号和权限信息**

查询数据库关联的账号和权限信息

Input: 

```
tccli sqlserver DescribeAccountPrivilegeByDB --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --InstanceId mssql-mz23h8n7 \
    --DBName test_db
```

Output: 
```
{
    "Response": {
        "Accounts": [
            {
                "AccountType": "L1",
                "Privilege": "DBOwner",
                "UserName": "L1"
            }
        ],
        "RequestId": "33046d34-f461-11ed-9950-525400853186",
        "TotalCount": 1
    }
}
```

