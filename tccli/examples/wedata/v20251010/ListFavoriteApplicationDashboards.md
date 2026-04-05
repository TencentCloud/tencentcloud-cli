**Example 1: ListFavoriteApplicationDashboards**



Input: 

```
tccli wedata ListFavoriteApplicationDashboards --cli-unfold-argument  \
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
                "NextPageToken": "eyJzZWFyY2hBZnRlclZhbHVlcyI6WzE3Njg0ODI1Mzg5NzMsIjc5OTY5NTU3NTIyMDI0ODU3NkAyNjAwNzM0OTNfYXAtZ3Vhbmd6aG91X0RBU0hCT0FSRCJdfQ=="
            }
        },
        "RequestId": "62dd7d7f-1fd7-4279-bf0c-00ab24347ccf"
    }
}
```

