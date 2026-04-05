**Example 1: UpdateServiceGroupMonitorConfig**



Input: 

```
tccli wedata UpdateServiceGroupMonitorConfig --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceGroupId 9f87c6d3-1d1e-4089-b49b-576486992365 \
    --InferenceTableCollectionEnabled True \
    --ClsDeliveryEnabled True \
    --LogConfig.LogsetId 2b59c4a1-1611-46fe-a04f-5933736721f5 \
    --LogConfig.TopicId 956ae47b-ea7e-496a-9b64-8cd81c5aaecc \
    --CatalogPath DataLakeCatalog \
    --SchemaPath tiny_wedata \
    --PayloadPath test013
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "xddsdas"
    }
}
```

