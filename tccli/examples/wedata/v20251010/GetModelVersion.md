**Example 1: 1**



Input: 

```
tccli wedata GetModelVersion --cli-unfold-argument  \
    --CatalogName catalog_model \
    --SchemaName schema_model \
    --ModelName test_model \
    --ModelVersion 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModelVersion": {
                "Aliases": [],
                "Audit": {
                    "CreatedAt": "1764748587513",
                    "Creator": "700002164619",
                    "CreatorName": "",
                    "LastModifiedAt": "1764748587513",
                    "LastModifier": "700002164619",
                    "LastModifierName": ""
                },
                "CatalogName": "",
                "Comment": "",
                "ModelName": "",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid311552397959865813"
                    }
                ],
                "SchemaName": "",
                "Tags": [],
                "Uri": "http://130.1.1.1",
                "Version": "1"
            }
        },
        "RequestId": "e3280eeb-1946-4f4b-9ec8-842c419fb1a6"
    }
}
```

