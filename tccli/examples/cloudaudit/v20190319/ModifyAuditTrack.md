**Example 1: 修改云审计跟踪**



Input: 

```
tccli cloudaudit ModifyAuditTrack --cli-unfold-argument  \
    --TrackId 1 \
    --Name audit \
    --ActionType Read \
    --ResourceType audit \
    --Status 0 \
    --TrackForAllMembers 1 \
    --EventNames LookUpEvents DeleteAudit \
    --Storage.StorageType cos \
    --Storage.StorageRegion ap-guangzhou \
    --Storage.StorageName audit-cos \
    --Storage.StoragePrefix test
```

Output: 
```
{
    "Response": {
        "RequestId": "2d4a7fba-bba8-452e-a99e-ccf11fdaa583"
    }
}
```

