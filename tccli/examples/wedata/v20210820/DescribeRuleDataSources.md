**Example 1: 查询质量规则数据源**



Input: 

```
tccli wedata DescribeRuleDataSources --cli-unfold-argument  \
    --ProjectId 567898765632 \
    --DatasourceId 45678 \
    --DsTypes 1
```

Output: 
```
{
    "Response": {
        "Data": [
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

