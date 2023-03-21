**Example 1: 查询云审计跟踪集列表**

在控制台或者使用接口，查看已经创建的跟踪集列表

Input: 

```
tccli cloudaudit DescribeAuditTracks --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Tracks": [
            {
                "TrackId": 1,
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
                "Status": 1,
                "CreateTime": "2021-01-14 14:43:38"
            }
        ],
        "TotalCount": 1,
        "RequestId": "2d4a7fba-bba8-452e-a99e-ccf11fdaa583"
    }
}
```

