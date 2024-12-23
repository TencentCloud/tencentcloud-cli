**Example 1: 查询快照策略**



Input: 

```
tccli cfs DescribeAutoSnapshotPolicies --cli-unfold-argument  \
    --AutoSnapshotPolicyId asp-12345
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicies": [
            {
                "AliveDays": 30,
                "AppId": 1,
                "AutoSnapshotPolicyId": "asp-12345",
                "CreationTime": "2021-08-11 19:36:53",
                "CrossRegionsAliveDays": 0,
                "DayOfMonth": "",
                "DayOfWeek": "1,2,3,4,5,6,7",
                "FileSystemNums": 0,
                "FileSystems": [],
                "Hour": "11,12,13,14,15,16,17,18,19,20,21",
                "IntervalDays": 0,
                "IsActivated": 1,
                "NextActiveTime": "2024-12-12 16:00:00",
                "PolicyName": "default",
                "RegionName": "ap-guangzhou",
                "Status": "available"
            }
        ],
        "RequestId": "d803fa9b-cbd1-42a8-9098-c5f8a5bd763c",
        "TotalCount": 1
    }
}
```

