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
                "DatasourceName": "abc",
                "DatasourceId": "abc",
                "DatabaseName": "abc",
                "DatabaseId": "abc",
                "InstanceId": "abc",
                "DatasourceType": 1,
                "OriginDatabaseName": "abc",
                "OriginSchemaName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

