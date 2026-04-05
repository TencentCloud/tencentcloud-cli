**Example 1: GetServiceGroupMonitorConfig**



Input: 

```
tccli wedata GetServiceGroupMonitorConfig --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId 9f87c6d3-1d1e-4089-b49b-576486992365
```

Output: 
```
{
    "Response": {
        "Data": {
            "ServiceGroupId": "9f87c6d3-1d1e-4089-b49b-576486992365",
            "ClsDeliveryEnabled": 1,
            "ClsConfig": {
                "LogsetId": "2b59c4a1-1611-46fe-a04f-5933736721f5",
                "TopicId": "956ae47b-ea7e-496a-9b64-8cd81c5aaecc"
            },
            "InferenceTableCollectionEnabled": 1,
            "CatalogPath": "DataLakeCatalog",
            "SchemaPath": "tiny_wedata",
            "PayloadPath": "test013",
            "CreateTime": "0",
            "UpdateTime": "1764665676375",
            "TaskId": "afe915e1-b429-4991-b5a6-21e21d1f7357",
            "ErrorMessage": ""
        },
        "RequestId": "xddsdas"
    }
}
```

