**Example 1: 搜索模型版本**



Input: 

```
tccli tccatalog SearchModels --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --SnapshotBased True \
    --SnapshotId 369a522b-7792-4d9e-888a-8a3ce05c67a7
```

Output: 
```
{
    "Response": {
        "Models": [
            {
                "Audit": {
                    "CreatedAt": 1762429027050,
                    "CreatedTime": "2025-11-06 19:37:07",
                    "Creator": "fdafdaf@qq.com",
                    "LastModifiedAt": null,
                    "LastModifiedTime": "",
                    "LastModifier": ""
                },
                "CatalogName": "yb_test05",
                "LatestVersion": 1,
                "Name": "randomforest_join_2852187340369190912_202511061936",
                "Owner": "fdafdsa@qq.com",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4311819005374974997"
                    }
                ],
                "SchemaName": "sc_test05"
            }
        ],
        "SnapshotId": "369a522b-7792-4d9e-888a-8a3ce05c67a7",
        "TotalCount": 433,
        "RequestId": "78197b93-885a-46e1-8615-9e6ca3f9e2ee"
    }
}
```

