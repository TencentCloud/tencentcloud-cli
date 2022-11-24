**Example 1: 创建跟踪集**



Input: 

```
tccli cloudaudit CreateAuditTrack --cli-unfold-argument  \
    --Name audit \
    --ActionType Read \
    --ResourceType audit \
    --Status 1 \
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
        "TrackId": 1,
        "RequestId": "2d4a7fba-bba8-452e-a99e-ccf11fdaa583"
    }
}
```

