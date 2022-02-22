**Example 1: 账号当前权限语句**



Input: 

```
tccli cynosdb DescribeAccountAllGrantPrivileges --cli-unfold-argument  \
    --Account.Host % \
    --Account.AccountName test \
    --ClusterId cynosdbmysql-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "DatabasePrivileges": [
            {
                "Db": "test1",
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
            "GRANT DROP, EXECUTE ON `test1`.* TO 'test'@'%'",
            "GRANT UPDATE, SHOW VIEW ON `test1`.`user1` TO 'test'@'%'"
        ],
        "RequestId": "46bf5c40-3fc1-4030-ab84-a66355ae25ab",
        "TablePrivileges": [
            {
                "Db": "test1",
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

