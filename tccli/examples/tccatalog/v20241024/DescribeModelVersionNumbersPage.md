**Example 1: 获取模型版本号**



Input: 

```
tccli tccatalog DescribeModelVersionNumbersPage --cli-unfold-argument  \
    --CatalogName master_model_catalog \
    --SchemaName master_model_schema \
    --ModelName master_model
```

Output: 
```
{
    "Response": {
        "SnapshotId": "",
        "TotalCount": 1,
        "Versions": [
            1
        ],
        "RequestId": "92571659-7928-406a-9323-bdfa92cfabdc"
    }
}
```

