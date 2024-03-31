**Example 1: 查询数据来源列表**



Input: 

```
tccli wedata DescribeDataBases --cli-unfold-argument  \
    --ProjectId 56789087 \
    --DatasourceId 56789 \
    --DsTypes 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "DatasourceName": "hive-78yughb",
                "DatasourceId": "567890",
                "DatabaseName": "dbName",
                "DatabaseId": "67tygu897iyugh",
                "InstanceId": "t67gy967yigu6789y",
                "DatasourceType": 1,
                "OriginDatabaseName": "test",
                "OriginSchemaName": "test"
            }
        ],
        "RequestId": "0ff4e8ae-ebea-4a41-8aa2-1f6bc4b68e69"
    }
}
```

