**Example 1: 1**

1

Input: 

```
tccli wedata DescribeTableBasicInfo --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --OrderFields.0.Name abc \
    --OrderFields.0.Direction abc
```

Output: 
```
{
    "Response": {
        "TableBasicInfoList": [
            {
                "TableId": "abc",
                "DatasourceId": "abc",
                "DatasourceName": "abc",
                "DatabaseId": "abc",
                "DatabaseName": "abc",
                "TableName": "abc",
                "EngineType": "abc",
                "TableType": "abc",
                "ProjectId": "abc",
                "ProjectName": "abc",
                "ProjectDisplayName": "abc",
                "TableOwnerId": "abc",
                "TableOwnerName": "abc",
                "StorageLocation": 0,
                "Description": "abc",
                "IsPartitionTable": 0,
                "PartitionColumns": [
                    "abc"
                ],
                "StorageFormat": "abc",
                "StorageSize": 1,
                "StorageSizeWithUnit": "abc",
                "TotalSizeMb": 1,
                "ReplicaCount": 0,
                "FileCount": [
                    0
                ],
                "PartitionCount": [
                    0
                ],
                "PartitionFieldCount": 0,
                "PartitionExpireDays": 0,
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: 错误1**

错误1

Input: 

```
tccli wedata DescribeTableBasicInfo --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name 1 \
    --Filters.0.Values 1 \
    --OrderFields.0.Name 1 \
    --OrderFields.0.Direction 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "8ded1268-1ffe-4d7c-af37-6d5eeb9868a4"
    }
}
```

