**Example 1: 删除元数据库**



Input: 

```
tccli dlc DeleteMetaDatabase --cli-unfold-argument  \
    --DatabaseName testDB \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "BatchId": "batch-45nyt3ee",
        "RequestId": "b577857e-041f-46c7-b5cf-4b3d3f50bc51",
        "TaskIdSet": [
            "e9663251-3a14-423a-b003-13c77c3fae11"
        ]
    }
}
```

