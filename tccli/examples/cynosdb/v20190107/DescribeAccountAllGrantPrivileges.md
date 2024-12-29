**Example 1: 查询账号所有可授予权限**

查询账号所有可授予权限

Input: 

```
tccli cynosdb DescribeAccountAllGrantPrivileges --cli-unfold-argument  \
    --Account.Host % \
    --Account.AccountName andy \
    --ClusterId cynosdbmysql-j9i41hfv
```

Output: 
```
{
    "Response": {
        "DatabasePrivileges": [
            {
                "Db": "db1",
                "Privileges": [
                    "DROP",
                    "EXECUTE"
                ]
            }
        ],
        "GlobalPrivileges": [
            "CREATE",
            "ALTER"
        ],
        "PrivilegeStatements": [
            "GRANT CREATE, ALTER ON *.* TO 'test'@'%'",
            "GRANT DROP, EXECUTE ON `db1`.* TO 'andy'@'%'",
            "GRANT UPDATE, SHOW VIEW ON `db1`.`user1` TO 'andy'@'%'"
        ],
        "RequestId": "46bf5c40-3fc1-4030-ab84-a66355ae25ab",
        "TablePrivileges": [
            {
                "Db": "andy1",
                "Privileges": [
                    "UPDATE",
                    "SHOW VIEW"
                ],
                "TableName": "user1"
            }
        ]
    }
}
```

