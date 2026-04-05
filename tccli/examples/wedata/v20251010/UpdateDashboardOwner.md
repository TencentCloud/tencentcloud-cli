**Example 1: UpdateDashboardOwner**



Input: 

```
tccli wedata UpdateDashboardOwner --cli-unfold-argument  \
    --DashboardAccessKey 800017322219413504 \
    --WorkspaceId 17678671667189298 \
    --NewOwnerUin 700002164619
```

Output: 
```
{
    "Response": {
        "Data": {
            "DashboardAccessKey": "800017322219413504",
            "NewOwnerUin": "700002164619",
            "OldOwnerUin": "700002270529"
        },
        "RequestId": "c3ee3afd-0308-4ba2-ba7e-264baf7124a9"
    }
}
```

