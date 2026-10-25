**Example 1: 1**



Input: 

```
tccli databuddy ListViewNames --cli-unfold-argument  \
    --CatalogName lsj_test \
    --SchemaName default \
    --WorkspaceId 17678671667189298 \
    --MaxResults 10 \
    --CatalogSource METALAKE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "NextPageToken": ""
        },
        "RequestId": "a1b85c4d-67e1-4915-9822-9f1cb88ed4f3"
    }
}
```

