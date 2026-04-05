**Example 1: UpdatePage**



Input: 

```
tccli wedata UpdatePage --cli-unfold-argument  \
    --PageAccessKey 3d7fd2be1768892231508b8f11877 \
    --PageVersion 5 \
    --DashboardAccessKey 800017322219413504 \
    --WorkspaceId 17678671667189298 \
    --DisplayName 无标题页面33
```

Output: 
```
{
    "Response": {
        "Data": {
            "CustomerRefId": "page-f7ea0fe3-a6a5-4d93-bbde-d3cb5aa31e42",
            "DisplayName": "无标题页面33",
            "PageAccessKey": "3d7fd2be1768892231508b8f11877",
            "PageLayout": "",
            "PageVersion": 6
        },
        "RequestId": "2af399cd-ba29-4e80-be8b-871e89685f58"
    }
}
```

