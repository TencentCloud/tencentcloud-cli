**Example 1: 1**



Input: 

```
tccli databuddy ListCatalogNames --cli-unfold-argument  \
    --MaxResults 1000 \
    --WorkspaceId 17899589369776893 \
    --PageToken 1: \
    --Types TABLE \
    --CatalogSources METALAKE
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "xzp_test",
                    "Namespace": [],
                    "CatalogSource": "SETATS"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "61c7184f-7f22-486f-9ca3-4d91a7fcd655"
    }
}
```

