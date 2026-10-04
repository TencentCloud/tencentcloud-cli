**Example 1: 示例**



Input: 

```
tccli databuddy ListWorkspaces --cli-unfold-argument  \
    --WorkspaceId 17676143448574812 \
    --WorkspaceKeyword example \
    --StatusList 1 \
    --PageNumber 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [],
            "PageNumber": 1,
            "PageSize": 11,
            "TotalCount": 0,
            "TotalPageNumber": 0
        },
        "RequestId": "53f42163-04ec-4854-bb90-ce71f730e43e"
    }
}
```

