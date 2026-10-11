**Example 1: 示例**



Input: 

```
tccli databuddy ListWorkspaceGroups --cli-unfold-argument  \
    --WorkspaceId 17851563773633788 \
    --GroupKeyword example \
    --RoleIds 2001 \
    --PageNumber 1 \
    --PageSize 11 \
    --GroupType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "",
                    "GroupId": "700002164618",
                    "GroupName": "all_users",
                    "GroupType": "0",
                    "Roles": [],
                    "Tags": [],
                    "UpdateTime": "",
                    "UserCount": 0
                }
            ],
            "PageNumber": 0,
            "PageSize": 0,
            "TotalCount": 0,
            "TotalPageNumber": 0
        },
        "RequestId": "a5c4fc49-defc-4230-b46f-36ce2d2a7168"
    }
}
```

