**Example 1: demo**



Input: 

```
tccli wedata ListConnectionSchemaNames --cli-unfold-argument  \
    --ConnectionId f5d22891-8727-4b48-9991-11251e27e1d4 \
    --CatalogName diveCatalog \
    --DatabaseName diveDB \
    --Keyword div \
    --MaxResults 10 \
    --PageToken eyJvZmZzZXQiOjEwfQ== \
    --WorkspaceId 17678671667189298
```

Output: 
```
{
    "Response": {
        "Data": {
            "Names": [
                "randyrren"
            ],
            "NextPageToken": ""
        },
        "RequestId": "bb86a692-afb8-4222-be09-6c5c1c8b3b4a"
    }
}
```

