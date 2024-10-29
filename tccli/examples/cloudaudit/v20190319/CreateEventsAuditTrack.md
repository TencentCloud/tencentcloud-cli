**Example 1: 创建操作审计跟踪集**



Input: 

```
tccli cloudaudit CreateEventsAuditTrack --cli-unfold-argument  \
    --Name test_track \
    --Status 1 \
    --Storage.StorageType cos \
    --Storage.StorageRegion ap-guangzhou \
    --Storage.StorageName test \
    --Storage.StoragePrefix 123 \
    --Storage.StorageAccountId  \
    --Storage.StorageAppId  \
    --Filters.ResourceFields.0.ResourceType cam \
    --Filters.ResourceFields.0.ActionType * \
    --Filters.ResourceFields.0.EventNames ConsoleLogin \
    --TrackForAllMembers 1
```

Output: 
```
{
    "Response": {
        "TrackId": 1,
        "RequestId": "abc"
    }
}
```

