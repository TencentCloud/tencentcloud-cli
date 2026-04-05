**Example 1: demo**



Input: 

```
tccli wedata ListRelatedEntities --cli-unfold-argument  \
    --WorkspaceId zz-aa \
    --ConnectionId aa-cc \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 100
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageResponse": {
                "ExtendInfo": "",
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 0,
                "TotalPageNumber": 0
            }
        },
        "RequestId": "1bc5c996-eafa-4dfd-80a9-7711ae056da1"
    }
}
```

