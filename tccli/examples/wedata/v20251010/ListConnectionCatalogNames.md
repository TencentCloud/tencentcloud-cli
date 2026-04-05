**Example 1: demo1**



Input: 

```
tccli wedata ListConnectionCatalogNames --cli-unfold-argument  \
    --ConnectionId 1090-321-y78321 \
    --Types POSTGRE \
    --Keyword rad \
    --MaxResults 10 \
    --PageToken eyJvZmZzZXQiOjEwfQ== \
    --WorkspaceId 10898079321
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
        "RequestId": "0c7e1898-dbd5-4262-9419-f2f37fab952a"
    }
}
```

