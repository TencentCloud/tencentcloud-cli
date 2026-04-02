**Example 1: 创建schema**



Input: 

```
tccli wedata CreateSchema --cli-unfold-argument  \
    --CatalogName mico_test_1018 \
    --Name mico_schema_1027 \
    --Comment test create schema
```

Output: 
```
{
    "Response": {
        "RequestId": "b9c4c3f5-4c1c-4264-bc1c-2824578420ad",
        "Data": {
            "Schema": {
                "Audit": {
                    "CreatedAt": "1761627980744",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "0",
                    "LastModifier": ""
                },
                "Comment": "test create schema",
                "Name": "mico_schema_1027",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid1052210150648680833"
                    }
                ]
            }
        }
    }
}
```

