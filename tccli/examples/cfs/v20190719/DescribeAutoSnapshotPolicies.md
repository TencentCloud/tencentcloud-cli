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
        "TotalCount": 1,
        "AutoSnapshotPolicies": [
            {
                "AutoSnapshotPolicyId": "abc",
                "PolicyName": "abc",
                "CreationTime": "abc",
                "FileSystemNums": 1,
                "DayOfWeek": "abc",
                "Hour": "abc",
                "IsActivated": 1,
                "NextActiveTime": "abc",
                "Status": "abc",
                "AppId": 1,
                "AliveDays": 1,
                "RegionName": "abc",
                "FileSystems": [
                    {
                        "CreationToken": "abc",
                        "FileSystemId": "abc",
                        "SizeByte": 1,
                        "StorageType": "abc",
                        "TotalSnapshotSize": 1,
                        "CreationTime": "abc",
                        "ZoneId": 1
                    }
                ],
                "DayOfMonth": "abc",
                "IntervalDays": 1,
                "CrossRegionsAliveDays": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

