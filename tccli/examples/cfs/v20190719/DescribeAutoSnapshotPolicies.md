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
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "TotalCount": 1,
        "AutoSnapshotPolicies": [
            {
                "AutoSnapshotPolicyId": "asp-12345",
                "PolicyName": "未命名",
                "RegionName": "ap-guangzhou",
                "CreationTime": "2021-08-26 15:19:46",
                "AliveDays": 1,
                "DayOfWeek": "1",
                "Hour": "1",
                "IsActivated": 0,
                "AppId": 1255558577,
                "FileSystemNums": 0,
                "Status": "available",
                "NextActiveTime": "2021-11-22 01:00:00",
                "FileSystems": []
            }
        ]
    }
}
```

