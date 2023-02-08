**Example 1: 查询云数据库账户的权限信息**



Input: 

```
tccli cdb DescribeAccountPrivileges --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --Host 127.0.0.1 \
    --User ajnnw
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TablePrivileges": [
            {
                "Table": "user",
                "Privileges": [
                    "SELECT",
                    "INSERT"
                ],
                "Database": "mysql"
            }
        ],
        "GlobalPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE",
            "CREATE",
            "DROP",
            "REFERENCES",
            "INDEX",
            "ALTER",
            "SHOW DATABASES",
            "CREATE TEMPORARY TABLES",
            "LOCK TABLES",
            "EXECUTE",
            "CREATE VIEW",
            "SHOW VIEW",
            "CREATE ROUTINE",
            "ALTER ROUTINE",
            "EVENT",
            "TRIGGER"
        ],
        "ColumnPrivileges": [
            {
                "Column": "Host",
                "Table": "user",
                "Privileges": [
                    "SELECT",
                    "INSERT"
                ],
                "Database": "mysql"
            }
        ],
        "DatabasePrivileges": [
            {
                "Privileges": [
                    "CREATE",
                    "DROP"
                ],
                "Database": "jersey_test"
            }
        ]
    }
}
```

