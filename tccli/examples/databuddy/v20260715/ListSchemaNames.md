**Example 1: 1**



Input: 

```
tccli databuddy ListSchemaNames --cli-unfold-argument  \
    --MaxResults 1000 \
    --WorkspaceId 17899589369776893 \
    --CatalogName xzp_test \
    --CatalogSource SETATS
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "0924_demo",
                    "Namespace": [],
                    "CatalogSource": "SETATS"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "05890671-4e3a-4168-80b1-14fb10c872ea"
    }
}
```

