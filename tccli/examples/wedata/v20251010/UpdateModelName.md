**Example 1: 1**



Input: 

```
tccli wedata UpdateModelName --cli-unfold-argument  \
    --CatalogName model_catalog \
    --SchemaName model_schema \
    --ModelName aaaabbbdd \
    --NewName test_model
```

Output: 
```
{
    "Response": {
        "Data": {
            "Model": {
                "Audit": {
                    "CreatedAt": "1763561238376",
                    "Creator": "700002164619",
                    "CreatorName": "",
                    "LastModifiedAt": "1764748393975",
                    "LastModifier": "700002164619",
                    "LastModifierName": ""
                },
                "CatalogName": "model_catalog",
                "Comment": "",
                "Id": "tccatalog.v1.uid4431250594840088609",
                "LatestVersion": "0",
                "MetaOwner": {
                    "FullName": "model_catalog.model_schema.test_model",
                    "Owner": "700002164619",
                    "OwnerName": "",
                    "OwnerType": "user"
                },
                "Name": "test_model",
                "Properties": [
                    {
                        "Key": "tclake.mlflow.deployment_job_id",
                        "Value": ""
                    },
                    {
                        "Key": "tclake.wedata.type",
                        "Value": "MACHINE_LEARNING"
                    },
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4431250594840088609"
                    },
                    {
                        "Key": "tclake.wedata.workspace_id",
                        "Value": "17625100163628872"
                    }
                ],
                "SchemaName": "model_schema"
            }
        },
        "RequestId": "0bcdd29b-2d5f-4c69-8053-57cf7b5966db"
    }
}
```

