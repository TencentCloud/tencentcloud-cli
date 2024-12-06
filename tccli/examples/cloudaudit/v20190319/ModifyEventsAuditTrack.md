**Example 1: 修改操作审计跟踪集**



Input: 

```
tccli cloudaudit ModifyEventsAuditTrack --cli-unfold-argument  \
    --TrackId 1 \
    --Name track_test \
    --Status 1 \
    --Storage.StorageType cos \
    --Storage.StorageRegion ap-guangzhou \
    --Storage.StorageName costest \
    --Storage.StoragePrefix audita_config \
    --Storage.StorageAccountId 2342424 \
    --Storage.StorageAppId 353535 \
    --TrackForAllMembers 1 \
    --Filters.ResourceFields.0.ResourceType cvm \
    --Filters.ResourceFields.0.ActionType Read \
    --Filters.ResourceFields.0.EventNames ConsoleLogin
```

Output: 
```
{
    "Response": {
        "RequestId": "a60ef700-c3e4-4921-8d8f-30fc93dc07f4"
    }
}
```

