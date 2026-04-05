**Example 1: 获取dashbaord详情**



Input: 

```
tccli wedata GetApplicationDashboard --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --AccessKey 801934639037759488
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccessKey": "801934639037759488",
            "CreatedOn": "1769004117547",
            "CreatedUser": "",
            "CustomerRefId": "231e46c87c5949648d05398b369c1129",
            "DashboardSource": "MANUAL",
            "DashboardVersion": 0,
            "DatasetOrderList": [
                "a666ca9f1769004244669034c2c98"
            ],
            "DisplayName": "New Dashboard 2026-01-21 22:01:53",
            "ExecuteResourceId": "res-4d5a8928",
            "IsFavorite": false,
            "ModifiedOn": "1769084088595",
            "Owner": "700002164618",
            "OwnerUser": "wedata30-dev@tencent.com",
            "PageOrderList": [
                "5b2395691769004117553ca160ee3"
            ],
            "PermissionInfo": {
                "AuthList": [
                    "bi_dashboard_view"
                ],
                "Permission": "MANAGE"
            },
            "PublishStrategy": "",
            "PublishTime": "0",
            "PublishUin": "",
            "RefreshTime": "",
            "ResourceDirId": "",
            "ShareConfig": "{\"AccessType\":\"INVITED_ONLY\"}",
            "Status": "DRAFT",
            "UiSettings": ""
        },
        "RequestId": "475fdad1-8837-4a07-9c4f-2a0db314b7fb"
    }
}
```

