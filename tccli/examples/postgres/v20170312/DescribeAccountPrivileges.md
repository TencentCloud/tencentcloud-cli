**Example 1: 查看账号类型**

查看账号类型

Input: 

```
tccli postgres DescribeAccountPrivileges --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName user_without_permission \
    --DatabaseObjectSet.0.ObjectType account \
    --DatabaseObjectSet.0.ObjectName user_without_permission
```

Output: 
```
{
    "Response": {
        "PrivilegeSet": [
            {
                "Object": {
                    "DatabaseName": "",
                    "ObjectName": "without_per",
                    "ObjectType": "account",
                    "SchemaName": "",
                    "TableName": ""
                },
                "PrivilegeSet": [
                    "tencentDBSuper"
                ]
            }
        ],
        "RequestId": "dc43ec52-efbe-4bde-b588-bfa427a8c29b"
    }
}
```

**Example 2: 查询数据库权限**

查询账号without_per对数据库user_database的权限

Input: 

```
tccli postgres DescribeAccountPrivileges --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName without_per \
    --DatabaseObjectSet.0.ObjectType database \
    --DatabaseObjectSet.0.ObjectName user_database
```

Output: 
```
{
    "Response": {
        "PrivilegeSet": [
            {
                "Object": {
                    "DatabaseName": "",
                    "ObjectName": "user_database",
                    "ObjectType": "database",
                    "SchemaName": "",
                    "TableName": ""
                },
                "PrivilegeSet": [
                    "CREATE",
                    "CONNECT",
                    "TEMPORARY"
                ]
            }
        ],
        "RequestId": "fc891ba1-8943-4116-8eb6-4696873d90c8"
    }
}
```

**Example 3: 查询模式权限**

查询账号without_per对user_database数据库下，user_schema的权限

Input: 

```
tccli postgres DescribeAccountPrivileges --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName without_per \
    --DatabaseObjectSet.0.ObjectType schema \
    --DatabaseObjectSet.0.ObjectName user_schema \
    --DatabaseObjectSet.0.DatabaseName user_database
```

Output: 
```
{
    "Response": {
        "PrivilegeSet": [
            {
                "Object": {
                    "DatabaseName": "user_database",
                    "ObjectName": "user_schema",
                    "ObjectType": "schema",
                    "SchemaName": "",
                    "TableName": ""
                },
                "PrivilegeSet": [
                    "USAGE",
                    "CREATE"
                ]
            }
        ],
        "RequestId": "410f0673-c35c-401e-97c8-d4e196d1f33c"
    }
}
```

**Example 4: 批量查询**

批量查询

Input: 

```
tccli postgres DescribeAccountPrivileges --cli-unfold-argument  \
    --DBInstanceId postgres-5cz25tr5 \
    --UserName without_per \
    --DatabaseObjectSet.0.ObjectType table \
    --DatabaseObjectSet.0.ObjectName users \
    --DatabaseObjectSet.0.DatabaseName user_database \
    --DatabaseObjectSet.0.SchemaName user_schema \
    --DatabaseObjectSet.1.ObjectType schema \
    --DatabaseObjectSet.1.ObjectName user_schema \
    --DatabaseObjectSet.1.DatabaseName user_database
```

Output: 
```
{
    "Response": {
        "PrivilegeSet": [
            {
                "Object": {
                    "DatabaseName": "user_database",
                    "ObjectName": "users",
                    "ObjectType": "table",
                    "SchemaName": "user_schema",
                    "TableName": ""
                },
                "PrivilegeSet": [
                    "DELETE",
                    "TRUNCATE",
                    "REFERENCES",
                    "TRIGGER",
                    "SELECT",
                    "INSERT",
                    "UPDATE"
                ]
            },
            {
                "Object": {
                    "DatabaseName": "user_database",
                    "ObjectName": "user_schema",
                    "ObjectType": "schema",
                    "SchemaName": "",
                    "TableName": ""
                },
                "PrivilegeSet": [
                    "CREATE",
                    "USAGE"
                ]
            }
        ],
        "RequestId": "41d71515-447d-4557-a799-3b60ad86323d"
    }
}
```

