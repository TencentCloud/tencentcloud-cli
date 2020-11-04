**Example 1: 查询状态为NORMAL的定期快照策略**



Input: 

```
tccli cbs DescribeAutoSnapshotPolicies --cli-unfold-argument  \
    --Filters.0.Name auto-snapshot-policy-state\
    --Filters.0.Values NORMAL\
    --Limit 3\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AutoSnapshotPolicySet": [
            {
                "DiskIdSet": [],
                "IsActivated": 1,
                "AutoSnapshotPolicyState": "NORMAL",
                "AutoSnapshotPolicyName": "快照策略1",
                "IsPermanent": 0,
                "NextTriggerTime": "2017-12-04 12:00:00",
                "AutoSnapshotPolicyId": "asp-lfp6fi4f",
                "Policy": [
                    {
                        "DayOfWeek": [
                            1,
                            4
                        ],
                        "Hour": [
                            12
                        ]
                    }
                ],
                "CreateTime": "2017-11-01 10:46:22",
                "RetentionDays": 7
            },
            {
                "DiskIdSet": [],
                "IsActivated": 1,
                "AutoSnapshotPolicyState": "NORMAL",
                "AutoSnapshotPolicyName": "快照策略2",
                "IsPermanent": 0,
                "NextTriggerTime": "2017-12-03 10:00:00",
                "AutoSnapshotPolicyId": "asp-nqu08k2l",
                "Policy": [
                    {
                        "DayOfWeek": [
                            0
                        ],
                        "Hour": [
                            10
                        ]
                    }
                ],
                "CreateTime": "2017-11-17 15:01:25",
                "RetentionDays": 7
            }
        ],
        "TotalCount": 2,
        "RequestId": "701c8a35-ed66-fc79-3795-5a1fa72cdbf1"
    }
}
```

