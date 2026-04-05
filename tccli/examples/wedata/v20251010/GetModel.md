**Example 1: 1**



Input: 

```
tccli wedata GetModel --cli-unfold-argument  \
    --CatalogName model \
    --SchemaName schema \
    --ModelName testaaa
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
        "RequestId": "4fa85c31-9655-4d13-9c57-a69adb20b1a2"
    }
}
```

