**Example 1: demo**



Input: 

```
tccli wedata ListWorkspaceAddableGroups --cli-unfold-argument  \
    --WorkspaceId 176214168140400 \
    --PageRequest.PageNumber 1 \
    --PageRequest.PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "",
                    "Description": "",
                    "GroupId": "17619023441437512",
                    "GroupName": "abel1031",
                    "UpdateTime": "",
                    "UserCount": 0
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 6,
                "TotalPageNumber": 6
            }
        },
        "RequestId": "7ab530b9-f54d-49cd-8c07-44521f0481c1"
    }
}
```

