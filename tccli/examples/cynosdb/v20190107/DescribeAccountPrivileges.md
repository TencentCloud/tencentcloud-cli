**Example 1: 查询账号已有权限**

查询账号已有权限

Input: 

```
tccli cynosdb DescribeAccountPrivileges --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxxxxx \
    --AccountName test \
    --Host 1.1.1.1 \
    --Db testDb \
    --Type table \
    --TableName testTable
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

