**Example 1: 查询账号已有权限**



Input: 

```
tccli cynosdb DescribeAccountPrivileges --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxxxx \
    --Host xxx \
    --AccountName xxx \
    --Db xxx \
    --Type table \
    --TableName xx
```

Output: 
```
{
    "Response": {
        "Privileges": [
            "select",
            "update",
            "delete",
            "create",
            "drop",
            "references",
            "index",
            "alter",
            "show_db",
            "create_tmp_table",
            "lock_tables",
            "execute",
            "create_view",
            "show_view",
            "create_routine",
            "alter_routine",
            "event",
            "trigger"
        ],
        "RequestId": "167350"
    }
}
```

