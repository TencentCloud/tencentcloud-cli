**Example 1: CreatePage**



Input: 

```
tccli wedata CreatePage --cli-unfold-argument  \
    --CustomerRefId page-f7ea0fe3-a6a5-4d93-bbde-d3cb5aa31e42 \
    --DisplayName 无标题页面 3 \
    --PageType PAGE_TYPE_NORMAL \
    --DashboardAccessKey 800017322219413504 \
    --DashboardVersion 0 \
    --WorkspaceId 17678671667189298 \
    --PageOrderList b945260d1768546993350aefface7
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "800017322219413504",
            "DashboardVersion": 0,
            "PageAccessKey": "3d7fd2be1768892231508b8f11877",
            "PageVersion": 0
        },
        "RequestId": "6a5be9c1-c8db-4dd6-9724-84cc00ca4581"
    }
}
```

