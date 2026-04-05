**Example 1: 1**



Input: 

```
tccli wedata UpdateModelComment --cli-unfold-argument  \
    --CatalogName model \
    --SchemaName schema \
    --ModelName testaaa \
    --NewComment comment1
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
                    "LastModifiedAt": "1764747268183",
                    "LastModifier": "700002164619",
                    "LastModifierName": ""
                },
                "CatalogName": "model",
                "Comment": "comment1",
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
        "RequestId": "f1e41c7f-b3de-4884-bc7a-48455705b84b"
    }
}
```

