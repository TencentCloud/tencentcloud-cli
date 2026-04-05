**Example 1: demo**

demo

Input: 

```
tccli wedata ListWorkspaceGroups --cli-unfold-argument  \
    --WorkspaceId 17621416814092400 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 0,
                "TotalPageNumber": 0
            }
        },
        "RequestId": "02718f07-9de4-4b71-98dc-26424ba7715a"
    }
}
```

