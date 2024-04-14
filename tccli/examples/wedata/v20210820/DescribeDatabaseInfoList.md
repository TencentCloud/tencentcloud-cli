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
                "DatasourceName": "hive-78yughbhyg",
                "DatasourceId": "6789",
                "DatabaseName": "dbName",
                "DatabaseId": "89yuhi675tgy",
                "InstanceId": "y79ugibh2wefsdc",
                "DatasourceType": 1,
                "OriginDatabaseName": "dbNmae",
                "OriginSchemaName": "dbNmae"
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

