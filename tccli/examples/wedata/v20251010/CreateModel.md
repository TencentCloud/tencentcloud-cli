**Example 1: 1**



Input: 

```
tccli wedata CreateModel --cli-unfold-argument  \
    --CatalogName model \
    --SchemaName schema \
    --ModelName testaaa \
    --Comment comment
```

Output: 
```
{
    "Response": {
        "Data": {
            "Model": {
                "Audit": {
                    "CreatedAt": "1764746758163",
                    "Creator": "700002164619",
                    "CreatorName": "",
                    "LastModifiedAt": "1764746758163",
                    "LastModifier": "700002164619",
                    "LastModifierName": ""
                },
                "CatalogName": "model",
                "Comment": "comment",
                "Id": "tccatalog.v1.uid3752223554152542985",
                "LatestVersion": "0",
                "MetaOwner": {
                    "FullName": "model.schema.testaaa",
                    "Owner": "700002164619",
                    "OwnerName": "",
                    "OwnerType": "user"
                },
                "Name": "testaaa",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid3752223554152542985"
                    }
                ],
                "SchemaName": "schema"
            }
        },
        "RequestId": "a8f5c47f-4420-4822-b154-e6f8c3cc5167"
    }
}
```

