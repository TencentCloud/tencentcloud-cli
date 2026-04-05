**Example 1: RecoverPage**



Input: 

```
tccli wedata RecoverPage --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --PageAccessKey 3d7fd2be1768892231508b8f11877 \
    --DashboardAccessKey 800017322219413504 \
    --PageOrderList b945260d1768546993350aefface7 \
    --NewPageOrderList b945260d1768546993350aefface7 3d7fd2be1768892231508b8f11877
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "800017322219413504",
            "PageAccessKey": "3d7fd2be1768892231508b8f11877",
            "PageVersion": 4
        },
        "RequestId": "544b4f38-30f7-468e-85e6-806ffc318e98"
    }
}
```

