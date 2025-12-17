**Example 1: 创建模型**



Input: 

```
tccli tccatalog CreateModel --cli-unfold-argument  \
    --CatalogName yb_test05 \
    --SchemaName sc_test05 \
    --ModelName fdafads \
    --Comment fdasfd
```

Output: 
```
{
    "Response": {
        "Model": {
            "Audit": {
                "CreatedAt": 1760948948220,
                "CreatedTime": "2025-10-20 16:29:08",
                "Creator": "fdafd@qq.com",
                "LastModifiedAt": null,
                "LastModifiedTime": "",
                "LastModifier": ""
            },
            "Comment": "fdafdsa",
            "LatestVersion": 0,
            "Name": "fdafda",
            "Properties": [
                {
                    "Key": "tccatalog.identifier",
                    "Value": "tccatalog.v1.uid1210047631414366659"
                }
            ]
        },
        "RequestId": "968ddfc9-4552-4db5-9275-a933afa4d619"
    }
}
```

