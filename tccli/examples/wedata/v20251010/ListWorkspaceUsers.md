**Example 1: demo**



Input: 

```
tccli wedata ListWorkspaceUsers --cli-unfold-argument  \
    --WorkspaceId 1 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 3
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 3,
                "TotalCount": 0,
                "TotalPageNumber": 0
            }
        },
        "RequestId": "105dce72-aa16-4135-ac63-a32fec5fd04c"
    }
}
```

