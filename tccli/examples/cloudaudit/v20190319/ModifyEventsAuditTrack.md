**Example 1: 修改操作审计跟踪集**



Input: 

```
tccli cloudaudit ModifyEventsAuditTrack --cli-unfold-argument  \
    --TrackId 1 \
    --Name abc \
    --Status 1 \
    --Storage.StorageType abc \
    --Storage.StorageRegion abc \
    --Storage.StorageName abc \
    --Storage.StoragePrefix abc \
    --Storage.StorageAccountId abc \
    --Storage.StorageAppId abc \
    --TrackForAllMembers 1 \
    --Filters.ResourceFields.0.ResourceType abc \
    --Filters.ResourceFields.0.ActionType abc \
    --Filters.ResourceFields.0.EventNames abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

