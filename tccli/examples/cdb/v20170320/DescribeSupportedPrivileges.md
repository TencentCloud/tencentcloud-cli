**Example 1: 查询云数据库实例支持的权限信息**



Input: 

```
tccli cdb DescribeSupportedPrivileges --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "GlobalSupportedPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        "DatabaseSupportedPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        "TableSupportedPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "DELETE"
        ],
        "ColumnSupportedPrivileges": [
            "SELECT",
            "INSERT",
            "UPDATE",
            "REFERENCES"
        ]
    }
}
```

