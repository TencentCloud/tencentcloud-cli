**Example 1: ListApplicationDashboardsV2**



Input: 

```
tccli wedata ListApplicationDashboardsV2 --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --TokenPageRequest.MaxResults 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "AccessKey": "801186950343671808",
                    "CreatedOn": "1768825854398",
                    "CreatedUser": "wedata30-test1@tencent.com",
                    "DashboardVersion": 26,
                    "DisplayName": "symontest 2026-01-19",
                    "ExecuteResourceId": "res-0aa8c845",
                    "IsFavorite": true,
                    "ModifiedOn": "1768889216928",
                    "OwnerUser": "wedata30-test1@tencent.com",
                    "PermissionList": [],
                    "ResourceDirId": "",
                    "ResourceId": "",
                    "Status": "DRAFT"
                }
            ],
            "TokenPageResponse": {
                "NextPageToken": "20"
            }
        },
        "RequestId": "f459202b-7423-4bfa-9e3b-864d9a0e0add"
    }
}
```

