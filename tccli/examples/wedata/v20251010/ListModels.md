**Example 1: ListModels**



Input: 

```
tccli wedata ListModels --cli-unfold-argument  \
    --CatalogName model \
    --SchemaName schema \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Audit": {
                        "CreatedAt": "1763561238376",
                        "Creator": "700002164619",
                        "CreatorName": "",
                        "LastModifiedAt": "1763561238376",
                        "LastModifier": "700002164619",
                        "LastModifierName": ""
                    },
                    "CatalogName": "model",
                    "Comment": "",
                    "Id": "tccatalog.v1.uid4431250594840088609",
                    "LatestVersion": "0",
                    "MetaOwner": {
                        "FullName": "model.schema.aaaabbbdd",
                        "Owner": "700002164619",
                        "OwnerName": "",
                        "OwnerType": "user"
                    },
                    "Name": "aaaabbbdd",
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
                    "SchemaName": "schema"
                }
            ],
            "NextPageToken": "eyJsaW1pdCI6MSwib2Zmc2V0IjoxfQ==",
            "TotalCount": "11"
        },
        "RequestId": "4bd7d3b8-d2d3-4417-976d-5adc5ceb59f5"
    }
}
```

