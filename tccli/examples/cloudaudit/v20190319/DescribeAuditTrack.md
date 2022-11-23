**Example 1: 查询云审计跟踪集详情**



Input: 

```
tccli cloudaudit DescribeAuditTrack --cli-unfold-argument  \
    --TrackId 1
```

Output: 
```
{
    "Response": {
        "Name": "audit",
        "ActionType": "Read",
        "ResourceType": "audit",
        "EventNames": [
            "LookUpEvents"
        ],
        "Storage": {
            "StorageName": "audit-cos",
            "StoragePrefix": "test",
            "StorageRegion": "ap-guangzhou",
            "StorageType": "cos"
        },
        "TrackForAllMembers": 1,
        "Status": 1,
        "CreateTime": "2021-01-14 14:43:38",
        "RequestId": "2d4a7fba-bba8-452e-a99e-ccf11fdaa583"
    }
}
```

