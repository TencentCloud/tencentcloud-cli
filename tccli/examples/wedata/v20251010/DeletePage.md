**Example 1: DeletePage**



Input: 

```
tccli wedata DeletePage --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --PageAccessKey 548546db17688914777462250212d \
    --PageVersion 0 \
    --DashboardAccessKey 800017322219413504 \
    --DashboardVersion 0 \
    --PageOrderList b945260d1768546993350aefface7 548546db17688914777462250212d
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "800017322219413504",
            "DashboardVersion": 0
        },
        "RequestId": "662f20cc-cd13-413b-b030-eccbd35ead24"
    }
}
```

