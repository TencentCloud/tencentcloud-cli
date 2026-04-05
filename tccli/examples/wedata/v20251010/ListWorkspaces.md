**Example 1: 成功调用**



Input: 

```
tccli wedata ListWorkspaces --cli-unfold-argument  \
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
                    "CreateTime": "2025-11-05 17:05:49",
                    "Creator": {
                        "Nickname": "wedata30-dev@tencent.com",
                        "Uin": "700002164618",
                        "UserName": "wedata30-dev@tencent.com"
                    },
                    "Description": "abel_1105",
                    "ErrorReason": "",
                    "Status": 1,
                    "UpdateTime": "2025-11-05 17:05:49",
                    "WorkspaceId": "17623335490472931",
                    "WorkspaceName": "abel_1105",
                    "WorkspaceRegion": "ap-guangzhou"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 1,
                "TotalCount": 35,
                "TotalPageNumber": 35
            }
        },
        "RequestId": "6b6335ea-4d28-43b3-91fb-92e6d738fa01"
    }
}
```

