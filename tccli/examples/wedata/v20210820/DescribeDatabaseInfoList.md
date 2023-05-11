**Example 1: 获取数据库信息**

获取数据库信息

Input: 

```
tccli wedata DescribeDatabaseInfoList --cli-unfold-argument  \
    --ConnectionType rpc \
    --Filters.0.Values cdlq-34sfds \
    --Filters.0.Name datasourceId \
    --Filters.1.Values hive \
    --Filters.1.Name type
```

Output: 
```
{
    "Response": {
        "DatabaseInfo": [
            {
                "DatabaseId": null,
                "DatabaseName": "",
                "OriginDatabaseName": "test",
                "OriginSchemaName": null
            }
        ],
        "RequestId": "21cf31f1-f8fd-4ecd-9217-594bba69d8ab"
    }
}
```

