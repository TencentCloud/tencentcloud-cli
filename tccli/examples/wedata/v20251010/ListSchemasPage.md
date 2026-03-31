**Example 1: 获取TCLake Schema信息**



Input: 

```
tccli wedata ListSchemasPage --cli-unfold-argument  \
    --DatabaseName c4 \
    --ConnectionType TCLake \
    --WorkspaceId 17663856806379896
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "SchemaName": "default"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "d346a26d-5227-4a9c-a947-1400179da312"
    }
}
```

