**Example 1: 创建操作审计跟踪集**



Input: 

```
tccli cloudaudit CreateEventsAuditTrack --cli-unfold-argument  \
    --Name test_track \
    --Status 1 \
    --Storage.StorageType cos \
    --Storage.StorageRegion ap-guangzhou \
    --Storage.StorageName audit_test \
    --Storage.StoragePrefix audit_config \
    --Storage.StorageAccountId 2345345 \
    --Storage.StorageAppId 23456546 \
    --Filters.ResourceFields.0.ResourceType cam \
    --Filters.ResourceFields.0.ActionType Read \
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

