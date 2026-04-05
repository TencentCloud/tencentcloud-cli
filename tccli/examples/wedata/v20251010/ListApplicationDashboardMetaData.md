**Example 1: 仪表盘元数据列表**



Input: 

```
tccli wedata ListApplicationDashboardMetaData --cli-unfold-argument  \
    --WorkspaceId 17663856806379896
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreatedBy": "700002164618",
                    "CreatedOn": "1768893167222",
                    "DisplayName": "New Dashboard 2026-01-20 15:12:44",
                    "Key": "801469279624839168",
                    "ModifiedBy": "700002164618",
                    "ModifiedOn": "1768983282238",
                    "Owner": "700002164618",
                    "Path": "/Workspace/Users/wedata30-dev@tencent.com@700002164618/New Dashboard 2026-01-20 15:12:44"
                }
            ],
            "PageResponse": {
                "PageNumber": 1,
                "PageSize": 10,
                "TotalCount": 44,
                "TotalPageNumber": 5
            }
        },
        "RequestId": "4f4957eb-c2e3-4892-aea8-56504c8a10fe"
    }
}
```

